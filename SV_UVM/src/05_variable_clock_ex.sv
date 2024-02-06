`timescale 1ns / 1ps

module tb();

    reg clk = '0';

  task cacl_times(input real period, input real duty_cycle, output real time_on, output real time_off);
        time_on = period * duty_cycle;
        time_off = period - time_on;
    endtask

  task clkgen(input real time_on, input real time_off);
        while(1) begin
            #time_off;
            clk = 1;
            #time_on;
            clk = 0;
        end
    endtask

    real time_on;
    real time_off;
  
    initial begin
      cacl_times(10, 0.2, time_on, time_off);
        clkgen(time_on, time_off);
    end

    initial begin
        #200;
        $finish();
    end

    initial begin
        $dumpfile("dump.vcd");
        $dumpvars();
    end
endmodule