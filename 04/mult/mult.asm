// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Mult.asm

// Multiplies R0 and R1 and stores the result in R2.
// (R0, R1, R2 refer to RAM[0], RAM[1], and RAM[2], respectively.)

@R0
D=M
@R1
D=M
@COUNT
M=D
@R2
M=0

//Decrementing counter
(LOOP)
@COUNT
D=M
@END
D;JEQ
@COUNT
M=D-1

//Incrementing
@R0 // ex 3
D=M 
@R2
M=D+M
@LOOP
0;JMP

(END)
@END
0;JMP






