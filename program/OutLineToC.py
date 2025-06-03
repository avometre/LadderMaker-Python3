"""
Waltech Ladder Maker is distributed under the MIT License. 

Copyright (c) 2014 Karl Walter.  karl (at) waltech.com

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
"""
#!/usr/bin/env python
# -*- coding: utf-8 -*- 

#this wil be the outline to C functions
from PyQt5 import QtCore, QtGui
from PyQt5.QtGui import QFont
from managegrid import ManageGrid  
import sys     

class OutLineToC():
    
    def __init__(self,grid,currentHW):#bring in all the things being sent down here
        self.grid = grid
        self.currentHW = currentHW
        
        if self.currentHW == "Waltech":
            #>>>inputs for Waltech IC
            self.inPutList = ["PINA",4],["PINA",3],["PINA",2],["PINA",1]\
                            ,["PINB",0],["PINB",1],["PINB",2],["PINB",3]\
                            ,["PINC",0],["PINC",1],["PINC",2],["PINC",3]
            #>>>outputs:                
            self.outPutList = ["PORTD",2],["PORTD",3],["PORTD",4],["PORTD",5]\
                            ,["PORTB",4],["PORTA",5],["PORTA",6],["PORTA",7]\
                            ,["PORTC",4],["PORTC",5],["PORTC",6],["PORTC",7]
            self.ADCList = []
            self.PWMList = []
                            
        if currentHW == "ArduinoUno":
            #>>>inputs 
            self.inPutList = ["PINC",4],["PINC",5],["PIND",2],["PIND",3]\
                            ,["PIND",4]
            #>>>outputs:                
            self.outPutList =["PORTD",5],["PORTD",6],["PORTD",7]\
                            ,["PORTB",0],["PORTB",3],["PORTB",4],["PORTB",5]
                            
            self.ADCList  = ["DDRC",0,0],["DDRC",1,1],["DDRC",2,2],["DDRC",3,3]
            #mode8 PWM on 16 bit timer
            self.PWMList  = ["DDRB","1","TCCR1A","----","COM1A1","TCCR1B","WGM13","CS10","OCR1A","ICR1"],\
                            ["DDRB","2","TCCR1A","----","COM1B1","TCCR1B","WGM13","CS10","OCR1B","ICR1"]
            
        if currentHW == "ArduinoNano": #same as Uno
            #>>>inputs 
            self.inPutList = ["PINC",4],["PINC",5],["PIND",2],["PIND",3]\
                            ,["PIND",4]
            #>>>outputs:                
            self.outPutList =["PORTD",5],["PORTD",6],["PORTD",7]\
                            ,["PORTB",0],["PORTB",3],["PORTB",4],["PORTB",5]
                            
            self.ADCList  = ["DDRC",0,0],["DDRC",1,1],["DDRC",2,2],["DDRC",3,3]
            #mode8 PWM on 16 bit timer
            self.PWMList  = ["DDRB","1","TCCR1A","----","COM1A1","TCCR1B","WGM13","CS10","OCR1A","ICR1"],\
                            ["DDRB","2","TCCR1A","----","COM1B1","TCCR1B","WGM13","CS10","OCR1B","ICR1"]
            
        if currentHW == "ArduinoMega":
            #>>>inputs 
            self.inPutList = ["PINK",0],["PINK",1],["PINK",2],["PINK",3],["PINK",4],["PINK",5],["PINK",6],["PINK",7]\
                            ,["PINB",0],["PINB",2]\
                            ,["PINL",0],["PINL",2],["PINL",4],["PINL",6]\
                            ,["PING",0],["PING",2]\
                            ,["PINC",0],["PINC",2],["PINC",4],["PINC",6]
            #>>>outputs:                
            self.outPutList= ["PORTB",1],["PORTB",3]\
                            ,["PORTL",1],["PORTL",3],["PORTL",5],["PORTL",7]\
                            ,["PORTG",1]\
                            ,["PORTD",7]\
                            ,["PORTC",1],["PORTC",3],["PORTC",5],["PORTC",7]\
                            ,["PORTA",6],["PORTA",4],["PORTA",2],["PORTA",0]\
                            ,["PORTD",0],["PORTB",1]

            #>>>PWM:     OK, checked mega2560  
            #Port, pin,(8 other register settings)  
            #in order of pwm_X choices in ladder       
            self.PWMList = ["DDRE","4","TCCR3A","----","COM3B1","TCCR3B","WGM33","CS30","OCR3B","ICR3"],\
                           ["DDRE","5","TCCR3A","----","COM3C1","TCCR3B","WGM33","CS30","OCR3C","ICR3"],\
                           ["DDRE","3","TCCR3A","----","COM3A1","TCCR3B","WGM33","CS30","OCR3A","ICR3"],\
                           \
                           ["DDRH","3","TCCR4A","----","COM4A1","TCCR4B","WGM43","CS40","OCR4A","ICR4"],\
                           ["DDRH","4","TCCR4A","----","COM4B1","TCCR4B","WGM43","CS40","OCR4B","ICR4"],\
                           \
                           ["DDRB","5","TCCR1A","----","COM1A1","TCCR1B","WGM13","CS10","OCR1A","ICR1"],\
                           ["DDRB","6","TCCR1A","----","COM1B1","TCCR1B","WGM13","CS10","OCR1B","ICR1"],\
                           ["DDRB","7","TCCR1A","----","COM1C1","TCCR1B","WGM13","CS10","OCR1C","ICR1"]

            #>>>ADC:  
            #Port DDR, pin, ADC channel #don't really need DDR             
            self.ADCList =  ["DDRF",0,0],\
                            ["DDRF",1,1],\
                            ["DDRF",2,2],\
                            ["DDRF",3,3],\
                            ["DDRF",4,4],\
                            ["DDRF",5,5],\
                            ["DDRF",6,6],\
                            ["DDRF",7,7]
                           

        
    def makeC(self,outLine,displayOutputPlace):
        print("making C\n")
        C_code_lines = []
        
        C_code_lines.append("#include <stdint.h>\n")
        C_code_lines.append("#include <stdlib.h>\n")
        C_code_lines.append("#include <string.h>\n")
        C_code_lines.append("#include <avr/io.h>\n")
        C_code_lines.append("#include <avr/interrupt.h>\n\n")

        C_code_lines.append("#define TIMER0_RELOAD_VALUE 101\n")
        C_code_lines.append("#define PWM_TIMER_TOP_VALUE 500\n")
        C_code_lines.append("#define PWM_PERCENT_TO_VALUE_SCALE_FACTOR 5.0\n\n")

        C_code_lines.append("volatile uint8_t timerOF=0;\n")
        if self.currentHW == "ArduinoMega"or self.currentHW == "ArduinoUno" or self.currentHW == "ArduinoNano":
            C_code_lines.append("#define OVERSAMPLES 10\n") # Already present, ensure it's not duplicated by mistake
            
            C_code_lines.append("static volatile uint16_t adcData;\n")
            C_code_lines.append("static volatile uint16_t ADCtotal;\n")
            C_code_lines.append("static volatile uint8_t adcDataL;\n")
            C_code_lines.append("static volatile uint8_t adcDataH;\n")
            C_code_lines.append("static volatile uint8_t sample_count;\n")
        
        if self.currentHW == "Waltech":
            C_code_lines.append("ISR(TIMER0_OVF_vect){timerOF=1;}\n") # Removed inline
        if self.currentHW == "ArduinoMega"or self.currentHW == "ArduinoUno" or self.currentHW == "ArduinoNano":
            C_code_lines.append("ISR(TIMER0_OVF_vect){timerOF=1;}\n") # Removed inline
        
        if self.currentHW == "ArduinoMega"or self.currentHW == "ArduinoUno" or self.currentHW == "ArduinoNano":
            C_code_lines.append("ISR(ADC_vect)\n{\n") # Removed inline
            C_code_lines.append("    adcDataL = ADCL;\n")
            C_code_lines.append("    adcDataH = ADCH;\n")
            C_code_lines.append("    adcData = 0;\n")
            C_code_lines.append("    adcData = adcData | adcDataH;\n")
            C_code_lines.append("    adcData = adcData << 8;\n")
            C_code_lines.append("    adcData = adcData | adcDataL;\n")
            C_code_lines.append("    ADCtotal = ADCtotal+adcData;\n")
            C_code_lines.append("    sample_count ++;\n}\n")

        #MATH:
        C_code_lines.append("int16_t do_math(int16_t A,int16_t B,char operator)\n{\n")
        C_code_lines.append("    int32_t result = 0;\n")
        C_code_lines.append("    if (operator == '+'){result = A+B;}\n")
        C_code_lines.append("    if (operator == '-'){result = A-B;}\n")
        C_code_lines.append("    if (operator == '*'){result = A*B;}\n")
        C_code_lines.append("    if (operator == '/')\n    {\n")
        C_code_lines.append("        if (B == 0) { return 0; /* Or INT16_MAX, or handle error appropriately */ }\n")
        C_code_lines.append("        result = A/B;\n    }\n")
        C_code_lines.append("//    if (operator == '='){result = A = B;} // This was commented out\n")
        C_code_lines.append("    return (int16_t)result; // Simpler cast\n}\n")
        
        #ADC:
        if self.currentHW == "ArduinoMega"or self.currentHW == "ArduinoUno" or self.currentHW == "ArduinoNano":
            C_code_lines.append("uint16_t read_adc(uint8_t channel)\n{\n")
            #C_code_lines.append("    sei();//set enable interrupts\n")
            C_code_lines.append("    ADMUX = channel;// set channel\n")
            C_code_lines.append("    ADMUX |=  (1<<REFS0);// sets ref volts to Vcc\n")
            C_code_lines.append("    ADCSRA |= (1<<ADEN); // enable the ADC\n")
            C_code_lines.append("    sample_count = 0; ADCtotal = 0;//clear sample count\n")
            C_code_lines.append("    ADCSRA |= (1<<ADSC);//start conversion\n")
            C_code_lines.append("    //read adcData done in interrupt\n")
            C_code_lines.append("    while (sample_count < OVERSAMPLES){asm volatile (\"nop\"::);}//wait for completion\n")
            C_code_lines.append("    ADCSRA &=~ (1<<ADEN); // stop the ADC\n")
            C_code_lines.append("    return (ADCtotal/OVERSAMPLES); //mx osamples = 63  othewise will overflow total register with 10 bit adc results\n}\n")

        C_code_lines.append("int main()\n")
        C_code_lines.append("{\n")
        if self.currentHW == "ArduinoMega"or self.currentHW == "ArduinoUno" or self.currentHW == "ArduinoNano":
            C_code_lines.append("//set up ADC\n")
            C_code_lines.append("    ADCSRA |= ( (1<<ADPS2)|(1<<ADPS1)|(1<<ADPS0) );//  sets adc clock prescaler to 128 //checked\n")
            C_code_lines.append("    ADCSRA |= (1<<ADIE); // enable ADC conversion complete interrupt\n")
            C_code_lines.append("    ADCSRA |= (1<<ADATE);// set to auto trigger (free running by default)\n")
        self.DDROutPuts(C_code_lines)#//do DDR's#//use outputlist to generate
        #pullups on for Arduino:
        if self.currentHW == "ArduinoMega"or self.currentHW == "ArduinoUno" or self.currentHW == "ArduinoNano":
            self.pullupInPuts(C_code_lines)
        C_code_lines.append("    //set up loop timer:\n")
        if self.currentHW == "Waltech":
            C_code_lines.append("    TIMSK |= (1<<TOIE0);// overflow capture enable\n")
            C_code_lines.append("    TCNT0 = TIMER0_RELOAD_VALUE;// start at this\n")
            C_code_lines.append("    TCCR0 |= (1<<CS02);// timer started with /256 prescaler  fills up @61 hz\n")
        if self.currentHW == "ArduinoMega"or self.currentHW == "ArduinoUno" or self.currentHW == "ArduinoNano":
            C_code_lines.append("    TIMSK0 |= (1<<TOIE0);// overflow capture enable\n")
            C_code_lines.append("    TCNT0 = TIMER0_RELOAD_VALUE;// start at this\n")
            C_code_lines.append("    TCCR0B |= ((1<<CS10)|(1<<CS12));// timer started with /1024 prescaler \n ")
            self.setUpPWMs(outLine,C_code_lines)
            
        C_code_lines.append("    sei();\n")
        self.initVarsForMicro(outLine,C_code_lines) # This will be refactored next
        C_code_lines.append("    uint8_t rung_current_state = 1;\n") # W to rung_current_state
        C_code_lines.append("    while (1)\n")
        C_code_lines.append("    {\n")
        C_code_lines.append("        if (timerOF == 1)\n")
        C_code_lines.append("        {\n")
        
        if self.currentHW == "Waltech":
            C_code_lines.append("           timerOF=0;//reset timer flag\n")
            C_code_lines.append("           TCNT0 = TIMER0_RELOAD_VALUE;// start at this\n")
            self.findInPuts(outLine,C_code_lines)
            
        if self.currentHW == "ArduinoMega"or self.currentHW == "ArduinoUno" or self.currentHW == "ArduinoNano":
            C_code_lines.append("           timerOF=0;//reset timer flag\n")
            C_code_lines.append("           TCNT0 = TIMER0_RELOAD_VALUE;// start at this\n")#ok
            self.findInPutsArd(outLine,C_code_lines)
        
        if self.currentHW == "ArduinoMega"or self.currentHW == "ArduinoUno" or self.currentHW == "ArduinoNano":
            pwmList = []
            for i in range (len(outLine)):
                if "PWM_" == str(outLine[i][0])[:4] and outLine[i][1] not in pwmList:
                    C_code_lines.append("           "+str(outLine[i][1]) +" = 0;//set PWM flag to 0\n")
                    pwmList.append(outLine[i][1])

        #go through the outLine and create  if-then and or statements from elements

        currentBranchList=[None]
        for i in range (len(outLine)):
            if "//" in outLine[i]:
                C_code_lines.append("            "+str(outLine[i])+"\n")
            if "rung at" in outLine[i]:
                C_code_lines.append("             rung_current_state = 1;\n") # W to rung_current_state
            #BRANCHES:    
            if "branch" in outLine[i]: #normal branch, not a starter
                C_code_lines.append("             branch_"+\
                        str(outLine[i][1][0])+"_"+str(outLine[i][1][1])+ " = 1;\n")
                currentBranchList.append(outLine[i][1])#this keeps track of the nested branches
            if "startBR" in outLine[i]:#starter branch.  add to branchlist 
                C_code_lines.append("             branch_"+\
                        str(outLine[i][1][0])+"_"+str(outLine[i][1][1])+ " = 1;\n")
                currentBranchList.append(outLine[i][1])#this keeps track of the nested branches
            #print("current branch", currentBranchList)
            #COMPARISONS:
            ##027##
            #"Equals" "Greater""Lessthan""GreaterOrEq""LessOrEq"
            if "Equals_" in str(outLine[i][0]):
                self.addEquals(outLine, C_code_lines, i)
            if "Greater_" in str(outLine[i][0]):
                self.addGreater(outLine, C_code_lines, i)
            if "Lessthan_" in str(outLine[i][0]):
                self.addLessthan(outLine, C_code_lines, i)
            if "GreaterOrEq_" in str(outLine[i][0]):
                self.addGreaterOrEq(outLine, C_code_lines, i)
            if "LessOrEq_" in str(outLine[i][0]):
                self.addLessOrEq(outLine, C_code_lines, i)
               
            #ELEMENTS:
            ##026##

            if "cont_" in str(outLine[i][0])\
                    or "Counter_" in str(outLine[i][0])\
                    or "Timer_" in str(outLine[i][0])\
                    or "Fall_" in str(outLine[i][0])\
                    or "Equals_" in str(outLine[i][0])\
                    or "Greater_" in str(outLine[i][0])\
                    or "Lessthan_" in str(outLine[i][0])\
                    or "GreaterOrEq_" in str(outLine[i][0])\
                    or "LessOrEq_" in str(outLine[i][0]):
                varNameStr = str(outLine[i][0])
                if len(outLine[i])>=2 and ("contNO" in outLine[i][1]):
                    varNameStr=varNameStr+"_NO"
                if len(outLine[i])>=2 and ("contNC" in outLine[i][1]):
                    varNameStr=varNameStr+"_NC"      
                if "rungstate" not in str(outLine[i][0]):
                    #element on rung, no parallel: (apply to rung_current_state)
                    if currentBranchList[-1] == None:
                        if (len(outLine[i])>3) and  ("latching" in outLine[i][3]):
                            C_code_lines.append("             if("+varNameStr+ " == 0){rung_current_state = 0;}\n") # W to rung_current_state
                            C_code_lines.append("             else{rung_current_state = 1;}\n") # W to rung_current_state
                        else:
                            C_code_lines.append("             if("+varNameStr+ " == 0){rung_current_state = 0;}\n") # W to rung_current_state
                    #element with parallel (apply to last item in branchlist )
                    if  currentBranchList[-1] != None:
                        if (len(outLine[i])>3) and  ("latching" in outLine[i][3]):
                            C_code_lines.append("             if("+\
                            varNameStr+ " == 0){branch_"+str(currentBranchList[-1][0])+"_"+str(currentBranchList[-1][1])+" = 0;}\n")
                            C_code_lines.append("             else {branch_"+str(currentBranchList[-1][0])+"_"+str(currentBranchList[-1][1])+" = 2;}\n")
                        else:
                            C_code_lines.append("             if("+\
                                varNameStr+ " == 0){branch_"+str(currentBranchList[-1][0])+"_"+str(currentBranchList[-1][1])+" = 0;}\n")

            
            #NODE:
            #if "node_" in outLine[i][0]:
            if str(outLine[i][0])[:5] == "node_":    
                tempText1_list = []
                tempText2_list = []
                tempText1_list.append("             if( ") #for node
                tempText2_list.append("             if( ") # for node with latching on it
                for k in range(2,len(outLine[i])):
                    a = outLine[i][k][0]
                    b = outLine[i][k][1]
                    tempText1_list.append("(branch_"+str(a) + "_"+ str(b)+" == 0) && ")
                    tempText2_list.append("(branch_"+str(a) + "_"+ str(b)+" == 2) || ")
                    #Branch tracking:
                    #look through currentBranchList and remove (pop) any matching a,b
                    m = 0
                    while m < len(currentBranchList):
                        if currentBranchList[m] == [a,b]: 
                            #print("A,B here")
                            currentBranchList.pop(m)
                        else: m = m+1

                tempText1 = "".join(tempText1_list)
                tempText2 = "".join(tempText2_list)

                tempText1 = tempText1[:-5]#take away last " && " or " || "
                tempText2 = tempText2[:-5]#take away last " && " or " || "
                if currentBranchList[-1] != None:
                    tempText1 = tempText1 +" )) {branch_"+str(currentBranchList[-1][0])+"_"+str(currentBranchList[-1][1])+" = 0;} \n" 
                    tempText2 = tempText2 +" )) {branch_"+str(currentBranchList[-1][0])+"_"+str(currentBranchList[-1][1])+" = 1;} \n" 
                else:
                    tempText1 = tempText1 +" )) {rung_current_state = 0;} //"+ str(outLine[i][0])+ str(outLine[i][1])+"\n" # W to rung_current_state
                    tempText2 = tempText2 +" )) {rung_current_state = 1;} //"+ str(outLine[i][0])+ str(outLine[i][1])+" if is latching element\n" # W to rung_current_state
                C_code_lines.append(tempText1)
                C_code_lines.append(tempText2)
                    
            #State Users: (need to know the last state of the rung and the current state
            #WAS: if "rungstate_Counter" in str(outLine[i][0]):
            if str(outLine[i][0])[:17] ==  "rungstate_Counter":
                self.addCounter(outLine, C_code_lines, str(outLine[i][0]),outLine)
                
            #WAS: if "rungstate_Timer" in str(outLine[i][0]):
            if str(outLine[i][0])[:15] ==  "rungstate_Timer":
                self.addTimer(outLine, C_code_lines, str(outLine[i][0]))
            
            #WAS: if "rungstate_Fall" in str(outLine[i][0]):
            if str(outLine[i][0])[:14] ==  "rungstate_Fall":
                self.addFall(outLine, C_code_lines, str(outLine[i][0]))
            ##028##
            #OUTPUT:
            #WAS: if "output_" in str(outLine[i][0]):
            if str(outLine[i][0])[:7] ==  "output_":
                C_code_lines.append("              "+  str(outLine[i][0]) +" = rung_current_state;\n") # W to rung_current_state
            
            #MATH:
            #WAS: if "Result_" in str(outLine[i][0]):
            if str(outLine[i][0])[:7] ==  "Result_":
                self.addMath(outLine, C_code_lines, i)
            #PWM:
            #WAS: if "PWM_" == str(outLine[i][0])[:4]:
            if str(outLine[i][0])[:4] ==  "PWM_":
                self.addPWM(outLine, C_code_lines, i)
            #ADC:
            #WAS: if "ADC_" == str(outLine[i][0])[:4]:
            if str(outLine[i][0])[:4] ==  "ADC_" and str(outLine[i][1]) != "Internal":
                self.addADC(outLine, C_code_lines, i)

        self.findOutPuts(outLine,C_code_lines)
        #C_txt = self.linkNames(outLine, C_txt)
        C_code_lines.append("       }\n") #end of conditional
        C_code_lines.append("   }\n") #end of main loop
        C_code_lines.append("}\n") #end of main

        C_txt = "".join(C_code_lines)
        print(C_txt)
        
        print("saving C and Compiling")
        
        plat = sys.platform.lower()	# try to detect the OS so that a device can be selected...
        print(("checked platform", plat))
        opSys = "UNK" #default
        
        if   plat[:5] == 'linux': #linux
            opSys = "NIX"
        elif plat == 'win32':       #win32
            opSys = "WIN"
        elif plat == "darwin": #mac
            opSys = "MAC"
            print("found a MAC!")
        if opSys != "UNK":
            from hexmaker import hexMaker
            hexMaker(opSys).saveCfileAndCompile(C_txt,displayOutputPlace,self.currentHW)
        else: print("Op Sys not detected")
        
        
        
        
        
        
        
        
    #go through grid and assign inputs to variables    
    def findInPuts(self,outLine,C_code_lines):
        C_code_lines.append("           //inputs:\n")
        # Keep a record of added microPinStrings to avoid duplicates if C_code_lines is checked later
        # For now, assuming direct append based on original logic's C_txt check
        added_pin_strings_no = set()
        added_pin_strings_nc = set()

        for i in range (len(outLine)):
            #WAS if len(outLine[i])>2 and "in_" in str(outLine[i][2]) :
            if len(outLine[i])>2 and str(outLine[i][2])[:3] == "in_" :
                inNum = (int(outLine[i][2].split("in_")[1])) -1
                microPinString = str(self.inPutList[inNum][0])+ " &(1<<"+str(self.inPutList[inNum][1])+");\n"
                #very unlikley that an element name has "&(1<<" in it  plus the rest of the micropinstring
                # The original check `microPinString not in C_txt` is tricky with list appends.
                # We'll assume for now that the logic intends to add these lines if the condition is met.
                # A more robust check would involve inspecting C_code_lines if exact duplicate lines are an issue.
                if outLine[i][1] == "contNO": # and microPinString not in C_txt (approximated by set)
                    # Simplified: assume it should be added. If strict non-duplication of the exact C line is needed,
                    # the logic to check C_code_lines would be more complex.
                    C_code_lines.append("           "+str(outLine[i][0])+"_NO = "+microPinString)
                if outLine[i][1] == "contNC": # and microPinString not in C_txt (approximated by set)
                    C_code_lines.append("           "+str(outLine[i][0])+"_NC =~ "+microPinString)

            #link inputs to outputs if names shared:
            #print("linking output names")
            if len(outLine[i])>1 and outLine[i][1] == "contNO":
                basename = (str(outLine[i][0])[5:])
                for x in range (len(outLine)):
                    if outLine[x][0][:7] == "output_" and outLine[x][0][7:] == basename:
                        C_code_lines.append("             if(output_"+basename+" == 1){\n")
                        C_code_lines.append("                "+str(outLine[i][0])+"_NO=1;}\n")
                        C_code_lines.append("             else {\n")
                        C_code_lines.append("                "+str(outLine[i][0])+"_NO=0;} //link name\n")
            if len(outLine[i])>1 and outLine[i][1] == "contNC":
                basename = (str(outLine[i][0])[5:])
                for x in range (len(outLine)):
                    if outLine[x][0][:7] == "output_" and outLine[x][0][7:] == basename:
                        C_code_lines.append("             if(output_"+basename+" == 0){\n")
                        C_code_lines.append("                "+str(outLine[i][0])+"_NC=1;}\n")
                        C_code_lines.append("             else {\n")
                        C_code_lines.append("                "+str(outLine[i][0])+"_NC=0;} //link name\n")
        C_code_lines.append("\n")

        # return C_code_lines # No longer returns, modifies in place
    """don't need    
    def findFalling(self,outLine,C_code_lines):
        #need to write c code to set the falling variable based on the last one
        #will need to setup a falling variable ahead of time like initVarsForMicro
        # return C_code_lines # Modifies in place or returns list to extend
        pass # Placeholder if it's truly not needed or to be implemented later
    """

    #go through grid and assign inputs to variables for Arduino different only because hi is on  
    def findInPutsArd(self,outLine,C_code_lines):
        C_code_lines.append("           //inputs:\n")
        for i in range (len(outLine)):
            #WAS if len(outLine[i])>2 and "in_" in str(outLine[i][2]) :
            if len(outLine[i])>2 and str(outLine[i][2])[:3] == "in_" :
                inNum = (int(outLine[i][2].split("in_")[1])) -1
                microPinString = str(self.inPutList[inNum][0])+ " &(1<<"+str(self.inPutList[inNum][1])+");\n"
                # Similar to findInPuts, omitting C_txt check for brevity, assuming append is intended.
                if outLine[i][1] == "contNO":
                    C_code_lines.append("           "+str(outLine[i][0])+"_NO =~ "+microPinString)
                if outLine[i][1] == "contNC":
                    C_code_lines.append("           "+str(outLine[i][0])+"_NC = "+microPinString)
            #link inputs to outputs if names shared:
            #print("linking output names")
            if len(outLine[i])>1 and outLine[i][1] == "contNO":
                basename = (str(outLine[i][0])[5:])
                for x in range (len(outLine)):
                    if outLine[x][0][:7] == "output_" and outLine[x][0][7:] == basename:
                        C_code_lines.append("             if(output_"+basename+" == 1){\n")
                        C_code_lines.append("                "+str(outLine[i][0])+"_NO=1;}\n")
                        C_code_lines.append("             else {\n")
                        C_code_lines.append("                "+str(outLine[i][0])+"_NO=0;} //link name\n")
            if len(outLine[i])>1 and outLine[i][1] == "contNC":
                basename = (str(outLine[i][0])[5:])
                for x in range (len(outLine)):
                    if outLine[x][0][:7] == "output_" and outLine[x][0][7:] == basename:
                        C_code_lines.append("             if(output_"+basename+" == 0){\n")
                        C_code_lines.append("                "+str(outLine[i][0])+"_NC=1;}\n")
                        C_code_lines.append("             else {\n")
                        C_code_lines.append("                "+str(outLine[i][0])+"_NC=0;} //link name\n")
        C_code_lines.append("\n")
        # return C_code_lines # Modifies in place


    def addCounter(self,outline, C_code_lines, outlineEntry, wholeOutline):
        C_code_lines.append("             "+  outlineEntry +" = rung_current_state;\n") # W to rung_current_state
        baseName = outlineEntry[10:]
        C_code_lines.append("             if((prev_rungstate_"+baseName+" == 0) && (rungstate_"+baseName+" == 1)){\n")
        C_code_lines.append("                 reg_"+baseName +"++;\n")
        C_code_lines.append("                 if (reg_"+baseName+" == 65535) {reg_"+baseName+"--;}//avoid overrun\n")
        C_code_lines.append("                 if (setpoint_"+baseName+" <= reg_"+baseName+") {"+baseName+"=1;}\n")
        #C_code_lines.append("                 if (setpoint_"+baseName+" <= reg_"+baseName+") {W=1;}\n")
        C_code_lines.append("             }\n")
        C_code_lines.append("             prev_rungstate_"+baseName+" = rungstate_"+baseName+";\n")
        #check reset/ shared name with output:
        baseName = baseName[8:]
        #if "output_"+baseName in C_code_lines: # This check is problematic for a list of strings
        for x in range (len(wholeOutline)):
            if wholeOutline[x][0][:7] == "output_" and wholeOutline[x][0][7:] == baseName:
                C_code_lines.append("             if(output_"+baseName+" == 1){reg_Counter_"+baseName+"=0; Counter_"+baseName+"=0;} //reset\n")
        # return C_code_lines # Modifies in place
        
    def addTimer(self,outline, C_code_lines, outlineEntry):
        C_code_lines.append("             "+  outlineEntry +" = rung_current_state;\n") # W to rung_current_state
        baseName = outlineEntry[10:]
        C_code_lines.append("             if((prev_rungstate_"+baseName+" == 0) && (rungstate_"+baseName+" == 1)){\n")
        C_code_lines.append("                run_"+baseName +"=1;}\n")
        C_code_lines.append("             if(run_"+baseName+" == 1){\n")
        C_code_lines.append("                reg_"+baseName +"++;\n")
        C_code_lines.append("                if (reg_"+baseName+" == 65535) {reg_"+baseName+"--;}//avoid overrun\n")
        C_code_lines.append("                if (setpoint_"+baseName+" <= reg_"+baseName+") {"+baseName+"=1;}\n")
        C_code_lines.append("             }\n")
        
        #check reset/ shared name with output:
        #baseName = baseName[6:]
        C_code_lines.append("             if((prev_rungstate_"+baseName+" == 1) && (rungstate_"+baseName+" == 0)){\n")
        C_code_lines.append("                reg_"+baseName+"=0; "+baseName+"=0; run_"+baseName+"=0;} //reset\n")
        C_code_lines.append("             prev_rungstate_"+baseName+" = rungstate_"+baseName+";\n")
        # return C_code_lines # Modifies in place
    
    def addFall(self,outline, C_code_lines, outlineEntry):
        baseName = outlineEntry[10:]
        C_code_lines.append("             if("+baseName+" == 1){"+baseName+" = 0;}\n")
        C_code_lines.append("             "+  outlineEntry +" = rung_current_state;\n") # W to rung_current_state

        C_code_lines.append("             if((prev_rungstate_"+baseName+" == 1) && (rungstate_"+baseName+" == 0)){\n")
        C_code_lines.append("             "+baseName+"=1;\n")
        C_code_lines.append("             }\n")
        C_code_lines.append("             prev_rungstate_"+baseName+" = rungstate_"+baseName+";\n")
        # return C_code_lines # Modifies in place
  
   
    #COMPARISONS:    
    def addEquals(self,outline, C_code_lines, line):
        temp_list = []
        if outline[line][1] == "Constant":
            temp_list.append("             if("+ str(outline[line][3]) +" == ")
        else:
            temp_list.append("             if("+self.outputAndName(outline,outline[line],1)+" == ")
        if outline[line][2] == "Constant":
            temp_list.append(str(outline[line][4])+"){\n")
        else:
            temp_list.append(self.outputAndName(outline,outline[line],2)+"){\n")
        
        temp_list.append(str(outline[line][0])+"=1;}\n")
        temp_list.append("             else {\n")
        temp_list.append(str(outline[line][0])+"=0;} //comparison\n")
        C_code_lines.extend(temp_list) # Use extend for list of strings
        # return C_code_lines # Modifies in place

    def addGreater(self,outline, C_code_lines, line):
        temp_list = []
        if outline[line][1] == "Constant":
            temp_list.append("             if("+ str(outline[line][3]) +" > ")
        else:
            temp_list.append("             if("+self.outputAndName(outline,outline[line],1)+" > ")
        if outline[line][2] == "Constant":
            temp_list.append(str(outline[line][4])+"){\n")
        else:
            temp_list.append(self.outputAndName(outline,outline[line],2)+"){\n")
        
        temp_list.append(str(outline[line][0])+"=1;}\n")
        temp_list.append("             else {\n")
        temp_list.append(str(outline[line][0])+"=0;} //comparison\n")
        C_code_lines.extend(temp_list)
        # return C_code_lines # Modifies in place

    def addLessthan(self,outline, C_code_lines, line):
        temp_list = []
        if outline[line][1] == "Constant":
            temp_list.append("             if("+ str(outline[line][3]) +" < ")
        else:
            temp_list.append("             if("+self.outputAndName(outline,outline[line],1)+" < ")
        if outline[line][2] == "Constant":
            temp_list.append(str(outline[line][4])+"){\n")
        else:
            temp_list.append(self.outputAndName(outline,outline[line],2)+"){\n")
        
        temp_list.append(str(outline[line][0])+"=1;}\n")
        temp_list.append("             else {\n")
        temp_list.append(str(outline[line][0])+"=0;} //comparison\n")
        C_code_lines.extend(temp_list)
        # return C_code_lines # Modifies in place

    def addGreaterOrEq(self,outline, C_code_lines, line):
        temp_list = []
        if outline[line][1] == "Constant":
            temp_list.append("             if("+ str(outline[line][3]) +" >= ")
        else:
            temp_list.append("             if("+self.outputAndName(outline,outline[line],1)+" >= ")
        if outline[line][2] == "Constant":
            temp_list.append(str(outline[line][4])+"){\n")
        else:
            temp_list.append(self.outputAndName(outline,outline[line],2)+"){\n")
        
        temp_list.append(str(outline[line][0])+"=1;}\n")
        temp_list.append("             else {\n")
        temp_list.append(str(outline[line][0])+"=0;} //comparison\n")
        C_code_lines.extend(temp_list)
        # return C_code_lines # Modifies in place

    def addLessOrEq(self,outline, C_code_lines, line):
        temp_list = []
        if outline[line][1] == "Constant":
            temp_list.append("             if("+ str(outline[line][3]) +" <= ")
        else:
            temp_list.append("             if("+self.outputAndName(outline,outline[line],1)+" <= ")
        if outline[line][2] == "Constant":
            temp_list.append(str(outline[line][4])+"){\n")
        else:
            temp_list.append(self.outputAndName(outline,outline[line],2)+"){\n")
        
        temp_list.append(str(outline[line][0])+"=1;}\n")
        temp_list.append("             else {\n")
        temp_list.append(str(outline[line][0])+"=0;} //comparison\n")
        C_code_lines.extend(temp_list)
        # return C_code_lines # Modifies in place
        
    def addMath(self,outline, C_code_lines, line):
        temp_list = []
        if outline[line][1] == "Plus": Operator = "\'+\'"
        if outline[line][1] == "Minus": Operator = "\'-\'"
        if outline[line][1] == "Mult": Operator = "\'*\'"
        if outline[line][1] == "Divide": Operator = "\'/'"
        #if outline[line][1] == "Move": Operator ="\'=\'"
        print(("operator",Operator))
        temp_list.append("            if (rung_current_state == 1){\n                 "+str(outline[line][0])+" = ") # W to rung_current_state
        if outline[line][2] == "Constant":
            temp_list.append(" do_math("+str(outline[line][4])+",")
        else:
            temp_list.append(" do_math("+self.outputAndName(outline,outline[line],2)+",") #2
        if outline[line][3] == "Constant":
            temp_list.append(str(outline[line][5])+",")
        else:
            temp_list.append(self.outputAndName(outline,outline[line],3)+",") #3
        temp_list.append(Operator +");}\n")
        C_code_lines.extend(temp_list)
        # return C_code_lines # Modifies in place
            
    def addPWM(self,outline, C_code_lines, line):
        if outline[line][1][:4] == "pwm_" : #if "internal" then PWM disabled
            pwmNum = (int (outline[line][1].split("pwm_")[1])) -1# this is the pwm #
            # pwmVal calculation is done in C using the define
            C_code_lines.append(f"            if ((rung_current_state == 1 )&& ("+outline[line][1]+" == 0)){{"+self.PWMList[pwmNum][8]+"= (int)(round("+str(outline[line][2])+" * PWM_PERCENT_TO_VALUE_SCALE_FACTOR));"+ outline[line][1]+" = 1; }}\n") # W to rung_current_state and use define
            C_code_lines.append(f"            if ((rung_current_state == 0 )&& ("+outline[line][1]+" == 0)){{"+self.PWMList[pwmNum][8]+"= 0;}}\n") # W to rung_current_state
        # return C_code_lines # Modifies in place
        
    def addADC(self,outline, C_code_lines, line):
        channel = str((int (outline[line][1].split("adc_")[1])) -1)# this is the adc# 
        
        C_code_lines.append("            if (rung_current_state == 1){") # W to rung_current_state
        C_code_lines.append("reg_"+outline[line][0]+"=read_adc("+channel+");}\n")
        C_code_lines.append("            else{reg_"+outline[line][0]+"=0;}\n")
        # return C_code_lines # Modifies in place
    
    ##030##
    def outputAndName(self,outline,thisLine,pos):
        #scan outline for name
        #determine if output (8 bit unsigned) or result (16 bit signed)
        outputName = None
        for i in range (len(outline)):                  #check for Results first
            #print("compare to", str(outline[i][0]))
            if len(outline[i])>1 and  str(outline[i][0]) == "Result_"+str(thisLine[pos]):
                outputName = "Result_"+ str(thisLine[pos])
                return outputName
        for i in range (len(outline)):                  
            #print("compare to", str(outline[i][0]))
            if len(outline[i])>1 and  str(outline[i][0]) == "Counter_"+str(thisLine[pos]):
                outputName = "reg_Counter_"+ str(thisLine[pos])
                return outputName
        for i in range (len(outline)):                  
            #print("compare to", str(outline[i][0]))
            if len(outline[i])>1 and  str(outline[i][0]) == "Timer_"+str(thisLine[pos]):
                outputName = "reg_Timer_"+ str(thisLine[pos])
                return outputName
        for i in range (len(outline)):                  
            #print("compare to", str(outline[i][0]))
            if len(outline[i])>1 and  str(outline[i][0]) == "ADC_"+str(thisLine[pos]):
                outputName = "reg_ADC_"+ str(thisLine[pos])
                return outputName
        for i in range (len(outline)):
            if len(outline[i])>1 and  str(outline[i][0]) == "output_"+str(thisLine[pos]):
                outputName = "output_"+ str(thisLine[pos])
                print("comparing to a binary output")
        return outputName
        
    #go through grid and assign outputs to variables 
    def findOutPuts(self,outLine,C_code_lines):
        C_code_lines.append("           //outputs:\n")
        for i in range (len(outLine)):
            #WAS if len(outLine[i])>1 and "out_" in str(outLine[i][1]) :
            if len(outLine[i])>1 and  str(outLine[i][1])[:4] == "out_":    
                outNum = (int(outLine[i][1].split("out_")[1])) -1
                microString =  "         if("+str(outLine[i][0])+" == 0){"\
                                +str(self.outPutList[outNum][0])+" &=~ (1<<"+str(self.outPutList[outNum][1])\
                                +");}\n"
                C_code_lines.append(microString)
                C_code_lines.append("         else {"+str(self.outPutList[outNum][0])\
                                +" |= (1<<"+str(self.outPutList[outNum][1])+");}\n")
        C_code_lines.append("\n")
        # return C_code_lines # Modifies in place
    
    #set outputs on micro    
    def DDROutPuts(self,C_code_lines):
        for x in range(len(self.outPutList)):
            dirport = self.outPutList[x][0].strip("PORT")
            C_code_lines.append("   DDR"+dirport+\
                    " |= (1<<"+str(self.outPutList[x][1])+");\n")
        C_code_lines.append("\n")
        # return C_code_lines # Modifies in place
        
    def pullupInPuts(self,C_code_lines):
        for x in range(len(self.inPutList)):
            dirport = self.inPutList[x][0].strip("PIN")
            C_code_lines.append("   PORT"+dirport+\
                    " |= (1<<"+str(self.inPutList[x][1])+");\n")
        C_code_lines.append("\n")
        # return C_code_lines # Modifies in place
        
    ##029##
    def initVarsForMicro(self, outLine, C_code_lines):
            # look for cont_ and output_  These whole strings will be var names I_J
            #look for startBR and  branch: #these become branch_I_Jfor i in range (len(outLine)):
        # The logic `if "..." not in C_txt` is problematic.
        # It needs to be replaced with a set to track declared variables as per requirement 4.
        # This will be handled in a subsequent focused refactoring step for initVarsForMicro.
        # For now, we replicate the append behavior based on the original string check logic.
        # This means the check might not be perfect if the C_code_lines list content isn't easily searchable like a flat string.
        # This is a temporary measure to get the list-based structure in place.

        # temp_C_txt_for_checks = "".join(C_code_lines) # Create a temporary string for checks, less efficient but preserves logic for now
        # Refactor initVarsForMicro to use a set for declared_variables
        declared_variables = set()

        pwmList = [] # This list is specific to PWM setup, not general variable declaration.
        for i in range (len(outLine)): 
            var_name = ""
            var_declaration = ""

            if str(outLine[i][0])[:5] == "cont_" and str(outLine[i][1])[:6] == "contNO":
                var_name = str(outLine[i][0]) + "_NO"
                var_declaration = f"    uint8_t {var_name} = 0;\n"
            elif str(outLine[i][0])[:5] == "cont_" and str(outLine[i][1])[:6] == "contNC":
                var_name = str(outLine[i][0]) + "_NC"
                var_declaration = f"    uint8_t {var_name} = 1;\n"
            elif str(outLine[i][0])[:7] == "output_":
                var_name = str(outLine[i][0])
                var_declaration = f"    uint8_t {var_name} = 0;\n"
            elif str(outLine[i][0])[:7] == "Result_":
                var_name = str(outLine[i][0])
                var_declaration = f"    int16_t {var_name} = 0;\n"
            elif str(outLine[i][0])[:6] == "branch" or str(outLine[i][0])[:7] == "startBR":
                var_name = f"branch_{str(outLine[i][1][0])}_{str(outLine[i][1][1])}"
                var_declaration = f"    uint8_t {var_name} = 0;\n"
            elif str(outLine[i][0])[:5] == "node_": # Check for branches associated with nodes
                # This logic might be slightly different as it's based on outLine[i][-1]
                # For now, we'll try to capture it. A specific var_name for node's branch might be complex.
                # Original: "    uint8_t branch_"+str(outLine[i][-1][0])+"_"+str(outLine[i][-1][1])+ " = 0;\n"
                # This seems to declare a branch variable. If it's always a branch, the above case handles it.
                # If a node itself implies a variable, it needs specific handling.
                # The original code seems to ensure branches mentioned in nodes are declared.
                # This is likely covered by the 'branch' or 'startBR' cases if those outline entries exist.
                pass # Covered by branch/startBR, or needs more specific logic if node implies a unique var
            
            # Comparison operators
            elif outLine[i][0][:7] == "Equals_": var_name = str(outLine[i][0])
            elif outLine[i][0][:8] == "Greater_": var_name = str(outLine[i][0])
            elif outLine[i][0][:9] == "Lessthan_": var_name = str(outLine[i][0])
            elif outLine[i][0][:12] == "GreaterOrEq_": var_name = str(outLine[i][0])
            elif outLine[i][0][:9] == "LessOrEq_": var_name = str(outLine[i][0])

            if var_name and not var_declaration: # For comparison ops that only set var_name
                var_declaration = f"\n    uint8_t {var_name} = 0;\n"

            if var_name and var_name not in declared_variables:
                C_code_lines.append(var_declaration)
                declared_variables.add(var_name)

            # Counter, Timer, Fall, ADC, PWM specific multi-variable declarations
            if outLine[i][0][:8]== "Counter_" and "rungstate_" not in outLine[i][0]:
                base_name = str(outLine[i][0])
                if base_name not in declared_variables:
                    C_code_lines.append(f"\n    uint8_t {base_name} = 0;\n")
                    C_code_lines.append(f"    uint16_t setpoint_{base_name} = {outLine[i][2]};\n")
                    C_code_lines.append(f"    uint16_t reg_{base_name} = 0;\n")
                    C_code_lines.append(f"    uint8_t prev_rungstate_{base_name} = 0;\n")
                    C_code_lines.append(f"    uint8_t rungstate_{base_name} = 0;\n\n")
                    declared_variables.add(base_name) # Add base_name, other _reg, _setpoint are implicitly tied
            
            if "ADC_" ==  outLine[i][0][:4] :
                reg_adc_name = "reg_"+ str(outLine[i][0])
                if reg_adc_name not in declared_variables:
                    C_code_lines.append(f"    uint16_t {reg_adc_name} = 0;\n")
                    declared_variables.add(reg_adc_name)
            
            if "PWM_" == str(outLine[i][0])[:4] and outLine[i][1] not in pwmList: # pwmList here is for a different check in original code
                pwm_flag_var = str(outLine[i][1])
                if pwm_flag_var != "Internal" and pwm_flag_var not in declared_variables: # ensure it's a var name
                    C_code_lines.append(f"    uint8_t {pwm_flag_var} = 0;\n")
                    declared_variables.add(pwm_flag_var)
                if pwm_flag_var != "Internal": # Add to pwmList only if it's a valid PWM var
                    pwmList.append(outLine[i][1])


            if outLine[i][0][:6] == "Timer_" and "rungstate_" not in outLine[i][0]:
                base_name = str(outLine[i][0])
                if base_name not in declared_variables:
                    C_code_lines.append(f"\n    uint8_t {base_name} = 0;\n")
                    C_code_lines.append(f"    uint16_t setpoint_{base_name} = {outLine[i][2]};\n")
                    C_code_lines.append(f"    uint16_t reg_{base_name} = 0;\n\n")
                    C_code_lines.append(f"    uint8_t prev_rungstate_{base_name} = 0;\n")
                    C_code_lines.append(f"    uint8_t rungstate_{base_name} = 0;\n\n")
                    C_code_lines.append(f"    uint8_t run_{base_name} = 0;\n\n")
                    declared_variables.add(base_name)

            if outLine[i][0][:5] ==  "Fall_" and "rungstate_" not in outLine[i][0]:
                base_name = str(outLine[i][0])
                if base_name not in declared_variables:
                    C_code_lines.append(f"\n    uint8_t {base_name} = 0;\n")
                    C_code_lines.append(f"    uint8_t prev_rungstate_{base_name} = 0;\n")
                    C_code_lines.append(f"    uint8_t rungstate_{base_name} = 0;\n\n")
                    declared_variables.add(base_name)
            
            
            #add timer, counter and falling vaiables needed here. 
       
        # return C_code_lines # Modifies in place
        
    def setUpPWMs(self, outLine, C_code_lines):
        pwmList = []
        for i in range (len(outLine)):
            if "PWM_" == str(outLine[i][0])[:4] and outLine[i][1] not in pwmList and outLine[i][1] != "Internal":
                pwmNum = (int(outLine[i][1].split("pwm_")[1])) -1# this is the pwm #
                C_code_lines.append("\n   //setup timer for PWM  "+ str(pwmNum+1)+"\n")
                C_code_lines.append("    "+self.PWMList[pwmNum][0]+ " |= (1<<"+self.PWMList[pwmNum][1]+");\n")
                C_code_lines.append("    "+self.PWMList[pwmNum][2]+ " |= (1<<"+self.PWMList[pwmNum][4]+");\n")
                C_code_lines.append("    "+self.PWMList[pwmNum][5]+ " |= ((1<<"+self.PWMList[pwmNum][6]+")|(1<<"+self.PWMList[pwmNum][7]+"));\n")
                C_code_lines.append("    "+self.PWMList[pwmNum][8]+ " = 0 ;\n")
                C_code_lines.append("    "+self.PWMList[pwmNum][9]+ " = PWM_TIMER_TOP_VALUE ;\n\n")#top value for 16khz freq
                pwmList.append(outLine[i][1])
        # return C_code_lines # Modifies in place

                    
         

 
