library verilog;
use verilog.vl_types.all;
entity ConditionalLogic_vlg_sample_tst is
    port(
        ALUFlags        : in     vl_logic_vector(3 downto 0);
        Branch          : in     vl_logic;
        Cond            : in     vl_logic_vector(3 downto 0);
        FlagW           : in     vl_logic_vector(1 downto 0);
        MemW            : in     vl_logic;
        PCS             : in     vl_logic;
        RegW            : in     vl_logic;
        clk             : in     vl_logic;
        rst             : in     vl_logic;
        sampler_tx      : out    vl_logic
    );
end ConditionalLogic_vlg_sample_tst;
