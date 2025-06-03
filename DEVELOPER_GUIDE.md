# Waltech Ladder Maker Developer Guide

## Table of Contents

1.  [Introduction](#introduction)
2.  [Project Structure and Architecture](#project-structure-and-architecture)
3.  [Main Modules and Classes](#main-modules-and-classes)
    *   [program/main.py](#programmainpy)
    *   [program/managegrid.py](#programmanagegridpy)
    *   [program/LadderToOutLine.py](#programladdertooutlinepy)
    *   [program/OutLineToC.py](#programoutlinetocpy)
    *   [program/popupDialogs.py](#programpopupdialogspy)
    *   [program/mainwindow_ui.py](#programmainwindow_uipy)
    *   [program/tester.py](#programtesterpy)
    *   [Other UI Files (*_ui.py)](#other-ui-files)
4.  [Adding New Ladder Logic Elements](#adding-new-ladder-logic-elements)
5.  [Building and Debugging](#building-and-debugging)
6.  [Coding Conventions and Style Guidelines](#coding-conventions-and-style-guidelines)

## 1. Introduction

This guide provides information for developers looking to understand, modify, or extend the Waltech Ladder Maker application.

## 2. Project Structure and Architecture

The Waltech Ladder Maker project is primarily organized into two main directories:

*   **`program/`**: This is the core of the application.
    *   It contains all the Python source code (`.py` files) for the application logic, UI interactions, and backend processing.
    *   Qt Designer user interface definition files (`.ui`) are also located here. These are compiled into Python files (e.g., `mainwindow_ui.py`) using `pyuic5`.
    *   The main entry point of the application, `main.py`, resides in this directory.
    *   It includes a subdirectory `C/` which contains C boilerplate code (`ADC_boiler_plate.c`, `math_boiler_plate.c`, `uart.c`, `uart.h`) and a `Makefile` used for compiling the generated ladder logic into AVR executables.
    *   HTML files for help dialogs (e.g., `About.html`, `ArdUnoIO.html`) are also present.
    *   `toolbaricons_rc.py` (and its source, likely a `.qrc` file compiled with `pyrcc5`) suggests that toolbar icons are managed as Qt resources.

*   **`helpers/`**: This directory contains external tools and drivers necessary for the application's functionality, particularly for compiling and uploading code to Arduino boards.
    *   **`WinAVR/`**: Contains a distribution of the WinAVR toolchain, which includes `avr-gcc` (the AVR C compiler), `avrdude` (for uploading firmware), and other necessary utilities for Windows users.
    *   **`avr/`**: Seems to be a Linux-focused AVR toolchain, including `avr-gcc`, `avrdude`, etc.
    *   **`Drivers/`**: Contains USB drivers for various Arduino boards and related hardware (e.g., libusb-win32, USBtinyISP).
    *   `avrdude` (executable) and `avrdude.conf` (configuration file) are also present at the root of `helpers/`, likely for Linux/macOS usage or as a primary version.

The application follows a typical PyQt desktop application structure:
1.  UI is designed with Qt Designer (producing `.ui` files).
2.  `pyuic5` (or a script like `compile_ui_stuff.py` found in `program/`) converts `.ui` files to Python modules (e.g., `mainwindow_ui.py`, `ADC_ui.py`).
3.  `main.py` acts as the central orchestrator, initializing the main window, connecting UI signals to slots (event handlers), and managing the application's state.
4.  Other Python modules in `program/` handle specific tasks like managing the ladder grid (`managegrid.py`), converting ladder logic to an intermediate representation (`LadderToOutLine.py`), generating C code from this representation (`OutLineToC.py`), and handling UI pop-up dialogs (`popupDialogs.py`).

## 3. Main Modules and Classes

This section describes the core Python modules and their roles within the application.

### program/main.py

`main.py` is the main executable script and central hub of the Waltech Ladder Maker application. Its key responsibilities include:

*   **Application Entry Point:** Initializes the Qt Application and the main window.
*   **UI Management:**
    *   Loads the main window UI from `mainwindow_ui.py` (which is generated from `mainwindow.ui`).
    *   Connects UI elements (buttons, menu actions, etc.) to their respective handler functions (slots). This is evident in the `signalConnections` method.
    *   Manages the main graphics scene (`QGraphicsScene`) where the ladder diagram is drawn.
    *   Handles mouse events (move, click) on the graphics view for placing and interacting with ladder elements, using an event filter.
    *   Updates the element list table (`QTableWidget`) on the right side of the UI.
    *   Manages the display of mouse coordinates.
*   **Core Logic Orchestration:**
    *   Initializes and manages the main data structure for the ladder diagram (referred to as `self.grid`).
    *   Handles file operations: new, open, save, save as, using Python's `pickle` for serialization of the `grid` data.
    *   Manages undo/redo functionality by keeping copies of the `grid` state.
    *   Coordinates the process of compiling the ladder diagram:
        1.  Calls `ladderToOutLine` to convert the grid into an intermediate outline.
        2.  Calls `OutLineToC` to generate C code from this outline.
        3.  (Implicitly, `OutLineToC` or a helper likely invokes `avr-gcc` and `avrdude` from the `helpers` directory).
    *   Handles hardware selection (Waltech, Arduino Uno, Nano, Mega) and checks for I/O compatibility when switching hardware.
    *   Interfaces with `tester.py` to check USB hardware connections.
*   **Key Classes Defined/Used:**
    *   **`mainWindowUI(QMainWindow)`:** The main class that defines the application's primary window, inheriting from `QMainWindow`. It contains all the methods for UI interaction and application logic.
    *   **`elementList(elementStruct)`:** A class (likely a list wrapper or manager) to hold definitions and properties of available ladder logic elements (contacts, coils, timers, etc.). `elementStruct` seems to be a simple data structure for individual element properties.
    *   Uses classes from other modules like `ManageGrid`, `ladderToOutLine`, `OutLineToC`, and `popupDialogs`.

### program/managegrid.py

This module is responsible for managing the in-memory representation of the ladder logic diagram and its visual rendering on the `QGraphicsScene`.

*   **Role:**
    *   Handles the data structure for the ladder grid, which is a 2D list (list of lists) where each element is a `cellStruct`.
    *   Provides functions to modify this grid (add/remove rungs, widen/narrow, place/delete elements).
    *   Manages the drawing and redrawing of the entire ladder diagram on the `QGraphicsScene` in the main window. This includes drawing rung lines, OR wires, element icons, and associated text (variable names, comments, I/O assignments).

*   **Key Classes:**
    *   **`cellStruct`**: A simple class or data structure that holds all information for a single cell in the ladder grid. This includes:
        *   `midPointX`, `midPointY`: Coordinates for drawing.
        *   `MTorElement`: Type of element in the cell (e.g., "MT" for empty, "contNO", "Coil").
        *   `rungOrOR`: Indicates if the cell is part of a main "Rung" or an "OR" branch.
        *   `variableName`, `ioAssign`, `comment`, `setPoint`: Element-specific configuration.
        *   `branch`, `node`, `brchST`, `brchE`, `nodeST`, `nodeE`: Flags for parsing ladder structure (branches and nodes).
        *   `source_A`, `source_B`, `const_A`, `const_B`: For math and comparison elements.
    *   **`ManageGrid`**: The main class in this module. An instance of this class is likely held by `mainWindowUI`.
        *   **Constructor (`__init__`)**: Takes the grid data, `QGraphicsScene` instance, tool definitions, and graphics items for mouse tracking as input.

*   **Key Methods in `ManageGrid`:**
    *   **`totalRedraw()`**: Clears the `QGraphicsScene` and redraws the entire ladder diagram based on the current state of the `grid`. This involves drawing rung lines, OR branch connections, element icons, and text.
    *   **`placeIcon(cellNum, toolNum)`**: Places the visual icon for a ladder element onto the scene at the specified cell.
    *   **`placeText(cellNum)`**: Renders text (variable name, comments, I/O assignment, setpoints) associated with an element in a cell.
    *   **`Delete(cellNum)`**: Removes an element from a cell or deletes an entire empty rung. If an element is deleted, its properties in the `cellStruct` are reset.
    *   **`insertRung(row)`**: Inserts a new empty rung (a list of `cellStruct`s) into the grid at the specified row.
    *   **`insertBlankOR(cellNum)`**: Converts a rung or adds a new row for an OR branch.
    *   **`addWire(cellNum)`**: Adds or removes a vertical OR wire connection between rungs/branches.
    *   **`Widen(cellNum)`**: Increases the width of the ladder diagram by adding an empty column of cells.
    *   **`Shrink(cellNum)`**: Decreases the width of the ladder diagram if empty columns exist.
    *   **`placeElememt(cellNum, tempCellData, toolToPlace)`**: Updates a `cellStruct` in the grid with new element data (typically after a popup dialog is confirmed).
    *   `findBranchesAndNodes()`, `findStartsAndEnds()`: Helper methods to analyze the grid and mark cells for branch/node processing, likely used by `LadderToOutLine.py`.
    *   `checkOrphanName(cellNum)`: Checks if changing an element's name would leave other elements that reference it orphaned.
    *   `changeRectangle()`: Adjusts the `sceneRect` of the `QGraphicsScene` to fit the current grid dimensions.

### program/LadderToOutLine.py

This module is responsible for converting the 2D grid representation of the ladder diagram (managed by `managegrid.py`) into a more structured, linear "outline." This outline is an intermediate representation that is easier to parse for C code generation.

*   **Role:**
    *   Traverses the ladder logic grid, interpreting rungs, OR branches, series connections, and parallel connections.
    *   Generates a list of strings or structured data representing the logical flow of the ladder program.

*   **Key Classes:**
    *   **`ladderToOutLine`**: The main class in this module.
        *   **Constructor (`__init__`)**: Takes the ladder `grid` data as input.

*   **Key Methods in `ladderToOutLine`:**
    *   **`makeOutLine()`**: This is the primary public method. It orchestrates the conversion process and returns the generated outline (likely a list of lists or list of strings).
        *   It iterates through rungs and identifies branches and nodes using information pre-calculated by `ManageGrid.findStartsAndEnds()`.
        *   It handles special cases like "state users" (timers, counters, edge detectors that use the rung state) and outputs on OR branches by creating "fake" or temporary rungs for processing.
    *   **`processRung(i, branchList, outLine, nodeList, rightTurnList, position)`**: Processes a single rung or a segment of a rung/branch.
        *   `i`: current row index.
        *   `branchList`: keeps track of active branches.
        *   `outLine`: the list being built with the outline.
        *   `nodeList`: keeps track of nodes and their constituent branches.
        *   `rightTurnList`: handles complex paths where logic flows "up and then left" from an output on a lower branch.
        *   `position`: current column index being processed, or a limit for partial processing (e.g., for state users).
    *   **`loadRightTurns(i, j, hitRung)`**: Identifies paths that involve "right turns" in OR branches (where an element on a lower branch affects the logic flow of an upper branch to its left).
    *   **`branchStart(i, j, branchList, outLine, rightTurnList)`**: Detects the start of a new parallel branch and adds a "startBR" marker to the outline.
    *   **`nodeStart(i, j, nodeList, outLine, branchList, rightTurnList)`**: Detects the start of a node (where parallel branches converge) and calls `processNode`.
    *   **`processNode(i, j, outLine, branchList, nodeList, rightTurnList)`**: Handles the logic for a node, processing its parallel branches recursively or iteratively.
    *   **`addElementToOutline(i, j, outLine)`**: Adds the representation of a specific ladder element (contact, timer, counter, comparison) to the `outLine`. The format includes the element type, name, and any relevant parameters (e.g., I/O assignment, setpoint).
    *   Helper methods like `ORhere(i,j)`, `blankRow(i)`, `isOutOnOR(i,j)`, `MTorLeft(i,j)`, `rightTurnListCheck`, `straybranchSTcheck`, `rungStateUser` are used to query the grid and manage the parsing logic.

The output `outLine` is a list where each item can be a comment, a representation of an element (e.g., `['cont_MyInput_NO', 'contNO', 'in_1']`), a branch marker (e.g., `['startBR', [row, col]]`), or a node marker (e.g., `['node_', [node_row, node_col], [branch1_row, branch1_col], ...]`). This structured outline is then passed to `OutLineToC.py`.

### program/OutLineToC.py

This module takes the structured "outline" generated by `LadderToOutLine.py` and translates it into C code suitable for compilation and execution on AVR microcontrollers (like those found in Arduinos).

*   **Role:**
    *   Generates variable declarations for inputs, outputs, timers, counters, and internal logic states.
    *   Translates ladder logic elements (contacts, coils, timers, math operations, etc.) from the outline into C conditional statements (`if`, `else`), assignments, and function calls.
    *   Includes boilerplate C code such as necessary headers (`avr/io.h`, `avr/interrupt.h`), Interrupt Service Routines (ISRs) for timers (and ADC if applicable), and the main program loop structure (`int main()`, `while(1)`).
    *   Manages hardware-specific details, such as pin mappings for different Arduino boards or the Waltech proprietary board.
    *   Invokes `hexmaker.py` (via the `hexMaker` class) to compile the generated C code using `avr-gcc` and then upload the resulting `.hex` file using `avrdude`.

*   **Key Classes:**
    *   **`OutLineToC`**: The main class in this module.
        *   **Constructor (`__init__`)**: Takes the ladder `grid` (though primarily uses the `outLine`) and `currentHW` (current hardware selection string) as input. It initializes hardware-specific lists for inputs (`inPutList`), outputs (`outPutList`), ADC pins (`ADCList`), and PWM pins (`PWMList`).

*   **Key Methods in `OutLineToC`:**
    *   **`makeC(outLine, displayOutputPlace)`**: The primary public method that generates the C code.
        *   `outLine`: The structured outline from `LadderToOutLine.py`.
        *   `displayOutputPlace`: The `QTextBrowser` widget from the UI for displaying compilation messages.
        *   It starts by adding C headers, ISR for `TIMER0_OVF_vect` (used for timing scans and software timers/counters), and potentially an ADC ISR.
        *   Includes a C function `do_math` for arithmetic operations and `read_adc` if the hardware supports ADC.
        *   Generates `DDR` (Data Direction Register) setup for outputs and `PORT` setup for input pull-ups in `main()`.
        *   Calls `initVarsForMicro` to declare C variables based on elements found in the `outLine`.
        *   Iterates through the `outLine`, translating each type of entry:
            *   Rung start/end comments.
            *   `branch` and `startBR`: Translated into C variables representing branch states.
            *   `cont_`, `Timer_`, `Counter_`, `Fall_`, `Equals_`, etc. (elements): Translated into `if` conditions that modify the state of the current rung (`W`) or branch variable.
            *   `node_`: Combines the states of multiple branches using logical OR (`||`) or AND (`&&`) operations.
            *   `rungstate_Counter`, `rungstate_Timer`, `rungstate_Fall`: Handle the logic for counters, timers, and edge detection based on the overall rung state.
            *   `output_`: Assigns the final rung state `W` to the output variable.
            *   `Result_`: Calls the `do_math` C function.
            *   `PWM_`: Sets up PWM registers if `W` is true.
            *   `ADC_`: Calls the `read_adc` C function if `W` is true.
        *   Calls `findInPuts` (or `findInPutsArd`) to generate C code for reading hardware inputs into their respective variables.
        *   Calls `findOutPuts` to generate C code for writing output variables to hardware pins.
        *   Finally, it instantiates `hexMaker` and calls its `saveCfileAndCompile` method.
    *   **`initVarsForMicro(outLine, C_txt)`**: Scans the `outLine` and generates C variable declarations (e.g., `uint8_t cont_MyInput_NO = 0;`, `uint16_t reg_Timer_MyTimer = 0;`).
    *   **`DDROutPuts(C_txt)` / `pullupInPuts(C_txt)`**: Generate DDR and PORT register configurations for outputs and input pull-ups.
    *   **`setUpPWMs(outLine, C_txt)`**: Generates C code to configure PWM timers and pins based on PWM elements in the outline.
    *   Various `add<ElementName>` methods (e.g., `addCounter`, `addTimer`, `addEquals`, `addMath`, `addPWM`, `addADC`): These methods contain the specific logic to translate individual outline element types into C code snippets.
    *   `outputAndName(outline, thisLine, pos)`: A helper to correctly reference variables that might be outputs of other functions (like math or ADC results) or direct hardware I/O.

The module effectively acts as a simple compiler, translating the intermediate representation of the ladder logic into executable C code for the target microcontroller.

### program/popupDialogs.py

This module defines the various Qt Dialog classes used throughout the Waltech Ladder Maker application for configuring ladder logic elements when they are added to or edited on the grid.

*   **Role:**
    *   Provides specialized dialog windows for each type of ladder logic element (Coil, Contact, Timer, Counter, Math, Comparison, PWM, ADC).
    *   Allows users to input parameters such as variable names, I/O assignments, setpoints, comments, and sources for operations.
    *   Populates dialog widgets (like `QComboBox`, `QLineEdit`, `QSpinBox`) with relevant existing data from the grid (e.g., existing variable names, current I/O assignments) or hardware-specific I/O lists.

*   **Key Classes:**
    *   Each dialog typically inherits from `QtWidgets.QDialog` and uses a UI definition class generated by `pyuic5` (e.g., `Ui_CoilDialog` from `coil_ui.py`).
    *   **`CoilDialog(QtWidgets.QDialog)`**: For configuring Coils (variable name, I/O assignment, comment).
    *   **`ContDialog(QtWidgets.QDialog)`**: For configuring Contacts (Normally Open/Normally Closed) (variable name, I/O assignment, comment).
    *   **`EdgeDialog(QtWidgets.QDialog)`**: For configuring Edge detection elements (Falling Edge) (comment).
    *   **`TimerDialog(QtWidgets.QDialog)`**: For configuring Timers (variable name, setpoint as time delay, comment).
    *   **`CounterDialog(QtWidgets.QDialog)`**: For configuring Counters (variable name, setpoint as counts, comment).
    *   **`CompairDialog(QtWidgets.QDialog)`**: For configuring Comparison operators (Equals, Greater Than, Less Than, etc.) (sources A/B which can be constants or variable names). The specific operator (e.g., '=', '>') is often passed to the constructor to customize the label.
    *   **`MathDialog(QtWidgets.QDialog)`**: For configuring Mathematical operations (Plus, Minus, Multiply, Divide, Move) (result variable name, sources A/B which can be constants or variable names). The specific operation is passed to the constructor.
    *   **`PWMDialog(QtWidgets.QDialog)`**: For configuring PWM outputs (hardware PWM pin, duty cycle/value as setpoint).
    *   **`ADCDialog(QtWidgets.QDialog)`**: For configuring ADC inputs (result variable name, hardware ADC pin).
    *   **Informational Dialogs**:
        *   `USBHelpDialog`, `ArduinoUnoIOHelpDialog`, `ArduinoNanoIOHelpDialog`, `ArduinoMegaIOHelpDialog`, `AboutHelpDialog`: These display static HTML content in a `QTextBrowser`.
        *   `ardIODialog`: A warning dialog for I/O compatibility issues when changing hardware.
        *   `wrongVersionDialog`: A dialog shown if an attempt is made to open a file from an incompatible older version.
        *   `ThreeParallelsDialog`: A warning dialog if the user attempts to create more than two parallel branches in a node (which the C code generation might not support).

    *   **`cellSearch`**: This is a crucial helper class instantiated by many of the dialogs.
        *   **Constructor (`__init__`)**: Takes the current `grid`, `cellNum` (coordinates of the element being configured), and `currentHW` as input.
        *   **Methods:**
            *   `makeSharedNameList(elType)` / `makeSourceNameList(thisThing, elType)`: Scans the grid to find existing variable names that can be reused or linked. It suggests a new unique name if needed (e.g., "Name_1", "Name_2").
            *   `makeNamelistCoil(combobox)`, `makeNamelistCont(combobox)`, `makeNamelistComp(combobox, thisThing, elType)`: Populate `QComboBox` widgets with lists of available variable names.
            *   `makeIOlist(combobox, inpt)`: Populates a `QComboBox` with available I/O pins based on the `currentHW` and whether it's for an input, output, PWM, or ADC. It also filters out already used pins.
            *   `fillComment(lineEdit)`, `fillSpinBox(spinBox)`, `fillSpinBoxTimer(spinBox)`: Pre-fill dialog widgets with the existing configuration of an element when it's being edited.

When a dialog is accepted (e.g., user clicks "OK"), `main.py` retrieves the entered data from the dialog's UI elements and updates the corresponding `cellStruct` in the ladder grid.

### program/mainwindow_ui.py

This file (`program/mainwindow_ui.py`) is a Python module generated by `pyuic5` (or a similar Qt UI compiler tool) from the `mainwindow.ui` file (created with Qt Designer).

*   **Role:** It contains the code that sets up the layout and widgets of the main application window. Essentially, it translates the visual design from Qt Designer into Python code.
*   **Structure:** It typically defines a class, in this case, `Ui_MainWindow`, which has a method `setupUi(self, MainWindow)`. This method creates and arranges all the UI elements (buttons, menus, toolbars, graphics view, labels, etc.) as designed in Qt Designer.
*   **Manual Editing:** **This file should NOT be manually edited.** Any changes should be made in Qt Designer (`mainwindow.ui`), and then `mainwindow_ui.py` should be regenerated. Manual edits will be overwritten the next time the UI file is compiled. The main application logic, including event handling for these UI elements, is implemented in `program/main.py` (specifically within the `mainWindowUI` class which uses `Ui_MainWindow`).

### program/tester.py

This module provides functionality to test the USB connection to the selected hardware (Waltech or Arduino boards) and verify that `avrdude` can communicate with it.

*   **Role:**
    *   Helps users diagnose connection problems before attempting to compile and upload a ladder program.
    *   Executes `avrdude` with commands to read device signatures or fuses, which indicates successful communication if the command succeeds.
    *   Provides feedback to the user in the main window's output console.

*   **Key Classes:**
    *   **`tester`**: The main class in this module.
        *   **Constructor (`__init__`)**: Takes `opSys` (operating system: "WIN", "NIX", "MAC") and `currentHW` (hardware type string) as input.

*   **Key Methods in `tester`:**
    *   **`test1(displayOutputPlace)`**: The primary public method that initiates the hardware test.
        *   `displayOutputPlace`: The `QTextBrowser` widget from the UI for displaying test messages.
        *   Sets the cursor to `Qt.WaitCursor`.
        *   Changes the current directory to `helpers/hexes` (though `avrdude` and its config are usually in `helpers/` or `helpers/WinAVR/bin/`).
        *   Calls a hardware-and-OS-specific test method (e.g., `testWaltechWIN`, `testArduinoUnoNIX`).
        *   Restores the cursor and changes the directory back.
        *   Returns the `avrdude` command string that was tested (or would be used for upload), though this return value might not be directly used by the caller in `main.py` for the test operation itself.

    *   **Hardware/OS Specific Test Methods** (e.g., `testWaltechWIN`, `testArduinoUnoNIX`, `testArduinoMegaMAC`):
        *   These methods construct the appropriate `avrdude` command line.
        *   **For Waltech (usbtiny programmer):**
            *   Command: `avrdude -p m32 -P usb -c usbtiny -B5 -U lfuse:r:-:h -U hfuse:r:-:h` (or similar, paths adjusted for OS).
            *   Checks for device signature (`0x1e9502` for ATmega32) and fuse values. It might attempt to set fuses if they are incorrect.
        *   **For Arduino (Uno - m328p, Mega - m2560; various programmers like 'arduino', 'wiring', 'stk500v1', 'stk500v2'):**
            *   **Windows:** Tries COM ports 1 through 9. Uses `subprocess.Popen` with a timeout mechanism as `avrdude` might hang if the port is wrong.
            *   **Linux:**
                *   Uses `lsusb` to check if an Arduino-like device is listed.
                *   Uses `dmesg` to find potential serial port names (e.g., `ttyACM0`, `ttyUSB0`).
                *   Attempts `avrdude` on likely ports.
            *   **macOS:**
                *   Uses `system_profiler SPUSBDataType` to check for Arduino USB devices.
                *   Scans `/dev/tty.*` and `/dev/cu.*` for potential serial ports and tries `avrdude`.
        *   They use `subprocess.Popen` to execute the `avrdude` command and capture its output and error streams.
        *   Parse the output/error from `avrdude` to determine success or failure (e.g., looking for "AVR device initialized", "Device signature", or error messages like "Could not find USBtiny device", "timeout", "Operation not permitted").
        *   Display formatted messages (using `boldLine`) in the `displayOutputPlace` widget.

    *   **`boldLine(displayOutputPlace, txt)`**: A helper method to display text in bold in the output console.

The module relies on the `avrdude` executable and its configuration file (`avrdude.conf`) being present in the `helpers` directory (or `helpers/WinAVR/bin` for Windows). The specific `avrdude` parameters (programmer type `-c`, baud rate `-b`, part name `-p`) are hardcoded based on the selected hardware.

### Other UI Files (*_ui.py)

Similar to `mainwindow_ui.py`, the `program/` directory contains numerous other files ending with `_ui.py`. These are also Python modules generated by `pyuic5` from corresponding `.ui` files (designed in Qt Designer).

*   **Role:** Each of these files defines the UI structure for a specific dialog box or custom widget used within the application. For example, when you add a "Coil" to the ladder, a dialog pops up to configure its properties; the layout of this dialog is defined in a `coil.ui` file and its generated Python counterpart `coil_ui.py`.
*   **Manual Editing:** Like `mainwindow_ui.py`, **these `*_ui.py` files should not be manually edited.** Changes should be made in the respective `.ui` file using Qt Designer, and the Python file should be regenerated. The logic for these dialogs (e.g., how data is retrieved from them, how they are displayed) is typically handled in `program/popupDialogs.py` or directly within `program/main.py` when the dialogs are invoked.

Examples of such UI files found in `program/` include:
*   `ADC_ui.py` (from `ADC.ui`)
*   `coil_ui.py` (from `coil.ui`)
*   `compair_ui.py` (from `compair.ui`)
*   `cont_ui.py` (from `cont.ui`)
*   `counter_ui.py` (from `counter.ui`)
*   `edge_ui.py` (from `edge.ui`)
*   `IOHelp_ui.py` (from `IOHelp.ui`)
*   `math_ui.py` (from `math.ui`)
*   `PWM_ui.py` (from `PWM.ui`)
*   `timer_ui.py` (from `timer.ui`)
*   `USBHelp_ui.py` (from `USBHelp.ui`)
*   `ardIOnote_ui.py` (from `ardIOnote.ui`)
*   `wrongVersion_ui.py` (from `wrongVersion.ui`)

## 4. Adding New Ladder Logic Elements

This section outlines the general steps required to add a new functional ladder logic element to the Waltech Ladder Maker. It integrates information from `program/Adding_Elements.txt` and relevant source code files.

1.  **Creating Icons:**
    *   **Format & Size:** You'll typically need two icons in SVG format.
        *   One for the toolbar button (e.g., `contact_NO_button.svg`). `Adding_Elements.txt` mentions sizes like 36x27 pixels, but it's best to match existing button icon dimensions.
        *   One for rendering on the ladder diagram itself (e.g., `contact_NO.svg`). `Adding_Elements.txt` suggests 58x60 pixels. The diagram icon usually has a transparent background except for the core symbol, while the button might have a white background.
    *   **Storage:** Icons are managed as Qt Resources. Add your SVG files to the `program/icons/` directory (create it if it doesn't exist, though `toolbaricons_rc.py` implies icons are in `program/icons/` or a similar path defined in `toolbaricons.qrc`).
    *   **Resource Compilation:** Update the Qt Resource Collection file (`.qrc`, likely `program/toolbaricons.qrc`). Then, recompile it into `program/toolbaricons_rc.py` using `pyrcc5 resource.qrc -o resource_rc.py`. This makes the icons accessible via paths like `:/icons/icons/my_new_icon.svg`.

2.  **Updating the UI (Qt Designer & Compilation):**
    *   Open `program/mainwindow.ui` in Qt Designer.
    *   **Create QAction:** Add a new `QAction` for your element (e.g., `actionMyNewElement`).
        *   Set its `objectName`.
        *   Assign the **toolbar button icon** you created to this action (e.g., `icon=":/icons/icons/my_new_icon_button.svg"`).
        *   Set a tooltip and "What's This?" text for help.
    *   **Add to Toolbar:** Drag the new `QAction` onto the "Elements" toolbar (`toolBar` object in Qt Designer).
    *   **Regenerate UI Code:** After saving the `.ui` file, regenerate `program/mainwindow_ui.py` by running `pyuic5 program/mainwindow.ui -o program/mainwindow_ui.py` or by using the `program/compile_ui_stuff.py` script if it handles this.

3.  **Defining the Element in `program/main.py`:**
    *   Locate the `elementList` class definition.
    *   In its constructor (`__init__`), append a new `elementStruct` instance to `self.toolList`:
        ```python
        self.toolList.append(elementStruct(
            "MyNewElement",                       # toolName: Unique string identifier
            QtGui.QPixmap(":/icons/icons/my_new_icon_diagram.svg"),  # pixmap: For drawing on the grid
            "any",                                # position: "any" or "right"
            "Element"                             # toolType: Usually "Element"
        ))
        ```
        *   `toolName`: Must match the string you'll use in signal connections and `runPopup`.
        *   `pixmap`: The `QPixmap` created from your **diagram icon** SVG.
        *   `position`:
            *   `"any"`: Element can be placed in most free cells not at the far right.
            *   `"right"`: Element will always be placed in the rightmost column (like coils).
        *   `toolType`: Typically `"Element"` for functional blocks. Other types are `"Rung"` or `"OR"` for structural tools.

4.  **Connecting Signals in `program/main.py`:**
    *   Inside the `mainWindowUI.signalConnections(self)` method:
        *   **Connect Action to Handler:** Connect the `triggered` signal of your new QAction to the `self.anyButton` method. Use a lambda to pass your `toolName`:
            ```python
            self.ui.actionMyNewElement.triggered.connect(lambda who="MyNewElement": self.anyButton(who))
            ```
        *   **Add to Action Group:** Add your new QAction to `toolActionGroup` to make its selection exclusive with other element tools:
            ```python
            toolActionGroup.addAction(self.ui.actionMyNewElement)
            ```
        *   The `anyButton(self, who)` method in `mainWindowUI` sets `self.currentTool = who`, making the application aware of the selected element tool.

5.  **Handling Pop-up Configuration Dialog (if your element needs configuration):**
    *   **In `program/main.py` - `mainWindowUI.runPopup(self, tool, cellNum)` method:**
        *   Add an `elif` block for your new element:
            ```python
            elif tool == "MyNewElement":
                self.dialog = popupDialogs.MyNewElementDialog(self.grid, cellNum, self.currentHW)
                popUpOKed = self.dialog.exec_()
                # popUpOKed will be True if the user clicks OK, False otherwise
            ```
        *   If `popUpOKed` is `True`, retrieve the configured data from `self.dialog.ui` properties and store them in the `tempCellInfo` (an instance of `managegrid.cellStruct`). `main.py` already has generic code to populate `tempCellInfo.variableName`, `tempCellInfo.ioAssign`, `tempCellInfo.comment`, `tempCellInfo.setPoint`, etc., based on common dialog widget names. Ensure your custom dialog's widgets follow this naming convention (e.g., `comboBox` for I/O, `comboBox_2` for variable name, `lineEdit` for comment, `spinBox` or `doubleSpinBox` for setpoint) or add specific logic to retrieve values.
            ```python
            if popUpOKed == True:
                # ... (standard data retrieval from self.dialog.ui) ...
                # Example for a custom field:
                # try: tempCellInfo.myCustomParameter = self.dialog.ui.myCustomSpinBox.value()
                # except: pass
                tempCellInfo.MTorElement = tool # Set the element type
                return tempCellInfo
            else:
                return False # User cancelled
            ```

    *   **In `program/popupDialogs.py`:**
        *   Create a new dialog class (e.g., `MyNewElementDialog(QtWidgets.QDialog)`).
        *   Design its UI: Create a `mynewelement.ui` file with Qt Designer. Add `QLineEdit` for text, `QComboBox` for choices, `QSpinBox` for numbers, etc.
        *   Compile `mynewelement.ui` to `mynewelement_ui.py` using `pyuic5` and import it (e.g., `from mynewelement_ui import Ui_MyNewElementDialog`).
        *   In the `__init__` of your dialog class:
            ```python
            from mynewelement_ui import Ui_MyNewElementDialog # Or your actual UI class name

            class MyNewElementDialog(QtWidgets.QDialog):
                def __init__(self, grid, cellNum, currentHW, parent=None):
                    super().__init__(parent)
                    self.ui = Ui_MyNewElementDialog()
                    self.ui.setupUi(self)
                    # Use cellSearch to pre-fill common fields if needed:
                    # helper = cellSearch(grid, cellNum, currentHW)
                    # helper.makeNamelistCoil(self.ui.comboBox_2) # For variable name
                    # helper.makeIOlist(self.ui.comboBox, True) # For input I/O list
                    # helper.fillComment(self.ui.lineEdit)
                    # helper.fillSpinBox(self.ui.spinBox) # For a setpoint
                    # Pre-fill custom fields if editing an existing element:
                    # if grid[cellNum[0]][cellNum[1]].myCustomParameter is not None:
                    #    self.ui.myCustomSpinBox.setValue(grid[cellNum[0]][cellNum[1]].myCustomParameter)
            ```

6.  **Grid Placement and Rendering Logic:**
    *   **Placement (`program/main.py` - `mainWindowUI.leftClick`):**
        *   The general logic for placing elements based on `toolType == "Element"` and `position == "any"` or `"right"` is already in `leftClick`. If your element fits these, no changes might be needed here.
        *   If it has very unique placement rules, you might need to add a specific `elif self.Tools.toolList[toolToPlace[1]].toolName == "MyNewElement":` block within `leftClick` to implement custom placement logic.
    *   **Data Storage (`program/managegrid.py` - `ManageGrid.placeElememt`):**
        *   This method takes the `tempCellInfo` (populated from the dialog) and updates the `self.grid` at the given `cellNum`. Ensure all custom parameters from your dialog are correctly saved into the `cellStruct` here if not handled generically in `main.py`.
    *   **Rendering (`program/managegrid.py` - `ManageGrid.placeIcon` and `ManageGrid.placeText`):**
        *   `placeIcon` uses the `pixmap` defined in `elementStruct` to draw the icon on the grid.
        *   `placeText` draws common properties like `variableName`, `comment`, `setPoint`, `ioAssign`, and math sources (`source_A`, `source_B`, `const_A`, `const_B`). If your element has other unique text to display directly on the grid, you'll need to modify `placeText` to handle your new `MTorElement` type and render its specific properties.

7.  **Logic for Code Generation:**
    This is crucial for making your element functional.
    *   **`program/LadderToOutLine.py` - `ladderToOutLine.addElementToOutline(self, i, j, outLine)`:**
        *   Add an `if` or `elif` condition for your element's `toolName`:
            ```python
            if self.grid[i][j].MTorElement == "MyNewElement" and j < width - 1:
                outLine.append([
                    "MyNewElement_" + str(self.grid[i][j].variableName), # Unique ID for this instance
                    str(self.grid[i][j].MTorElement),      # Type
                    str(self.grid[i][j].ioAssign),         # Example: I/O assignment
                    str(self.grid[i][j].setPoint),         # Example: Setpoint
                    str(self.grid[i][j].myCustomParameter) # Example: Custom data
                ])
            ```
            Adapt the appended list to include all necessary parameters from the `cellStruct` that the C code generator will need.

    *   **`program/OutLineToC.py` - `OutLineToC` class:**
        *   **`initVarsForMicro(self, outLine, C_txt)`:**
            If your element requires C variables (e.g., to store its state, setpoints), add logic to declare them. Ensure uniqueness if multiple instances can exist.
            ```python
            # Example for MyNewElement
            if str(outLine[i][0])[:len("MyNewElement_")] == "MyNewElement_":
                # Assuming outLine[i][0] is "MyNewElement_VariableName"
                var_name = str(outLine[i][0])
                if "    uint8_t " + var_name + "_state = 0;\n" not in C_txt:
                    C_txt += "    uint8_t " + var_name + "_state = 0;\n"
                # Add declarations for setpoints or other parameters if needed
                # if "    uint16_t setpoint_" + var_name + " = " + str(outLine[i][3]) + ";\n" not in C_txt:
                #    C_txt += "    uint16_t setpoint_" + var_name + " = " + str(outLine[i][3]) + ";\n"
            ```
        *   **Main loop in `makeC(self, outLine, displayOutputPlace)`:**
            Add a block to handle your element's entry from the `outLine`:
            ```python
            if str(outLine[i][0])[:len("MyNewElement_")] == "MyNewElement_":
                # varNameStr will be like "MyNewElement_VariableName"
                varNameStr = str(outLine[i][0])
                # io_assign = str(outLine[i][2])
                # set_point = str(outLine[i][3])
                # custom_param = str(outLine[i][4])

                # C code logic:
                # Apply to W (rung state) or current branch state
                c_code_snippet = f"             if (rung_condition_for_{varNameStr}) {{ W = 0; }}\n"
                # Or if it's a latching/stateful element:
                # c_code_snippet = f"             if ({varNameStr}_state == 0) {{ W = 0; }}\n"

                # If it's an element that affects rung state directly:
                if currentBranchList[-1] is None: # Affecting main rung state W
                    C_txt += f"             if (!({varNameStr}_state)) {{ W = 0; }}\n"
                else: # Affecting a branch state
                    branch_var = f"branch_{currentBranchList[-1][0]}_{currentBranchList[-1][1]}"
                    C_txt += f"             if (!({varNameStr}_state)) {{ {branch_var} = 0; }}\n"

                # If it's an output-like element (e.g., a special coil or function block):
                # C_txt += f"            if (W == 1) {{ {varNameStr}_activate_function({set_point}); }}\n"

                C_txt += c_code_snippet # Add your generated C code
            ```
            This is highly dependent on what your element does (is it a contact-like, coil-like, function block?). You need to generate C code that reflects its behavior based on the input rung state (`W` or a branch variable) and its configured parameters.
        *   **Hardware Interaction:** If your element needs specific I/O pins not covered by existing `inPutList`, `outPutList`, `ADCList`, `PWMList` in `OutLineToC.__init__`, you might need to extend these or add new lists and corresponding C code generation for DDR/PORT setup and read/write operations.

This process is complex and requires careful integration with multiple parts of the existing codebase. Start with simple elements and test thoroughly at each step.

## 5. Building and Debugging

This section provides information on setting up the development environment, running the application, and common debugging practices.

*   **Prerequisites:**
    *   **Python:** Version 2.7 (implied by `print` statements without parentheses and `pyuic4`/`pyrcc4` usage in `compile_ui_stuff.py`).
    *   **PyQt4:** The application uses PyQt4. If not installed, you would typically install it using your system's package manager (e.g., `apt-get install python-qt4` on Debian/Ubuntu) or from source. `pip install PyQt4` might work in some environments but can be tricky.
    *   **AVR Toolchain (for C code compilation):**
        *   For compiling and uploading to Arduino/AVR targets, `avr-gcc` and `avrdude` are required.
        *   The `helpers/` directory bundles `WinAVR` (which includes these tools for Windows) and versions of `avrdude` for Linux/macOS. If these bundled versions don't work, or for development on Linux/macOS, a system-wide installation of `avr-gcc` and `avrdude` might be necessary (e.g., via `apt-get install gcc-avr avrdude`).

*   **Running the Application:**
    *   Navigate to the root directory of the project.
    *   Execute: `python program/main.py`

*   **UI Files (`.ui`):**
    *   The user interface files (e.g., `program/mainwindow.ui`, `program/coil.ui`) are created and edited using Qt Designer (version compatible with Qt4).
    *   If a `.ui` file is modified, its corresponding Python module (`_ui.py`) must be regenerated.
    *   The `program/compile_ui_stuff.py` script automates this process for all known `.ui` files using `pyuic4`. To run it: `python program/compile_ui_stuff.py` (ensure it's executable and paths are correct if running from a different directory).
    *   Alternatively, you can compile a single `.ui` file manually, for example:
        `pyuic4 program/mainwindow.ui -o program/mainwindow_ui.py`

*   **Resource Files (`.qrc`):**
    *   Icon resources are defined in a Qt Resource Collection file, which appears to be `program/toolbaricons.qrc` based on `compile_ui_stuff.py`.
    *   This `.qrc` file lists the SVG icons used in the UI.
    *   After modifying the `.qrc` file (e.g., adding new icons), the Python resource module (`program/toolbaricons_rc.py`) must be regenerated using `pyrcc4`.
    *   The `program/compile_ui_stuff.py` script also handles this:
        `pyrcc4 program/toolbaricons.qrc -o program/toolbaricons_rc.py`
        (Adjust path to `toolbaricons.qrc` if it resides elsewhere, e.g., `program/icons/toolbaricons.qrc`).

*   **Debugging:**
    *   **Python Debugging:** Use standard Python techniques such as `print` statements for tracing or the Python debugger (`pdb`).
        ```python
        import pdb; pdb.set_trace()
        ```
    *   **UI Issues:** For layout or widget problems, open the corresponding `.ui` file in Qt Designer to inspect properties and hierarchy.
    *   **Compilation/Upload Issues:**
        *   The application's **Output Console** (a `QTextBrowser` widget in the UI) displays messages from `avr-gcc` (C compiler) and `avrdude` (uploader). Check this for errors.
        *   The generated C code is saved to `program/C/main.c`. This file can be inspected to debug issues in the C code generation logic.
        *   You can manually run the `avr-gcc` and `avrdude` commands (as constructed in `OutLineToC.py` and `tester.py`) in a terminal for more direct feedback.
    *   **Hardware Testing:** Use the **Hardware > Test USB** menu option to check basic communication with the selected board using `avrdude`.

*   **Bundled Tools:**
    *   The `helpers/` directory is crucial. It contains:
        *   `WinAVR/`: A version of the AVR toolchain for Windows, including `avr-gcc` and `avrdude`.
        *   `avrdude` and `avrdude.conf`: Versions likely intended for Linux/macOS.
    *   On Windows, the application might work "out of the box" if `WinAVR` is correctly bundled and its path is accessible. On Linux/macOS, if the bundled `avrdude` has issues or `avr-gcc` is missing, developers might need to install these tools system-wide.

## 6. Coding Conventions and Style Guidelines

While the project predates strict adherence to modern Python standards in some areas (e.g., Python 2.7, PyQt4), strive for clarity and consistency.

*   **General Python:**
    *   Follow **PEP 8** (Style Guide for Python Code) where reasonable. Use a linter like Flake8 to catch common issues.
    *   Indent with 4 spaces.
*   **Naming Conventions:**
    *   **Classes:** `PascalCase` (e.g., `mainWindowUI`, `elementStruct`, `ManageGrid`).
    *   **Methods and Functions:** Predominantly `camelCase` (e.g., `signalConnections`, `newFile`, `makeOutLine`, `totalRedraw`). New code should probably follow this existing style for consistency within a module.
    *   **Variables:** `camelCase` (e.g., `currentHW`, `toolToPlace`) or `snake_case` for local variables if it enhances readability. Be consistent within a function/method.
    *   **UI Elements:** When referring to UI elements loaded from `_ui.py` files, use the names defined in Qt Designer (e.g., `self.ui.actionContNO`, `self.ui.tableWidget`).
*   **Comments:**
    *   Use docstrings for modules, classes, and methods/functions to explain their purpose, arguments, and return values. The existing codebase has inline comments (e.g., `##001##` markers, `#comments`) which can be useful but should be supplemented with proper docstrings for new code.
    *   Use inline comments (`#`) to explain complex or non-obvious sections of code.
*   **UI Code (`_ui.py` files):**
    *   These files (e.g., `mainwindow_ui.py`, `coil_ui.py`) are generated by `pyuic4` from `.ui` files. **Do NOT edit them manually**, as changes will be overwritten. Modify the `.ui` file in Qt Designer and recompile.
*   **Resource Code (`_rc.py` files):**
    *   Files like `toolbaricons_rc.py` are generated by `pyrcc4`. Do not edit manually.
*   **Imports:**
    *   Group imports:
        1.  Standard library imports (e.g., `sys`, `os`, `re`, `copy`).
        2.  Third-party library imports (e.g., `from PyQt5 import QtCore, QtGui, QtWidgets` - **Note: This should be `from PyQt4`** based on `compile_ui_stuff.py`. This guide needs consistent correction if the project is indeed PyQt4).
        3.  Application-specific imports (e.g., `from managegrid import ManageGrid`, `import popupDialogs`).
    *   Avoid `from module import *`. Import specific classes/functions or the module itself.
*   **Error Handling:**
    *   The application has some basic error handling (e.g., pop-up dialogs for invalid operations).
    *   For new code, use `try-except` blocks for operations that can fail, such as file I/O, subprocess calls, or potentially problematic calculations. Provide informative error messages to the user or log them.
*   **PyQt4 Usage:**
    *   Follow best practices for PyQt4 (e.g., proper signal/slot connections, layout management, dialog usage).
    *   Ensure correct parent-child relationships for QObjects to manage memory and object lifetimes.
    *   Use `QApplication.processEvents()` sparingly and only when necessary to keep the UI responsive during long operations (though ideally, long operations should be moved to separate threads).
*   **String Formatting:**
    *   The code uses older string formatting like `"string %s %d" % (var1, var2)`. For new code, consider using f-strings (if Python version were 3.6+) or `.format()` for better readability, but consistency with existing module style might be preferred. Given Python 2.7, stick to `%` formatting or `.format()`.
*   **File Paths:**
    *   Use `os.path.join()` for constructing file paths to ensure cross-platform compatibility, though existing code often uses hardcoded slashes.

By following these guidelines, new contributions can maintain or improve the codebase's consistency and readability.
