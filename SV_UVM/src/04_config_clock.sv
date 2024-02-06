`timescale 1ns / 1ps

module tb();
  
  reg clk   = 0;
  reg clk50 =0;
  
  always #5 clk = ~clk; // 100MHz
  
  task calc (input real freq_hz, input real duty_cycle, input real phase, output real pout, output real ton, output real toff);
    ton = (1.0 / freq_hz) * duty_cycle * 1000_000_000;
    toff = (1000_000_000 / freq_hz) - ton;
  endtask

  task clkgen(input real phase, input real ton, input real toff);
    @(posedge clk);
    #phase
    while(1) begin
      clk50 = 1;
      #ton;
      clk50 = 0;
      #toff;
    end
  endtask
  
  real pout;
  real ton;
  real toff;
  
  initial begin
    calc(100_000_000, 0.1, 5, pout, ton, toff);
    clkgen(5, ton, toff);
  end
  
  initial begin
    #200;
    $finish();
  end
  
  initial begin;
    $dumpfile("dump.vcd");
    $dumpvars();
  end
endmodule