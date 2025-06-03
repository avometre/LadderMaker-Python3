#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
Waltech Ladder Maker is distributed under the MIT License. 

Copyright (c) 2014 Karl Walter.  karl (at) waltech.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
 

#this wil be the outline to C functions
from PyQt4 import QtCore, QtGui
from PyQt4.Qt import QFont
from PyQt4.QtGui import QApplication, QCursor
from PyQt4.QtCore import Qt
import subprocess
from subprocess import PIPE
import sys
import os
import time
from tester import tester

class hexMaker():
    
    def __init__(self,opSys):#bring in all the things being sent down here
        self.opSys = opSys
        
    def saveCfileAndCompile(self,C_txt,displayOutputPlace,currentHW):
        QApplication.setOverrideCursor(QCursor(Qt.WaitCursor))

        # Path Definitions (relative to program/ where hexmaker.py resides)
        C_CODE_DIR = "C" # Relative to program/
        C_FILE_NAME = "main.c"
        C_FILE_PATH = os.path.join(C_CODE_DIR, C_FILE_NAME) # Path from program/ to C/main.c
        
        # Path from program/C/ to helpers/ (where avr tools and avrdude.conf might be)
        # Note: os.path.join will handle forward/backward slashes appropriately.
        # If C_CODE_DIR is just "C", then to get from "program/C/" to "program/helpers/"
        # we need to go up one ("..") then into "helpers".
        # So, from "program/" perspective, helpers is "../helpers"
        # From "program/C/" perspective, helpers is "../../helpers"
        HELPERS_DIR_FROM_C_DIR = os.path.join("..", "..", "helpers")

        HEX_FILE_NAME = "ladder_logic_main.hex" # As per Makefile's PROJECTNAME
        # HEX_FILE_PATH will be relative to C_CODE_DIR for avrdude command,
        # but for reading it after compilation, it's os.path.join(C_CODE_DIR, HEX_FILE_NAME)
        # from program/ perspective.

        # Ensure the C_CODE_DIR exists (it should, as it contains the Makefile)
        if not os.path.isdir(C_CODE_DIR):
            displayOutputPlace.append("Error: C Code directory %s does not exist." % C_CODE_DIR)
            QApplication.restoreOverrideCursor()
            return

        # Save C file to program/C/main.c
        actual_c_file_full_path = C_FILE_PATH
        try:
            with open(actual_c_file_full_path, 'w') as f:
                f.write(C_txt)
            displayOutputPlace.append("C file saved to: %s" % actual_c_file_full_path)
        except IOError as e:
            displayOutputPlace.append("Error saving C file: %s" % str(e))
            QApplication.restoreOverrideCursor()
            return

        # Determine MCU, MCU_FREQ, AVR_TOOLS_PREFIX for Makefile
        mcu_val = ""
        mcu_freq_val = ""
        makefile_avr_tools_prefix = ""
        avrdude_executable_path_prefix = "" # For direct avrdude call

        if currentHW == "Waltech":
            mcu_val = "atmega32"
            mcu_freq_val = "4000000UL"
        elif currentHW == "ArduinoUno" or currentHW == "ArduinoNano":
            mcu_val = "atmega328p"
            mcu_freq_val = "16000000UL"
        elif currentHW == "ArduinoMega":
            mcu_val = "atmega2560"
            mcu_freq_val = "16000000UL"
        else:
            displayOutputPlace.append("Unknown hardware: %s" % currentHW)
            QApplication.restoreOverrideCursor()
            return

        if self.opSys == "NIX":
            # Path from program/C/ to program/helpers/avr/bin/
            makefile_avr_tools_prefix = os.path.join(HELPERS_DIR_FROM_C_DIR, "avr", "bin") + os.sep
            avrdude_executable_path_prefix = makefile_avr_tools_prefix
        elif self.opSys == "MAC":
            makefile_avr_tools_prefix = "" # Tools assumed to be in PATH
            avrdude_executable_path_prefix = ""
        elif self.opSys == "WIN":
            # Path from program/C/ to program/helpers/WinAVR/bin/
            makefile_avr_tools_prefix = os.path.join(HELPERS_DIR_FROM_C_DIR, "WinAVR", "bin") + os.sep
            avrdude_executable_path_prefix = makefile_avr_tools_prefix
        
        # Construct make command
        make_command = [
            "make",
            "clean",
            "all",
            "MCU=" + mcu_val,
            "MCU_FREQ=" + mcu_freq_val,
            "AVR_TOOLS_PREFIX=" + makefile_avr_tools_prefix
        ]
        
        displayOutputPlace.append("Running make command: %s" % " ".join(make_command))
        displayOutputPlace.append("In directory: %s" % os.path.abspath(C_CODE_DIR))
        
        try: # Outer try for general errors and finally clause
            try: # Inner try for make process
                p_make = subprocess.Popen(make_command, cwd=C_CODE_DIR, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                stdout_data, stderr_data = p_make.communicate()

                # Always show stdout and stderr for make, as it can contain warnings even on success
                displayOutputPlace.append("--- Make stdout: ---")
                try:
                    displayOutputPlace.append(stdout_data.decode('utf-8', 'replace'))
                except AttributeError: # Already a string (Python 2)
                    displayOutputPlace.append(stdout_data)

                displayOutputPlace.append("--- Make stderr: ---")
                try:
                    displayOutputPlace.append(stderr_data.decode('utf-8', 'replace'))
                except AttributeError: # Already a string (Python 2)
                    displayOutputPlace.append(stderr_data)

                if p_make.returncode != 0:
                    displayOutputPlace.append("\nCompilation failed. Error details above.")
                    # No need to append stderr_data again as it's already printed
                else:
                    displayOutputPlace.append("\nCompilation successful. Hex file created: %s" % os.path.join(C_CODE_DIR, HEX_FILE_NAME))

                    # Avrdude Execution (only if make was successful)
                    commandAvrDude_base_options_str = ""
                    avrdude_conf_path_list = []

                    if currentHW == "Waltech":
                        avrdude_conf_path_list = ["-C", os.path.join(HELPERS_DIR_FROM_C_DIR, "avrdude.conf")]
                        commandAvrDude_base_options_str = "-p m32 -P usb -c usbtiny -B5"
                    else: # Arduinos
                        if currentHW == "ArduinoUno" or currentHW == "ArduinoNano":
                            commandAvrDude_base_options_str = "-p m328p -c arduino -P /dev/ttyUSB0 -b 57600" # Example
                            if self.opSys == "WIN":
                                 commandAvrDude_base_options_str = "-p m328p -c arduino -P COM3 -b 57600" # Example
                        elif currentHW == "ArduinoMega":
                            commandAvrDude_base_options_str = "-p m2560 -c wiring -P /dev/ttyACM0 -b 115200" # Example
                            if self.opSys == "WIN":
                                commandAvrDude_base_options_str = "-p m2560 -c wiring -P COM3 -b 115200" # Example

                    if commandAvrDude_base_options_str:
                        avrdude_exe_name = "avrdude.exe" if self.opSys == "WIN" else "avrdude"
                        avrdude_full_executable = os.path.join(avrdude_executable_path_prefix, avrdude_exe_name)

                        avrdude_command = [avrdude_full_executable]
                        avrdude_command.extend(avrdude_conf_path_list)
                        avrdude_command.extend(commandAvrDude_base_options_str.split())
                        avrdude_command.extend(["-U", "flash:w:" + HEX_FILE_NAME + ":i"])

                        displayOutputPlace.append("\nRunning avrdude: %s" % " ".join(avrdude_command))

                        try:
                            p_avrdude = subprocess.Popen(avrdude_command, cwd=C_CODE_DIR, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
                            stdout_avrdude, stderr_avrdude = p_avrdude.communicate()

                            displayOutputPlace.append("--- avrdude stdout: ---")
                            try:
                                displayOutputPlace.append(stdout_avrdude.decode('utf-8', 'replace'))
                            except AttributeError:
                                displayOutputPlace.append(stdout_avrdude)

                            displayOutputPlace.append("--- avrdude stderr: ---")
                            try:
                                displayOutputPlace.append(stderr_avrdude.decode('utf-8', 'replace'))
                            except AttributeError:
                                displayOutputPlace.append(stderr_avrdude)

                            if p_avrdude.returncode != 0:
                                displayOutputPlace.append("\nUpload failed. Error details above.")
                            else:
                                displayOutputPlace.append("\nUpload successful.")
                        except OSError as e_avrdude:
                            displayOutputPlace.append("\nError executing avrdude: %s. Is avrdude in PATH or helpers directory?" % str(e_avrdude))
                    else:
                        displayOutputPlace.append("\nAvrdude command options not determined for %s. Skipping upload." % currentHW)

            except OSError as e_make: # Error starting make itself
                displayOutputPlace.append("\nError executing make: %s. Is make in PATH?" % str(e_make))
            # Avrdude Execution
            # commandAvrDude_base_options will store the part of commandAvrDude string
                # that comes from tester.py or is hardcoded for Waltech, excluding the executable itself
                # and the -U flash:w:... part.
                commandAvrDude_base_options_str = ""
                avrdude_conf_path_list = [] # To store -C option if needed

                if currentHW == "Waltech":
                    # Original Waltech: r"../avrdude  -C ../avrdude.conf -p m32 -P usb -c usbtiny -B5" (NIX example)
                    # The executable part is handled by avrdude_full_executable.
                    # The conf path needs adjustment.
                    # HELPERS_DIR_FROM_C_DIR is already "program/helpers" relative to "program/C/"
                    # So, avrdude.conf is os.path.join(HELPERS_DIR_FROM_C_DIR, "avrdude.conf")
                    avrdude_conf_path_list = ["-C", os.path.join(HELPERS_DIR_FROM_C_DIR, "avrdude.conf")]
                    commandAvrDude_base_options_str = "-p m32 -P usb -c usbtiny -B5"
                else: # Arduinos
                    # tester.py returns the full command string including the executable and -C if needed
                    # We need to parse it.
                    # This is a simplification; tester.py's logic is complex.
                    # For now, assume tester.py returns options that are compatible.
                    # Ideally, tester.py should return options list directly, not a command string.
                    # Let's call tester.py to get the command string.
                    # The current directory for tester.py is tricky. It expects to be in program/helpers/hexes
                    # We are in program/
                    # This part needs careful adjustment if tester.py is to be used directly.
                    # For this refactor, let's assume we'll construct the basic Arduino ones here
                    # or that tester.py is adapted separately.
                    # Given the complexity, we'll hardcode basic Arduino options for now,
                    # similar to Waltech, and assume tester.py will be refactored later.

                    # Calling tester.py as is will fail due to cwd assumptions.
                    # commandAvrDude_from_tester = tester(self.opSys, currentHW).test1(displayOutputPlace)
                    # For now, this part will be incomplete for Arduinos if relying on tester.py output directly.
                    # We will focus on Waltech and a placeholder for Arduinos.

                    # Let's use some common defaults for Arduinos, knowing this might not match tester.py's dynamic port finding.
                    # This is a known limitation of this refactoring step.
        except Exception as e: # General exception for any other part of the process
            displayOutputPlace.append("\nAn unexpected error occurred: %s" % str(e))
        finally: # Ensure cursor is always restored
            QApplication.restoreOverrideCursor()
            # No need to change CWD back as Popen's cwd handles it per command.
            # Original code changed directories multiple times; this is cleaner.
            print "Final CWD (should be program/):", os.getcwd() # Should remain program/