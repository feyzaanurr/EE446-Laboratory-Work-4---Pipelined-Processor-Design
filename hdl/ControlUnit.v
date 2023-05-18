module ControlUnit(
	input clk, rst, 
	input [1:0] Op, 
	input [5:0] Funct, 
	input [3:0] Rd,
	input [4:0] shamt5,
	input [1:0] sh,
	input L, 
	input [23:0] bx_inst,
	input [3:0] Cond,
	input [3:0] ALUFlags,
	output WriteSrc, ALUSrcA,
	output [1:0] ALUSrcB, ResultSrc,
	output AdrSrc, IRWrite,
	output [1:0] ImmSrc,
	output [2:0] RegSrc,	
	output [3:0] ALUControl,
	output [4:0] shamt,
	output [1:0] shiftControl,
	output PCWrite, RegWrite, MemWrite,
	output ALU_CI,
	output wire [3:0] state_out);
	
wire PCS, RegW, MemW, NextPC;
wire [1:0] FlagW;
	
Decoder_control decoder_control(
	.rst(rst), .clk(clk),
	.Op(Op), 
	.Funct(Funct), 
	.Rd(Rd),
	.shamt5(shamt5),
	.sh(sh),
	.L(L), 
	.bx_inst(bx_inst), 
	.FlagW(FlagW),
	.PCS(PCS), .RegW(RegW), .MemW(MemW),
	.ALUSrcA(ALUSrcA), .WriteSrc(WriteSrc),
	.ALUSrcB(ALUSrcB), .ResultSrc(ResultSrc),
	.AdrSrc(AdrSrc), .IRWrite(IRWrite), .NextPC(NextPC),
	.ImmSrc(ImmSrc),
	.RegSrc(RegSrc),	
	.ALUControl(ALUControl),
	.shamt(shamt),
	.shiftControl(shiftControl),
	.state_out(state_out));
	
ConditionalLogic conditionalLogic(
	.Cond(Cond),
	.ALUFlags(ALUFlags),
	.FlagW(FlagW),
	.PCS(PCS), .RegW(RegW), .MemW(MemW), .NextPC(NextPC),
	.clk(clk),
	.PCWrite(PCWrite), .RegWrite(RegWrite), .MemWrite(MemWrite),
	.ALU_CI(ALU_CI));
	
endmodule 