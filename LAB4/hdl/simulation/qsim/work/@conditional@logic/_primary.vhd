library verilog;
use verilog.vl_types.all;
entity ConditionalLogic is
    port(
        Cond            : in     vl_logic_vector(3 downto 0);
        ALUFlags        : in     vl_logic_vector(3 downto 0);
        FlagW           : in     vl_logic_vector(1 downto 0);
        PCS             : in     vl_logic;
        Branch          : in     vl_logic;
        RegW            : in     vl_logic;
        MemW            : in     vl_logic;
        clk             : in     vl_logic;
        rst             : in     vl_logic;
        PCWrite         : out    vl_logic;
        RegWrite        : out    vl_logic;
        MemWrite        : out    vl_logic;
        ALU_CI          : out    vl_logic;
        CondEx          : out    vl_logic;
        Flags_wire      : out    vl_logic_vector(3 downto 0);
        FlagWrite_w     : out    vl_logic_vector(1 downto 0)
    );
end ConditionalLogic;
