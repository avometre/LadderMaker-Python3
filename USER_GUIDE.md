# Waltech Ladder Maker User Guide

## Table of Contents

1.  [Introduction](#introduction)
2.  [System Requirements and Installation](#system-requirements-and-installation)
3.  [User Interface Overview](#user-interface-overview)
4.  [Creating, Saving, and Opening Ladder Logic Diagrams](#creating-saving-and-opening-ladder-logic-diagrams)
5.  [Adding and Configuring Ladder Logic Elements](#adding-and-configuring-ladder-logic-elements)
6.  [Compiling and Uploading Programs to Arduino Boards](#compiling-and-uploading-programs-to-arduino-boards)
7.  [Troubleshooting](#troubleshooting)

## 1. Introduction

Welcome to the Waltech Ladder Maker! This guide will help you get started with using the Waltech Ladder Maker to create ladder logic programs for your Arduino projects.

## 2. System Requirements and Installation

*   **Operating System:** Windows, Linux, or macOS
*   **Python:** Version 3.x
*   **Dependencies:** PyQt5

To install the Waltech Ladder Maker, download the source code from the repository and ensure you have Python 3 and PyQt5 installed. You can then run the program by executing `python program/main.py` from the root directory.

## 3. User Interface Overview

The Waltech Ladder Maker user interface consists of the following main components:

*   **Menu Bar:** Located at the top of the window, the menu bar provides access to various functions:
    *   **File:** Options for creating new files, opening existing files, saving files, and closing the application.
    *   **Edit:** Undo and redo actions.
    *   **Hardware:** Options for selecting the target hardware (Waltech, Arduino Uno, Arduino Nano, Arduino Mega) and testing the USB connection.
    *   **Help:** Access to help resources, including this user guide, information about specific Arduino board I/O, and an "About" dialog.
*   **Toolbars:**
    *   **Elements Toolbar (Top):** Contains buttons for adding various ladder logic elements to the diagram, such as contacts (Normally Open, Normally Closed), coils, timers, counters, mathematical operations, comparison operators, PWM, and ADC elements.
    *   **Edit Toolbar (Left):** Provides tools for editing the ladder diagram, including adding rungs, adding OR wires, widening or narrowing the ladder, and deleting elements or rungs.
*   **Ladder Diagram View:** The central area of the window where you create and edit your ladder logic diagrams. You can drag and drop elements from the toolbar onto the rungs in this view.
*   **Mouse Coordinates:** Displays the current X and Y coordinates of the mouse cursor within the ladder diagram view.
*   **Undo/Redo Buttons:** Quick access buttons for undoing and redoing actions.
*   **Compile Button:** Initiates the process of compiling the ladder logic diagram into C code and uploading it to the selected hardware.
*   **Element List Table:** Located on the right side of the window, this table displays a list of all elements used in the current ladder diagram, along with their names, I/O assignments, element type, and location (rung, column).
*   **Output Console:** A text browser at the bottom right that displays messages related to compilation, uploading, and hardware testing.

*(Screenshots or diagrams could be added here in a later step if possible)*

## 4. Creating, Saving, and Opening Ladder Logic Diagrams

The Waltech Ladder Maker provides standard file operations for managing your ladder logic projects.

### Creating a New Diagram

*   To create a new ladder logic diagram, go to **File > New** in the menu bar.
*   This will clear the current diagram and initialize a new empty grid with a default number of rungs.

### Saving a Diagram

*   To save the current diagram:
    *   Go to **File > Save** in the menu bar.
    *   If the file has not been saved before, a "Save As" dialog will appear, allowing you to choose a location and filename. The default file extension is `.wlm` (Waltech Ladder Maker).
    *   If the file has been saved previously, it will be overwritten with the current changes.
*   To save the current diagram under a new name or in a different location:
    *   Go to **File > Save As** in the menu bar.
    *   A "Save As" dialog will appear, allowing you to choose a new location and filename.

### Opening an Existing Diagram

*   To open an existing ladder logic diagram:
    *   Go to **File > Open** in the menu bar.
    *   A file dialog will appear, allowing you to browse and select a `.wlm` file.
    *   Once a file is selected, it will be loaded into the ladder diagram view, and the element list table will be populated.
    *   The program will also attempt to restore the hardware selection (e.g., Arduino Uno, Waltech) that was active when the file was saved. If there are compatibility issues (e.g., the saved diagram uses I/O pins not available on the currently selected hardware), a warning may be displayed.

## 5. Adding and Configuring Ladder Logic Elements

Ladder logic diagrams are built by adding and configuring various elements on the rungs.

### Selecting an Element Tool

*   The **Elements Toolbar** (top) and **Edit Toolbar** (left) contain various tools for adding and modifying ladder logic elements and the diagram structure.
*   Click on a tool button to select it. The selected tool will remain active until another tool is chosen.

### Placing Elements on the Diagram

*   Once a tool is selected (e.g., "Normally Open Contact," "Coil"), move your mouse cursor over the desired cell in the **Ladder Diagram View**.
*   A blue marker will indicate the cell where the element will be placed.
*   **Left-click** in the cell to place the selected element.
*   For most elements, a configuration dialog will appear, allowing you to set its properties.

### Configuring Elements (Pop-up Dialogs)

*   When an element is placed, or when you **right-click** on an existing element, a pop-up dialog will appear. This dialog allows you to configure the element's specific parameters.
*   Common configuration options include:
    *   **Variable Name:** A user-defined name for the element. This name can be used to link elements (e.g., a contact can be linked to a coil by using the same variable name). Names should consist of letters, numbers, and underscores.
    *   **I/O Assignment:** For elements that interact with hardware (like contacts and coils), you can assign them to specific input or output pins on the selected hardware (e.g., `in_0`, `out_1`). You can also choose "internal" for virtual I/O that doesn't directly map to a physical pin.
    *   **Comment:** A brief description or note for the element.
    *   **Specific Parameters:** Different elements have unique parameters:
        *   **Contacts (Normally Open/Normally Closed):** Primarily configured with a variable name and I/O assignment.
        *   **Coils:** Configured with a variable name and I/O assignment. The state of a coil can control contacts with the same variable name.
        *   **Edge Detection (Falling Edge):** Creates a short pulse when the rung-in condition transitions from true to false.
        *   **Timers:**
            *   **Setpoint (Time Delay):** The duration (in seconds, up to 655 seconds) the rung-in condition must be true before the rung-out becomes true.
            *   The timer resets when the rung-in condition goes false.
        *   **Counters:**
            *   **Setpoint (Counts):** The number of times the rung-in condition must transition to true before the rung-out becomes true (up to 65535).
            *   A counter can be reset by linking its variable name to a coil.
        *   **Mathematical Operations (Plus, Minus, Multiply, Divide, Move):**
            *   These are typically placed on the far right of a rung.
            *   **Source A / Source B:** Can be constants or variable names of other elements.
            *   **Result:** The output of the operation, stored internally or assigned to an output. Values are typically 16-bit signed integers.
            *   Division by zero is handled without crashing but may result in specific defined behavior.
        *   **Comparison Operators (Equals, Greater Than, Less Than, Greater or Equal, Less Than or Equal):**
            *   These elements become "conductive" (rung-out becomes true) if the comparison is true.
            *   **Source A / Source B:** Can be constants or variable names of other elements.
        *   **PWM (Pulse Width Modulation):**
            *   Placed on the far right of a rung. Active when the rung-in is true.
            *   Requires compatible hardware (e.g., Arduino). The option will be disabled if the selected hardware doesn't support PWM.
            *   **Output Pin:** Assign to a PWM-capable hardware pin.
            *   **Duty Cycle/Value:** Set the PWM duty cycle.
            *   If multiple PWM elements target the same output pin, the first active one in the scan usually takes precedence.
        *   **ADC (Analog-to-Digital Converter):**
            *   Placed on the far right of a rung. Active when the rung-in is true.
            *   Reads an analog voltage and converts it to a digital value (typically 0-1023 for a 10-bit ADC with a 5V reference).
            *   Requires compatible hardware.
            *   **Input Pin:** Assign to an ADC-capable hardware pin.
            *   The result is stored internally and can be used by other elements (e.g., comparison or math operations).

### Editing the Ladder Structure

*   **Add Rung:** Select the "addRung" tool from the left toolbar. Click in the diagram where you want to insert a new horizontal rung. A marker will show the proposed insertion point.
*   **OR Wire (Vertical Wire):** Select the "OR wire" tool. Click between rungs in the same column to add or remove a vertical wire. This connects rungs электрически, creating an OR logic branch. This tool can also be used to widen or shrink existing OR branches.
*   **Widen:** Select the "Widen" tool. Click in the diagram to make the entire ladder one element width wider.
*   **Narrow:** Select the "Narrow" tool. Click in the diagram to make the entire ladder one element width narrower, if possible (it won't delete columns with elements).
*   **Delete (DEL):** Select the "DEL" tool.
    *   Click on an element to delete it.
    *   Click on an empty part of a rung to delete the entire rung (if it's empty or only contains basic rung lines).
    *   To delete OR branches, use the "OR wire" tool to remove the vertical connections.

### Undo and Redo

*   You can undo most actions by going to **Edit > undo** or pressing `Ctrl+Z`.
*   You can redo actions by going to **Edit > redo** or pressing `Ctrl+R`.
*   There are also Undo and Redo buttons in the main interface for quick access.
*   The system keeps a history of up to 30 actions for undo/redo.

### "What's This?" Help

*   For a quick description of most toolbar buttons and their corresponding elements, you can use the "What's This?" feature.
*   Go to **Help > WhatsThis** in the menu bar. The cursor will change to a help pointer.
*   Click on a toolbar button to see a pop-up explanation of its function and basic usage.

## 6. Compiling and Uploading Programs to Arduino Boards

Once you have created your ladder logic diagram, you can compile it into C code and upload it to your selected Arduino-compatible hardware.

### Selecting Hardware

*   Before compiling, ensure you have selected the correct target hardware.
*   Go to **Hardware** in the menu bar.
*   Choose your board from the list:
    *   Waltech (This might be a proprietary board or a default setting)
    *   Arduino Uno
    *   Arduino Nano
    *   Arduino Mega
*   When you select a hardware type, the availability of certain elements (like PWM and ADC) might change based on the board's capabilities.
*   If you try to switch to a hardware type that doesn't support the I/O, PWM, or ADC elements currently used in your diagram, a warning dialog will appear, and the switch might be prevented.

### Testing USB Connection

*   It's recommended to test the USB connection to your hardware before attempting to compile and upload.
*   Go to **Hardware > Test USB**.
*   The **Output Console** will display messages indicating the status of the USB connection, programmer, and controller. This helps ensure that the software can communicate with your board.

### Compiling and Uploading

1.  **Initiate Compilation:**
    *   Click the **Compile** button (usually labeled "compile" or an icon, located near the top or as part of the main interface controls).
    *   Alternatively, there might be a similar option in one of the menus.
2.  **Compilation Process:**
    *   The Waltech Ladder Maker will first convert your ladder logic diagram into an internal outline representation.
    *   Then, this outline is translated into C code.
    *   The generated C code is compiled using `avr-gcc` (part of the WinAVR toolkit or a similar AVR GCC toolchain if you're on Linux/macOS).
    *   The **Output Console** will display messages from the `avr-gcc` compiler, including any errors or warnings.
3.  **Uploading to Hardware:**
    *   If the C code compiles successfully, a `.hex` file is generated.
    *   The software then uses `avrdude` to upload this `.hex` file to the selected Arduino board via the USB connection.
    *   The **Output Console** will also display messages from `avrdude` regarding the upload process.
4.  **Troubleshooting Compilation/Upload Issues:**
    *   **Compiler Errors:** If `avr-gcc` reports errors, they will appear in the Output Console. These usually indicate a problem with how the ladder logic translates to C, or an issue with the C boilerplates or core logic. Review your ladder diagram for any unusual configurations.
    *   **Upload Errors:** If `avrdude` reports errors, these usually relate to:
        *   Incorrect hardware selected in the software.
        *   Incorrect port selected or driver issues for the USB-to-serial converter (e.g., CH340, FTDI).
        *   The board not being connected properly or not being in bootloader mode (though most Arduinos auto-reset for upload).
        *   Permission issues (on Linux, you might need to be part of the `dialout` group or have udev rules set up for Arduino).
        *   The wrong programmer selected in `avrdude`'s configuration (though this is usually handled internally by the software).

### Generated Files

*   During the process, several files might be generated in a subfolder (e.g., `program/C/` or a build directory):
    *   `main.c`: The generated C code.
    *   `.hex` file: The compiled machine code ready for upload.
    *   Other intermediate files (`.o`, `.lst`, etc.).

## 7. Troubleshooting

Here are some common issues and potential solutions when using the Waltech Ladder Maker:

*   **Application Fails to Start:**
    *   **Missing Python:** Ensure Python 3.x is installed and accessible in your system's PATH.
    *   **Missing PyQt5:** Ensure PyQt5 is installed for your Python environment. You can typically install it using pip: `pip install PyQt5`.
    *   **Corrupted Files:** If you've modified the source code, ensure there are no syntax errors. Try re-downloading or cloning the original source code.

*   **Elements Don't Appear or Behave Unexpectedly:**
    *   **Incorrect Tool Selected:** Double-check that you have the correct element tool selected from the toolbar before clicking on the diagram.
    *   **Configuration Errors:** Right-click the element to open its configuration dialog and verify all parameters are set correctly. Pay attention to variable names and I/O assignments.
    *   **Hardware Incompatibility:** Some elements (like PWM or ADC) might not function if the selected hardware doesn't support them. Check your hardware selection under the "Hardware" menu.

*   **Cannot Save or Open Files:**
    *   **Permissions:** Ensure the application has write permissions for the directory where you're trying to save files, and read permissions for the directory from which you're trying to open files.
    *   **Invalid Filename/Path:** Check for any special characters in the filename or path that might be causing issues.
    *   **Corrupted `.wlm` file:** If an existing `.wlm` file fails to open, it might be corrupted. Try opening a different file or a backup if available.

*   **Compilation Errors (in Output Console):**
    *   **Syntax Errors in Ladder Logic:** While the GUI tries to prevent this, complex or unusual ladder configurations might lead to C code that `avr-gcc` cannot compile. Simplify the problematic part of your ladder diagram.
    *   **Toolchain Issues:** Ensure `avr-gcc` (usually part of WinAVR on Windows, or installed separately on Linux/macOS) is correctly installed and in the system's PATH if the application relies on external calls. The application seems to bundle WinAVR in `helpers/WinAVR/`, so issues here might relate to the bundled version's compatibility with your OS or if its path is not correctly resolved by the application.
    *   **Conflicting Variable Names:** While the application should handle this, ensure variable names used in your ladder logic don't inadvertently conflict with C keywords or internal variables used by the generated code. Stick to alphanumeric names with underscores.

*   **Upload Errors (in Output Console, from `avrdude`):**
    *   **Incorrect Port:** Your Arduino might not be on the COM port that `avrdude` is trying to use.
        *   In the Arduino IDE, check which port your board is connected to. The Waltech Ladder Maker might auto-detect or have a way to configure this, but if not, this is a common issue. (The current codebase exploration hasn't revealed a port selection GUI, so it might be hardcoded or auto-detected).
        *   Ensure you have the correct drivers installed for your Arduino's USB-to-serial chip (e.g., CH340, FTDI).
    *   **Wrong Hardware Selected:** Ensure the hardware selected in the "Hardware" menu matches the connected board. Different boards use different microcontrollers and bootloaders, affecting `avrdude` parameters.
    *   **Board Not Connected or Powered:** Verify the USB cable is securely connected and the board is powered.
    *   **Bootloader Issues:** Rarely, an Arduino's bootloader can become corrupted. You might need to re-burn the bootloader using an ISP programmer.
    *   **Permissions (Linux):** You may need to add your user to the `dialout` group (`sudo usermod -a -G dialout yourusername`) and log out/in. Alternatively, udev rules might be needed for Arduino devices.
    *   **`avrdude.conf` Issues:** The `avrdude.conf` file (likely in `helpers/`) contains definitions for programmers and microcontrollers. If this file is corrupted or misconfigured for the target, uploads will fail.

*   **UI Glitches or Freezes:**
    *   **Complex Diagrams:** Very large or complex ladder diagrams might strain the UI, especially during redraws. Try to keep diagrams manageable.
    *   **PyQt5 Bugs:** While generally stable, specific interactions could trigger bugs in the PyQt5 library or the application's handling of it. Ensure you're using a reasonably up-to-date version of PyQt5.
    *   **Operating System or Driver Issues:** Graphics driver issues can sometimes affect Qt applications.

*   **"What's This?" Help Not Working:**
    *   Ensure you first click **Help > WhatsThis** to enter "What's This?" mode before clicking on a toolbar item.

If you encounter an issue not listed here, try to note the steps to reproduce it and any messages in the Output Console. This information can be helpful for debugging.
