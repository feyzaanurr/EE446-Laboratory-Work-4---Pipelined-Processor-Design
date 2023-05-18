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
MOV R3, #0x3C       ;initial memory address for length and elements
MOV R0, #0          ;number zero
MOV R2, #0          ;keeps sum
LDR R1, [R3]        ;read from memory location 0x3A, keeps number of elements
NOP (MOV R0, #0 )
NOP (MOV R0, #0 )
L1: CMP R1, R0
BEQ store
NOP (MOV R0, #0 )
NOP (MOV R0, #0 )
NOP (MOV R0, #0 )
NOP (MOV R0, #0 )
ADD R3, #4
SUB R1, #1
NOP (MOV R0, #0 )
LDR R4, [R3]
NOP (MOV R0, #0 )
NOP (MOV R0, #0 )
ADDS R2, R2, R4
B L1
NOP (MOV R0, #0 )
NOP (MOV R0, #0 )
NOP (MOV R0, #0 )
NOP (MOV R0, #0 )
store: STR R2, [R3, #4]     ;R2 gives array sum 
NOP (MOV R0, #0 )
NOP (MOV R0, #0 )
done: B done
"""

"""
not yet modified 
0000A0E3
0020A0E3
3C30A0E3
001093E5
000051E1
0400000A
043083E2
011041E2
004093E5
042092E0
F8FFFFEA
042083E5
FEFFFFEA
"""



@cocotb.test()
async def arrays_sum_test(dut):
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
    #print("dut.Inst.value",dut.Inst.value)
    #assert dut.Inst.value == 0
    assert dut.PC_out.value == 0
    await clkedge
    # decode
    #assert dut.PC_out.value == 4
    print ("dut.state_out.value", dut.state_out.value)
    await clkedge
    # ExecuteI
    await clkedge
    # ALUWB
    #assert dut.REGWr.value == 1 
    r0 = 0
    await clkedge
    # MOV R2, #0
    # fetch
    await clkedge
    # decode
    #assert dut.PC_out.value == 8
    await clkedge
    # ExecuteI 
    await clkedge
    # ALUWB
    #assert dut.REGWr.value == 1 
    r2 = 0
    await clkedge
    # MOV R3, #0x3C 
    # fetch
    print ("dut.state_out.value", dut.state_out.value)
    await clkedge
    # decode
    #assert dut.PC_out.value == 12
    await clkedge
    # ExecuteI 
    await clkedge
    # ALUWB
    #assert dut.REGWr.value == 1 
    r3 = 0x3C           # decimal 60
    await clkedge
    # LDR R1, [R3] 
    # fetch
    print("dut.Inst.value",dut.Inst.value)
    await clkedge
    # decode
    #assert dut.PC_out.value == 16
    print("dut.Inst.value",dut.Inst.value)
    await clkedge
    # memAdr 
    print ("dut.state_out.value", dut.state_out.value)
    assert dut.RD1.value == r3
    assert dut.REGWr.value == 0
    await clkedge
    # memread
    await clkedge
    # memWB
    print ("dut.state_out.value", dut.state_out.value)
    #print("dut.data_out.value", dut.data_out.value)
    #print("dut.ResultS.value",dut.ResultS.value)
    print("dut.Inst.value",dut.Inst.value)
    #print ("dut.state_out.value", dut.state_out.value)
    assert dut.REGWr.value == 1 
    assert dut.ResultS.value == 1           #should be 1????????????
    #print("dut.ResultS.value",dut.ResultS.value)
    r1 = 3
    
    
    for i in range(r1):
        print("Cycle ", i)
        await clkedge
        #L1: CMP R1, R0
        #assert dut.REGWr.value == 0 
        # fetch
        print ("fetch dut.state_out.value", dut.state_out.value)
        await clkedge
        # decode
        #assert dut.PC_out.value == 20
        print("dut.PC_out.value", int(dut.PC_out.value))
        print ("decode dut.state_out.value", dut.state_out.value)
        await clkedge
        # executeR 
        print("dut.Inst.value",hex(dut.Inst.value))   
        print ("executeR dut.state_out.value", dut.state_out.value)
        print("r1", r1, "dut.RD1.value", int(dut.RD1.value),"r0", r0, "dut.RD2.value", int(dut.RD2.value))
        assert dut.RD1.value == r1
        assert dut.RD2.value == r0
        print("dut.PC_out.value", int(dut.PC_out.value))
        #await clkedge
        print ("unknown dut.state_out.value", dut.state_out.value)
        print("dut.Inst.value",hex(dut.Inst.value)) 
        print("r1", r1, "dut.RD1.value", int(dut.RD1.value),"r0", r0, "dut.RD2.value", int(dut.RD2.value))
        assert dut.RD1.value == r1
        assert dut.RD2.value == r0
        await clkedge
        
        # BEQ store
        # fetch
        print("dut.Inst.value",hex(dut.Inst.value)) 
        print ("fetch dut.state_out.value", dut.state_out.value)
        await clkedge
        # decode
        print("dut.Inst.value",hex(dut.Inst.value)) 
        print ("decode dut.state_out.value", dut.state_out.value)
        await clkedge
        # branch_s 
        print("dut.Inst.value",hex(dut.Inst.value))
        print ("branch_s dut.state_out.value", dut.state_out.value)
        await clkedge
        
        # ADD R3, #4
        # fetch
        print ("fetch dut.state_out.value", dut.state_out.value)
        print("dut.Inst.value",hex(dut.Inst.value))
        print("dut.PC_out.value", int(dut.PC_out.value))
        #assert dut.PC_out.value == 24
        await clkedge
        # decode
        print("dut.Inst.value",hex(dut.Inst.value))
        print ("decode dut.state_out.value", dut.state_out.value)
        await clkedge
        # ExecuteI 
        print("dut.Inst.value",hex(dut.Inst.value))
        assert dut.RD1.value == r3
        print ("executeI dut.state_out.value", dut.state_out.value)
        await clkedge
        # ALUWB
        r3 = r3 + 4
        print ("aluwb dut.state_out.value", dut.state_out.value)
        await clkedge
        # SUB R1, #1
        #fetch
        #assert dut.PC_out.value == 28
        print ("fetch dut.state_out.value", dut.state_out.value)
        await clkedge
        # decode
        print ("decode dut.state_out.value", dut.state_out.value)
        await clkedge
        # ExecuteI 
        print("dut.Inst.value", hex(dut.Inst.value))
        print("r1=", r1, ",r3=", r3, ",dut.RD1.value=", int(dut.RD1.value))
        print ("executeI dut.state_out.value", dut.state_out.value)
        #assert dut.RD1.value == r1
        await clkedge
        print("r1=", r1, ",r3=", r3, ",dut.RD1.value=", int(dut.RD1.value))
        #assert dut.RD1.value == r1             # ?????????????????????????
        print ("aluwb dut.state_out.value", dut.state_out.value)
        # ALUWB
        r1 = r1 - 1
        await clkedge
        # LDR R4, [R3]
        # fetch
        print ("fetch dut.state_out.value", dut.state_out.value)
        await clkedge
        # decode
        #assert dut.PC_out.value == 32
        print ("decode dut.state_out.value", dut.state_out.value)
        await clkedge
        # memAdr 
        print("dut.Inst.value", hex(dut.Inst.value))
        print ("memadr dut.state_out.value", dut.state_out.value)
        print("r3*=", r3, ", r1=", r1, ", dut.RD1.value=", int(dut.RD1.value))
        assert dut.RD1.value == r3
        assert dut.REGWr.value == 0
        await clkedge
        # memread
        print ("memread dut.state_out.value", dut.state_out.value)
        await clkedge
        # memWB
        print ("memwb dut.state_out.value", dut.state_out.value)
        print("r3*=", r3, ", r1=", r1, ", dut.RD1.value=", int(dut.RD1.value))
        #assert dut.RD1.value == r3
        if i == 0:
            r4 = 4
        elif i == 1:
            r4 = 1
        else:
            r4 = 2
        await clkedge
        #ADDS R2, R2, R4
        # fetch
        #assert dut.PC_out.value == 36
        await clkedge
        # decode
        await clkedge
        # ExecuteI 
        print ("executeI dut.state_out.value", dut.state_out.value)
        print("r2",r2,"dut.RD1.value", int(dut.RD1.value),"r4",r4, "dut.RD2.value",int(dut.RD2.value))
        assert dut.RD1.value == r2                 #????????????????????
        assert dut.RD2.value == r4                 #????????????????????
        await clkedge
        # ALUWB
        print("r2",r2,"dut.RD1.value", int(dut.RD1.value),"r4",r4, "dut.RD2.value",int(dut.RD2.value))
        r2 = r2 + r4
        print ("aluwb dut.state_out.value", dut.state_out.value)
        await clkedge
        # B L1
        # fetch
        print ("fetch dut.state_out.value", dut.state_out.value)
        await clkedge
        print (" decode dut.state_out.value", dut.state_out.value)
        print("dut.PC_out.value", int(dut.PC_out.value))
        # decode
        await clkedge
        print ("branch_s dut.state_out.value", dut.state_out.value)
        # branch_s 
        print("dut.PC_out.value", int(dut.PC_out.value))
        print("PC+8: dut.RD1.value=", int(dut.RD1.value))
        print("PC+8: dut.RD2.value=", int(dut.RD2.value))
        print ("dut.state_out.value", dut.state_out.value)
        
    print("traverse completed***********************")
    await clkedge
    #L1: CMP R1, R0
    #assert dut.REGWr.value == 0 
    # fetch
    print ("fetch dut.state_out.value", dut.state_out.value)
    await clkedge
    # decode
    #assert dut.PC_out.value == 20
    print("dut.PC_out.value", int(dut.PC_out.value))
    print ("decode dut.state_out.value", dut.state_out.value)
    await clkedge
    # executeR 
    print("dut.Inst.value",hex(dut.Inst.value))   
    print ("executeR dut.state_out.value", dut.state_out.value)
    print("r1", r1, "dut.RD1.value", int(dut.RD1.value),"r0", r0, "dut.RD2.value", int(dut.RD2.value))
    assert dut.RD1.value == r1
    assert dut.RD2.value == r0
    print("dut.PC_out.value", int(dut.PC_out.value))
    #await clkedge
    print ("unknown dut.state_out.value", dut.state_out.value)
    print("dut.Inst.value",hex(dut.Inst.value)) 
    print("r1", r1, "dut.RD1.value", int(dut.RD1.value),"r0", r0, "dut.RD2.value", int(dut.RD2.value))
    assert dut.RD1.value == r1
    assert dut.RD2.value == r0
    await clkedge
    
    # BEQ store
    # fetch
    print("dut.Inst.value",hex(dut.Inst.value)) 
    print ("fetch dut.state_out.value", dut.state_out.value)
    await clkedge
    # decode
    print("dut.Inst.value",hex(dut.Inst.value)) 
    print ("decode dut.state_out.value", dut.state_out.value)
    await clkedge
    # branch_s 
    print("dut.Inst.value",hex(dut.Inst.value))
    print ("branch_s dut.state_out.value", dut.state_out.value)
    await clkedge
    
    #store: STR R2, [R3, #4]
    #fetch
    print ("fetch dut.state_out.value", dut.state_out.value)
    await clkedge
    # decode
    print (" decode dut.state_out.value", dut.state_out.value)
    print("dut.PC_out.value", int(dut.PC_out.value))
    await clkedge
    # memadr
    print("dut.Inst.value", hex(dut.Inst.value))
    print ("memadr dut.state_out.value", dut.state_out.value)
    print("r3*=", r3, ", r1=", r1, ", dut.RD1.value=", int(dut.RD1.value))
    assert dut.RD1.value == r3
    assert dut.REGWr.value == 0
    # memwrite
    print ("memwrite dut.state_out.value", dut.state_out.value)
    print("r2=", r2, ", dut.RD2.value=", int(dut.RD2.value))
    assert dut.RD2.value == r2
    await clkedge