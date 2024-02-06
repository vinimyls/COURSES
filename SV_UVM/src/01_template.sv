`timescale 1ns / 1ps

module tb();

  // floval signals clk, rst
  reg clk;
  reg rst;
  reg [3:0] temp;
  
  // initialized global variable
  initial begin
    clk = 1'b0;
    rst = 1'b0;
  end
  
  // random signal for data/control
  initial begin
    rst = 1'b1;
    #30;
    rst = 1'b0;
  end
  
  initial begin
    temp = 4'b0100;
    #10;
    temp = 4'b1100;
    #10;
    temp = 4'b0011;
  	#10;
  end
  
  // system task at the start of simulation
  initial begin
    $dumpfile("dump.vcd");
    $dumpvars();
  end
  
  // analyzing values of variable on console
  initial begin
    $monitor("Temp: %0d at time %0t", temp, $time);
  end
  
  // stop simulation
  initial begin
    #200;
    $finish();
  end  
endmodule