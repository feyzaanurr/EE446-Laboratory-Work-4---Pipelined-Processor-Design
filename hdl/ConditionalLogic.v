module ConditionalLogic(
	input [3:0] Cond,
	input [3:0] ALUFlags,
	input [1:0] FlagW,
	input PCS, Branch,
	input RegW, MemW,
	input clk,
	output PCWrite, RegWrite, MemWrite,
	output ALU_CI);
	
wire [1:0] FlagWrite;
reg [3:0] Flags;
wire CondEx;

ConditionCheck conditionCheck(
	.Cond(Cond),
	.Flags(Flags),			
	.CondEx(CondEx));
	
assign FlagWrite[1] = FlagW[1] & CondEx;
assign FlagWrite[0] = FlagW[0] & CondEx;
assign PCWrite = (PCS & CondEx) | (Branch & CondEx);
assign RegWrite = RegW & CondEx;
assign MemWrite = MemW & CondEx;
assign ALU_CI = Flags[1];			//ALU Carry In

		
always @ (posedge clk)
begin
	if(FlagWrite[1])
	begin
		Flags[3:2] <= ALUFlags[3:2];
	end
	
	if(FlagWrite[0])
	begin
		Flags[1:0] <= ALUFlags[1:0];
	end
	
end		
		
endmodule 