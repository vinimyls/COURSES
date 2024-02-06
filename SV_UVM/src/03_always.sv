`timescale 1ns / 1ps


module tb();

    reg clk;
    reg clk50;
    reg clk25;
    reg rst;

    initial begin;
        clk   = 1'b0;
        clk50 = 1'b0;
        clk25 = 1'b0;
        rst   = 1'b0;
    end

    always #5  clk   = ~clk;
    always #10 clk50 = ~clk50;
    always #20 clk25 = ~clk25;

    initial begin;
        $dumpfile("dump.vcd");
        $dumpvars;
    end

    initial begin
        #200;
        $finish;
    end

endmodule;