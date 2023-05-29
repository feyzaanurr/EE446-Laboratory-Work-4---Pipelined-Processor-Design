library verilog;
use verilog.vl_types.all;
entity topmodule_vlg_check_tst is
    port(
        ALUCnt          : in     vl_logic_vector(3 downto 0);
        ALUFlags_w      : in     vl_logic_vector(3 downto 0);
        ALUOutW         : in     vl_logic_vector(31 downto 0);
        CondE           : in     vl_logic_vector(3 downto 0);
        FlagWrite       : in     vl_logic_vector(1 downto 0);
        FlagWriteD      : in     vl_logic_vector(1 downto 0);
        FlagWriteE      : in     vl_logic_vector(1 downto 0);
        Flags           : in     vl_logic_vector(3 downto 0);
        Inst            : in     vl_logic_vector(31 downto 0);
        PCSrcM          : in     vl_logic;
        PC_out          : in     vl_logic_vector(31 downto 0);
        RD1             : in     vl_logic_vector(31 downto 0);
        RD2             : in     vl_logic_vector(31 downto 0);
        REGWr           : in     vl_logic;
        ReadDataW       : in     vl_logic_vector(31 downto 0);
        condEx          : in     vl_logic;
        sampler_rx      : in     vl_logic
    );
end topmodule_vlg_check_tst;
