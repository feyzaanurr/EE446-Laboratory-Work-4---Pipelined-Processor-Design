import random
import warnings

import cocotb
from cocotb.clock import Clock
from cocotb.triggers import FallingEdge
from cocotb.triggers import RisingEdge
from cocotb.triggers import Edge
from cocotb.triggers import Timer
from cocotb.binary import BinaryValue
#from cocotb.regression import TestFactory


"""
MOV R0, #0              ;number zero
MOV R5, #0              ;keeps sum
MOV R1, #16             ;keeps number of cycles
MOV R2, #1              ;necessary for and op
LDR R3, [R0, #52]       ;number
loop: AND R4, R2, R3    ;find lsb
ADD R5, R5, R4          ;sum
ADD R3, R0, R3, shr #1  ;shift number        
SUBS R1, R1, #1         ;decrease counter
BNE loop
AND R5, R5, R2          ;return value, lsb of sum
ADD R5, R0, R5          ; to show value
; fill with zero
; put number
"""

"""
0000A0E3
0050A0E3
1010A0E3
0120A0E3
343090E5
034002E0
045085E0
A33080E0
011051E2
FAFFFF1A        
025005E0
055080E0
"""

# number = 00005201             #16bit number
number = 0x00005201
# binary 00000000000000000101001000000001
summ = 4
result = 0

