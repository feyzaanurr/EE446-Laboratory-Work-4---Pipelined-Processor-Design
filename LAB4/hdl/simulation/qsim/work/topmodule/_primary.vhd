library verilog;
use verilog.vl_types.all;
entity topmodule is
    port(
        clk             : in     vl_logic;
        rst             : in     vl_logic;
        PC_out          : out    vl_logic_vector(31 downto 0);
        RD1             : out    vl_logic_vector(31 downto 0);
        RD2             : out    vl_logic_vector(31 downto 0);
        Inst            : out    vl_logic_vector(31 downto 0);
        REGWr           : out    vl_logic;
        PCSrcM          : out    vl_logic;
        ALUCnt          : out    vl_logic_vector(3 downto 0);
        ALUOutW         : out    vl_logic_vector(31 downto 0);
        ReadDataW       : out    vl_logic_vector(31 downto 0);
        CondE           : out    vl_logic_vector(3 downto 0);
        ALUFlags_w      : out    vl_logic_vector(3 downto 0);
        FlagWriteD      : out    vl_logic_vector(1 downto 0);
        FlagWriteE      : out    vl_logic_vector(1 downto 0);
        condEx          : out    vl_logic;
        Flags           : out    vl_logic_vector(3 downto 0);
        FlagWrite       : out    vl_logic_vector(1 downto 0)
    );
end topmodule;
