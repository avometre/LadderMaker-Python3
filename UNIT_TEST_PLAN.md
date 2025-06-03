# Waltech Ladder Maker - Unit Test Plan

This document outlines a plan for unit tests that would be beneficial for ensuring the robustness and correctness of the Waltech Ladder Maker's core logic. Implementation of these tests would typically require a local development environment with a Python unit testing framework (e.g., `unittest` module).

## I. Unit Tests for `LadderToOutLine.py`

**Module Purpose:** Converts the `grid` data structure (representing the visual ladder diagram) into a structured textual `outLine`.

**Testing Goal:** Ensure various ladder logic constructs are correctly translated into their intermediate textual representation.

**Key Class:** `ladderToOutLine`
**Key Method:** `makeOutLine()`

**Test Structure:**
For each test case:
1.  Programmatically create a `grid` object representing a specific ladder diagram snippet. This `grid` would be a list of lists of `cellStruct` objects (from `managegrid.py`).
2.  Instantiate `ladderToOutLine` with this grid.
3.  Call `makeOutLine()`.
4.  Assert that the generated `outLine` (list of strings/lists) matches the expected structure and content.

**Test Cases:**

| Test ID   | Description                                     | Input Grid Snippet Representation                                                                                                | Expected `outLine` Snippet                                                                                                                                                              |
|-----------|-------------------------------------------------|----------------------------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| LTO-001   | Single Rung: NO Contact to Coil                 | `[[NO_Contact_in1 (var_A, io_in_1)], [Coil_out1 (var_A, io_out_1)]]` (simplified)                                                | `["//rung at 0", ["cont_var_A_NO", "contNO", "in_1"], ["output_var_A", "out_1"], "//end rung"]` (simplified)                                                                            |
| LTO-002   | Single Rung: NC Contact to Coil                 | `[[NC_Contact_in1 (var_B, io_in_1)], [Coil_out1 (var_B, io_out_1)]]`                                                              | `["//rung at 0", ["cont_var_B_NC", "contNC", "in_1"], ["output_var_B", "out_1"], "//end rung"]`                                                                                         |
| LTO-003   | Series Contacts (AND)                           | `[[NO_Contact_A], [NO_Contact_B], [Coil_C]]`                                                                                     | `[..., ["cont_A_NO", ...], ["cont_B_NO", ...], ["output_C", ...], ...]`                                                                                                                  |
| LTO-004   | Parallel Branch (OR)                            | Grid representing: <br> `----[ A ]--+----[ Out ]----` <br> `         |         ` <br> `         +----[ B ]--+`                   | `[..., ["startBR", [rowA, colA]], ["cont_A_NO", ...], ["node_", [node_loc], [brA_loc], [brB_loc]], ["startBR", [rowB, colB]], ["cont_B_NO", ...], ["output_Out", ...], ...]` (structure is key) |
| LTO-005   | Timer Element                                   | `[[NO_Contact_A], [Timer_T1 (name_T1, setpoint_5s)], [Coil_B]]`                                                                  | `[..., ["cont_A_NO", ...], ["rungstate_Timer_name_T1"], ["output_B", ...], ...]` (and an entry for Timer_T1 itself)                                                                     |
| LTO-006   | Counter Element                                 | `[[NO_Contact_A], [Counter_C1 (name_C1, setpoint_10)], [Coil_B]]`                                                                | `[..., ["cont_A_NO", ...], ["rungstate_Counter_name_C1"], ["output_B", ...], ...]` (and an entry for Counter_C1)                                                                     |
| LTO-007   | Math Element (e.g., Plus)                       | `[[Plus_Op (name_Res, srcA_Var1, srcB_Const5)]]` (as rightmost element)                                                           | `[..., ["Result_name_Res", "Plus", "Var1", "Constant", "", "5"], ...]`                                                                                                                  |
| LTO-008   | Comparison Element (e.g., Equals)               | `[[NO_Contact_A], [Equals_Comp (srcA_VarX, srcB_Const100)], [Coil_B]]`                                                           | `[..., ["cont_A_NO", ...], ["Equals_Comp_X_Y", "VarX", "Constant", "", "100"], ["output_B", ...], ...]`                                                                                |
| LTO-009   | Rung with only an Output (direct connection)    | `[[Coil_A]]` (assuming direct connection from power rail)                                                                        | `[..., ["output_A", ...], ...]`                                                                                                                                                         |
| LTO-010   | Empty Rung                                      | `[[MT], [MT], [MT]]`                                                                                                             | `["//rung at X", "//end rung"]` (or similar, indicating processing but no functional elements)                                                                                         |
| LTO-011   | Complex nested OR branches                      | A more involved grid with multiple ORs and ANDs nested.                                                                          | A correspondingly complex but predictable `outLine` with correct `startBR` and `node_` entries.                                                                                         |
| LTO-012   | Element with I/O and Comment                    | `[[NO_Contact (name_N, io_in_3, comment_C)]]`                                                                                     | `outLine` should correctly capture name, I/O, and type. Comments are not directly part of `outLine` elements but associated with the `cellStruct`.                                     |

