library verilog;
use verilog.vl_types.all;
entity ConditionalLogic_vlg_check_tst is
    port(
        ALU_CI          : in     vl_logic;
        CondEx          : in     vl_logic;
        FlagWrite_w     : in     vl_logic_vector(1 downto 0);
        Flags_wire      : in     vl_logic_vector(3 downto 0);
        MemWrite        : in     vl_logic;
        PCWrite         : in     vl_logic;
        RegWrite        : in     vl_logic;
        sampler_rx      : in     vl_logic
    );
end ConditionalLogic_vlg_check_tst;