@cocotb.test()
async def parity_test(dut):
    #start the clock
    await cocotb.start(Clock(dut.clk, 10, 'us').start(start_high=False))
    #set clkedge as the FallingEdge for triggers
    clkedge = RisingEdge(dut.clk)
    dut.run.value = 1             # enable PC
    await clkedge
    # reset PC and RegFile
    dut.rst.value = 1
    await clkedge
    await clkedge
    dut.rst.value = 0
    assert dut.PC_out.value == 0
    assert dut.Inst.value == 0
    #await clkedge
    # starts operation
    # MOV R0, #0
    # fetch
    await clkedge
    assert dut.PC_out.value == 0
    await clkedge
    # decode
    print ("dut.state_out.value", dut.state_out.value)
    await clkedge
    # ExecuteI
    await clkedge
    # ALUWB
    assert dut.REGWr.value == 1 
    r0 = 0
    await clkedge
    # MOV R5, #0
    # fetch
    await clkedge
    # decode
    print ("dut.state_out.value", dut.state_out.value)
    await clkedge
    # ExecuteI
    await clkedge
    # ALUWB
    assert dut.REGWr.value == 1 
    r5 = 0
    await clkedge
    #MOV R1, #16 
    # fetch
    await clkedge
    # decode
    print ("dut.state_out.value", dut.state_out.value)
    await clkedge
    # ExecuteI
    await clkedge
    # ALUWB
    assert dut.REGWr.value == 1 
    r1 = 16
    await clkedge
    # MOV R2, #1
    # fetch
    await clkedge
    # decode
    print ("dut.state_out.value", dut.state_out.value)
    await clkedge
    # ExecuteI
    await clkedge
    # ALUWB
    assert dut.REGWr.value == 1 
    r2 = 1 
    await clkedge
    # LDR R3, [R0, #52] 
    # fetch
    print("dut.Inst.value",dut.Inst.value)
    await clkedge
    # decode
    print("dut.Inst.value",dut.Inst.value)
    await clkedge
    # memAdr 
    print ("dut.state_out.value", dut.state_out.value)
    assert dut.RD1.value == r0
    assert dut.REGWr.value == 0
    await clkedge
    # memread
    await clkedge
    # memWB
    print ("dut.state_out.value", dut.state_out.value)
    print("dut.Inst.value",dut.Inst.value)
    assert dut.REGWr.value == 1
    r3 = number
    await clkedge
    for i in range(16):
        print("Cycle ", i)
        # loop: AND R4, R2, R3
        # fetch
        await clkedge
        # decode
        print("dut.PC_out.value", int(dut.PC_out.value))
        await clkedge
        # ExecuteI 
        print ("executeR dut.state_out.value", dut.state_out.value)
        print("r2",r2,"dut.RD1.value", int(dut.RD1.value),"r3",r3, "dut.RD2.value",int(dut.RD2.value))
        assert dut.RD1.value == r2                 #????????????????????
        assert dut.RD2.value == r3                 #????????????????????
        await clkedge
        # ALUWB
        print("r2",r2,"dut.RD1.value", int(dut.RD1.value),"r3",r3, "dut.RD2.value",int(dut.RD2.value))
        r4 = r2 & r3
        print ("aluwb dut.state_out.value", dut.state_out.value)
        print("dut.PC_out.value", int(dut.PC_out.value))
        await clkedge
        # ADD R5, R5, R4 
        # fetch
        await clkedge
        # decode
        await clkedge
        # ExecuteI 
        print ("executeI dut.state_out.value", dut.state_out.value)
        print("r5",r5,"dut.RD1.value", int(dut.RD1.value),"r4",r4, "dut.RD2.value",int(dut.RD2.value))
        assert dut.RD1.value == r5                 #????????????????????
        assert dut.RD2.value == r4                 #????????????????????
        await clkedge
        # ALUWB
        print("r5",r5,"dut.RD1.value", int(dut.RD1.value),"r4",r4, "dut.RD2.value",int(dut.RD2.value))
        r5 = r5 + r4
        print ("aluwb dut.state_out.value", dut.state_out.value)
        await clkedge
        # ADD R3, R0, R3, shr #1
        # fetch
        await clkedge
        # decode
        await clkedge
        # ExecuteI 
        print ("executeI dut.state_out.value", dut.state_out.value)
        print("r0",r0,"dut.RD1.value", int(dut.RD1.value),"r3",r3, "dut.RD2.value",int(dut.RD2.value))
        assert dut.RD1.value == r0                 #????????????????????
        assert dut.RD2.value == r3                 #????????????????????
        await clkedge
        # ALUWB
        print("r0",r0,"dut.RD1.value", int(dut.RD1.value),"r3",r3, "dut.RD2.value",int(dut.RD2.value))
        r3 = (r3 >> 1)
        print ("aluwb dut.state_out.value", dut.state_out.value)
        await clkedge
        #SUB R1, R1, #1 
        # fetch
        await clkedge
        # decode
        await clkedge
        # ExecuteI 
        print ("executeI dut.state_out.value", dut.state_out.value)
        print("r1",r1,"dut.RD1.value", int(dut.RD1.value))
        print("dut.PC_out.value", int(dut.PC_out.value))
        assert dut.RD1.value == r1                 #????????????????????
        await clkedge
        # ALUWB
        print("r1",r1,"dut.RD1.value", int(dut.RD1.value))
        r1 = r1 - 1
        print ("aluwb dut.state_out.value", dut.state_out.value)
        await clkedge
        # BNE loop
        # fetch
        print ("fetch dut.state_out.value", dut.state_out.value)
        await clkedge
        print (" decode dut.state_out.value", dut.state_out.value)
        print("dut.PC_out.value", int(dut.PC_out.value))
        # decode
        await clkedge
        print ("branch_s dut.state_out.value", dut.state_out.value)
        # branch_s 
        await clkedge
        print ("dut.state_out.value", dut.state_out.value)
        
    print("traverse completed")
    # AND R5, R5, R2 
    # fetch
    await clkedge
    # decode
    print("dut.PC_out.value", int(dut.PC_out.value))
    await clkedge
    # ExecuteI 
    print ("executeR dut.state_out.value", dut.state_out.value)
    print("r5",r5,"dut.RD1.value", int(dut.RD1.value),"r2",r2, "dut.RD2.value",int(dut.RD2.value))
    assert dut.RD1.value == r5                 #????????????????????
    assert dut.RD2.value == r2                 #????????????????????
    assert dut.RD1.value == summ 
    await clkedge
    # ALUWB
    print("r2",r2,"dut.RD1.value", int(dut.RD1.value),"r3",r3, "dut.RD2.value",int(dut.RD2.value))
    r5 = r5 & r2
    print ("aluwb dut.state_out.value", dut.state_out.value)
    print("dut.PC_out.value", int(dut.PC_out.value))
    await clkedge
    #ADD R5, R0, R5
    # fetch
    await clkedge
    # decode
    await clkedge
    # ExecuteI 
    print ("executeI dut.state_out.value", dut.state_out.value)
    print("r0",r0,"dut.RD1.value", int(dut.RD1.value),"r5",r5, "dut.RD2.value",int(dut.RD2.value))
    assert dut.RD1.value == r0                 #????????????????????
    assert dut.RD2.value == r5                 #????????????????????
    assert dut.RD2.value == result
    await clkedge
    # ALUWB
    print("subroutine completed")
        
        
        