**Mocking:**
- The `cellStruct` objects would need to be created manually for test inputs.
- No complex mocking of UI or other parts should be necessary if `ladderToOutLine` is well-isolated.

## II. Unit Tests for `OutLineToC.py`

**Module Purpose:** Converts the textual `outLine` into C code for AVR microcontrollers.

**Testing Goal:** Ensure individual `outLine` constructs are correctly translated into C code snippets. Also, verify correct variable initialization and hardware-specific I/O mapping.

**Key Class:** `OutLineToC`
**Key Method:** `makeC()` (though testing smaller helper methods might be more effective)

**Test Structure:**
For each test case:
1.  Create an `outLine` list representing a specific ladder construct.
2.  Instantiate `OutLineToC` with a mock `grid` (if needed for context like hardware type or full I/O lists) and `currentHW`.
3.  Call `makeC()` or specific helper methods (e.g., `addCounter`, `addTimer`, `findInPuts`, `findOutPuts`, `addMath`).
4.  Assert that the generated C code string contains the expected declarations, statements, and logic.

**Test Cases:**

| Test ID   | Description                                  | Input `outLine` Snippet                                                                      | Expected C Code Snippet (Conceptual)                                                                                                                                                                                             |
|-----------|----------------------------------------------|----------------------------------------------------------------------------------------------|------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------|
| OTC-001   | Variable Initialization (Contact NO)         | `[["cont_Start_PB_NO", "contNO", "in_1"]]`                                                   | `uint8_t cont_Start_PB_NO = 0;` (in `initVarsForMicro`)                                                                                                                                                                            |
| OTC-002   | Variable Initialization (Contact NC)         | `[["cont_Stop_PB_NC", "contNC", "in_1"]]`                                                    | `uint8_t cont_Stop_PB_NC = 1;`                                                                                                                                                                                                    |
| OTC-003   | Variable Initialization (Output Coil)        | `[["output_Motor", "out_1"]]`                                                                | `uint8_t output_Motor = 0;`                                                                                                                                                                                                        |
| OTC-004   | Input Reading (Waltech)                      | `[["cont_SensorA_NO", "contNO", "in_1"]]` (HW: Waltech)                                      | `cont_SensorA_NO = PINA & (1<<PA4);` (or similar, based on `self.inPutList` for Waltech, input 1)                                                                                                                              |
| OTC-005   | Input Reading (Arduino Uno, NC)              | `[["cont_Button_NC", "contNC", "in_1"]]` (HW: ArduinoUno)                                    | `cont_Button_NC = PINC & (1<<PC4);` (based on `self.inPutList` for Uno, input 1 is PC4, NC logic applied)                                                                                                                        |
| OTC-006   | Output Writing (Waltech)                     | `[["output_LED1", "out_1"]]` (HW: Waltech)                                                   | `if(output_LED1 == 0){PORTD &=~ (1<<PD2);} else {PORTD |= (1<<PD2);}` (based on `self.outPutList` for Waltech, output 1)                                                                                                         |
| OTC-007   | Output Writing (Arduino Uno)                 | `[["output_Relay_A", "out_1"]]` (HW: ArduinoUno)                                             | `if(output_Relay_A == 0){PORTD &=~ (1<<PD5);} else {PORTD |= (1<<PD5);}` (based on `self.outPutList` for Uno, output 1)                                                                                                         |
| OTC-008   | Basic Rung Logic (Contact -> Coil)           | `["//rung at 0", "W = 1;", ["cont_A_NO"], ["output_B"], "//end rung"]`                       | `W = 1; if(cont_A_NO == 0){W = 0;} output_B = W;`                                                                                                                                                                                 |
| OTC-009   | Series Logic (AND)                           | `["//rung at 0", "W = 1;", ["cont_A_NO"], ["cont_B_NO"], ["output_C"], "//end rung"]`          | `W = 1; if(cont_A_NO == 0){W = 0;} if(cont_B_NO == 0){W = 0;} output_C = W;`                                                                                                                                                     |
| OTC-010   | Parallel Logic (OR Node)                     | `[["startBR", [0,0]], ["cont_A_NO"], ["node_", [0,1], [0,0], [1,0]], ["startBR", [1,0]], ["cont_B_NO"], ["output_C"]]` | Complex, involves `branch_0_0`, `branch_1_0`. `if( (branch_0_0 == 0) && (branch_1_0 == 0) ){W = 0;}` (or similar logic based on how branches are set for true/false states)                                                       |
| OTC-011   | Timer Logic                                  | `[["rungstate_Timer_T1"], ["Timer_T1", "Timer", "500"]]` (setpoint 500 for 5s)               | Includes `rungstate_Timer_T1 = W;`, logic for `prev_rungstate_Timer_T1`, `run_Timer_T1`, `reg_Timer_T1++`, comparison with `setpoint_Timer_T1`.                                                                                |
| OTC-012   | Counter Logic with Reset                     | `[["rungstate_Counter_C1"], ["Counter_C1", "Counter", "10"], ["output_ResetCoil"]]` (ResetCoil name matches Counter_C1) | Includes `rungstate_Counter_C1 = W;`, logic for `prev_rungstate_Counter_C1`, `reg_Counter_C1++`, comparison. Reset logic: `if(output_ResetCoil == 1){reg_Counter_C1=0; Counter_C1=0;}`                                              |
| OTC-013   | Math Operation (Plus, Constant & Variable)   | `[["Result_Sum", "Plus", "VarA", "Constant", "", "10"]]`                                    | `if (W == 1){ Result_Sum = do_math(output_VarA, 10, '+');}` (assuming VarA is an output type) or `do_math(reg_ADC_VarA, 10, '+')` if VarA is an ADC/Timer/Counter register.                                                 |
| OTC-014   | Comparison Operation (Greater Than)          | `[["Greater_Comp1_NO", "VarA", "Constant", "100", ""]]`                                     | `if(output_VarA > 100){Greater_Comp1_NO=1;} else {Greater_Comp1_NO=0;}`                                                                                                                                                           |
| OTC-015   | PWM Setup and Update (Arduino Uno)           | `[["PWM_P1", "pwm_1", "50"]]` (HW: ArduinoUno, 50% duty)                                     | Setup: `DDRB |= (1<<PB1); TCCR1A |= (1<<COM1A1); ... OCR1A = 250; ICR1 = 500;` <br> Update: `if ((W == 1 )&& (pwm_1 == 0)){OCR1A=250; pwm_1 = 1; } if ((W == 0 )&& (pwm_1 == 0)){OCR1A= 0;}` (Value 250 for 50% of 500 TOP) |
| OTC-016   | ADC Reading (Arduino Uno)                    | `[["ADC_Sensor1", "adc_1"]]` (HW: ArduinoUno)                                                | `if (W == 1){reg_ADC_Sensor1=read_adc(0);}` (Channel 0 for adc_1)                                                                                                                                                                |
| OTC-017   | DDR Initialization (Arduino Uno)             | (Based on `self.outPutList` and `self.inPutList` for Uno)                                    | `DDRD |= (1<<PD5); ... DDRC &=~ (1<<PC4); PORTC |= (1<<PC4);` (for pullup)                                                                                                                                                       |

**Mocking:**
- `currentHW` would be set directly.
- I/O lists (`self.inPutList`, `self.outPutList`, etc.) would be part of the `OutLineToC` instance.
- For methods like `addMath` or `addPWM`, the `outline` and `line number` would be the direct inputs.
- The `hexMaker` call would not be executed in unit tests; the focus is on C code string generation.

This plan provides a solid foundation for developing unit tests to significantly improve the reliability of the core logic of Waltech Ladder Maker.
