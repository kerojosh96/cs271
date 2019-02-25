// This file is part of www.nand2tetris.org
// and the book "The Elements of Computing Systems"
// by Nisan and Schocken, MIT Press.
// File name: projects/04/Fill.asm

// Runs an infinite loop that listens to the keyboard input.
// When a key is pressed (any key), the program blackens the screen,
// i.e. writes "black" in every pixel;
// the screen should remain fully black as long as the key is pressed. 
// When no key is pressed, the program clears the screen, i.e. writes
// "white" in every pixel;
// the screen should remain fully clear as long as no key is pressed.

// Put your code here.
 // A stores location and M stores Value

(RESTART)
@SCREEN // is a number like 18903 somthing 
D=A             // loads 18900 into D
@Location                                   // is a varible 
M=D            // Stores the value of SCREEN in Memory
(LOOP)
@KBD          
D=A           // loads keybord input into D
@Location     
D=D-M         // This subtracts the keybord from location
@RESTART      
D;JEQ         // RESTARTs the loop
@Location    
A=M          
M=0         // sets location = 0
@KBD        
D=M         // loads KBD into M
@BLACK      
D;JGT       // if less than 0 goto black


@Increment  
0;JMP       // jumps to Increment

(BLACK)
@Location
A=M      // loads location and sets Memory = A
M=-1
(Increment)
@Location // Loads Location 
M=M+1 // Increments it by 1

@LOOP
0;JMP //loops
