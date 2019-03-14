import sys
DestTable = {'null':'000','M':'001','D':'010','MD':'011','AM':'101','AD':'110','AND':'111','A':'100'}
JumpTable = {'null':'000','JGT':'001','JEQ':'010','JGE':'011','JLT':'100','JNE':'101','JLE':'110','JMP':'111'}
VaribleTable ={}
VCounter = 15
LabelTable ={}
FileName = sys.argv[1]
assmblyFile = open(sys.argv[1]) # fix this 
print("file name ", FileName)
hack_filename = "fixme.hack" # Initialize this based on the asm filename

assmblyLines = assmblyFile.readlines()

assmblyFile.close()

NewList =[]
RawP1 =[]
finalRaw = [] #important. this gets used a lot. 
binaryList =[]




CConst = '111'
for line in assmblyLines:
    newLine = line.replace("\n", "")
    newLine = line.strip()
    newline2 = newLine.replace(" ","")
    newline3 = line[:line.find("/")]
    newline4 = newline3.replace(" ","")
    #print(newline4)
    NewList.append(newline4)
    RawP1 = NewList
for a in RawP1:
    if (a!=""):
        finalRaw.append(a)
         
def SimpleA(InA): #whole lines gets put in here like "@12, @HELLO"
    z = 0
    x = InA[1-InA.find("@"):] # string
    print("x is:",x)
    
    if (x.isdigit()==True): #x.isupper()==False and x.islower()==False and x.find(".")==-1 and
         
        z = int(x) # this has an error
    if (x.isdigit()==False):#x.isupper()==True or x.islower()==True
        print("x is :",x)
        z=PreDefSymb(x)
        #print("sergshdfhdfghdf",z)
        if (z==123456789): # not in pre def symbol list
            print("not in PreDef Lable")
            if(x in LabelTable):
                print("here")
                z = LabelTable[x]
            else:
                global VCounter
                VCounter = VCounter +1
                LabelTable[x] = VCounter
                z = VCounter
    zz= format(z,'016b')
    return zz
   
#print("this is a test for bin: "+ SimpleA('10'))

def PreDefSymb(x):
    a = False
    if(x=="SP"):
        return 0
        a = True
    if(x=="LCL"):
        return 1
        a = True
    if(x=="ARG"):
        return 2
        a = True
    if(x=="THIS"):
        return 3
        a = True
    if(x=="THAT"):
        return 4
        a = True
    if(x=="R0"):
        return 0
        a = True
    if(x=="R1"):
        return 1
        a = True
    if(x=="R2"):
        return 2
        a = True
    if(x=="R3"):
        return 3
        a = True
    if(x=="R4"):
        return 4
        a = True
    if(x=="R5"):
        return 5
        a = True
    if(x=="R6"):
        return 6
        a = True
    if(x=="R7"):
        return 7
        a = True
    if(x=="R8"):
        return 8
        a = True
    if(x=="R9"):
        return 9
        a = True
    if(x=="R10"):
        return 10
        a = True
    if(x=="R11"):
        return 11
        a = True
    if(x=="R12"):
        return 12
        a = True
    if(x=="R13"):
        return 13
    if(x=="R14"):
        return 14
    if(x=="R15"):
        return 15
    if(x=="SCREEN"):
        return 16384
        a = True
    if(x=="KBD"):
        return 24576
        a = True
    else:
        return 123456789
    
def FirstPass(InList):
    counter = 0
    print(InList)
    for line in InList:
        
        if(line[0]=="("): 
            a =line.strip("(")
            b = a.strip(")")
            LabelTable[b] = counter
            print("this works")

        else:
            counter +=1
    print(LabelTable)

def AOrCInstruct(InList):
    for line in InList:
        if(line[0]=="@" and line[0]!="("):
           binaryList.append(SimpleA(line)+"\n")
           #print(":"+ line + ":" + " In Binary is: " + SimpleA(line))
        
        elif (line[0]!="@" and line[0]!="("): # this is the c instruction "if"
            DestHold = "000"
            CompHold = "0000000"
            JumpHold = "000"
             
            if (0==0): # If it finds an equal sign line.find("=") !=-1
                tempOnlyDest = line[:line.find("=")] 
                #print(tempOnlyDest)
                if(tempOnlyDest =="M"):
                    DestHold = DestTable['M']
                if(tempOnlyDest =="D"):
                    DestHold = DestTable['D']   
                if(tempOnlyDest =="MD"):
                    DestHold = DestTable['MD']
                if(tempOnlyDest =="A"):
                    DestHold = DestTable['A']
                if(tempOnlyDest =="AM"):
                    DestHold = DestTable['AM']
                if(tempOnlyDest =="AD"):
                    DestHold = DestTable['AD']
                if(tempOnlyDest =="AND"):
                    DestHold = DestTable['AND']
                #print(tempOnlyDest + " is what temp only dest is")

            if (line.find(";")!=-1): # has a jump command
                
                tempOnlyJump = line[1+line.find(";"):]
                #print("temp = "+tempOnlyJump)
                if(tempOnlyJump =="JGT"):
                    JumpHold = JumpTable['JGT']
                if(tempOnlyJump =="JEQ"):
                    JumpHold = JumpTable['JEQ']
                if(tempOnlyJump =="JGE"):
                    JumpHold = JumpTable['JGE']
                if(tempOnlyJump =="JLT"):
                    JumpHold = JumpTable['JLT']
                if(tempOnlyJump =="JNE"):
                    JumpHold = JumpTable['JNE']
                if(tempOnlyJump =="JLE"):
                    JumpHold = JumpTable['JLE']
                if(tempOnlyJump =="JMP"):
                    JumpHold = JumpTable['JMP']



            if (line.find("=")!=-1): #comp line.find("=")!=-1
                tempOnlyComp = line[1+line.find("="):]
                
               # print(line +" " +tempOnlyComp )
                # When a = 0 
                print("CHECK THIS LINE!!! ",tempOnlyComp)
                #........................................
                if(tempOnlyComp =="0"):
                    CompHold = '0101010'
                if(tempOnlyComp =="1"):
                    CompHold = '0111111'
                if(tempOnlyComp =='-1'):
                    CompHold = '0111010'
                if(tempOnlyComp =='D'):
                    CompHold = '0001100'
                if(tempOnlyComp =='A'):
                    CompHold = '0110000'
                if(tempOnlyComp =='!D'):
                    CompHold = '0001101'
                if(tempOnlyComp =='!A'):
                    CompHold = '0110011'
                if(tempOnlyComp =='-D'):
                    CompHold = '0001111'
                if(tempOnlyComp =='-A'):
                    CompHold = '0110011'
                if(tempOnlyComp =='D+1'):
                    CompHold = '0011111'
                if(tempOnlyComp =='A+1'):
                    CompHold = '0110111'
                if(tempOnlyComp =='D-1'):
                    CompHold = '0001110'
                if(tempOnlyComp =='A-1'):
                    CompHold = '0110010'
                if(tempOnlyComp =='D+A'):
                    CompHold = '0000010'
                if(tempOnlyComp =='D-A'):
                    CompHold = '0010011'
                if(tempOnlyComp =='A-D'):
                    CompHold = '0000111'
                if(tempOnlyComp =='A&D'):
                    CompHold = '0000000'
                if(tempOnlyComp =='D|A'):
                    CompHold = '0010101'
                
                # When a= 1
                if(tempOnlyComp =='M'):
                    CompHold = '1110000'
                    print("FOUND M")
                if(tempOnlyComp =='!M'):
                    CompHold = '1110001'
                if(tempOnlyComp =='-M'):
                    CompHold = '1110011'
                if(tempOnlyComp =='M+1'):
                    CompHold = '1110111'
                if(tempOnlyComp =='M-1'):
                    CompHold = '1110010'
                if(tempOnlyComp =='D+M'):
                    CompHold = '1000010'  
                if(tempOnlyComp =='D-M'):
                    CompHold = '1010011' 
                if(tempOnlyComp =='M-D'):
                    CompHold = '1000111' 
                if(tempOnlyComp =='D&M'):
                    CompHold = '1000000' 
                if(tempOnlyComp =='D|M'):
                    CompHold = '1010101' 
            #...............................
            #...............................
            if (line.find(";")!=-1): #comp line.find("=")!=-1
                tempOnlyComp2 = line[:1+line.find(";")-1]
                
               # print(line +" " +tempOnlyComp )
                # When a = 0 
                print("CHECK THIS LINE!!! ",tempOnlyComp2)
                #........................................
                if(tempOnlyComp2 =="0"):
                    CompHold = '0101010'
                if(tempOnlyComp2 =="1"):
                    CompHold = '0111111'
                if(tempOnlyComp2 =='-1'):
                    CompHold = '0111010'
                if(tempOnlyComp2 =='D'):
                    CompHold = '0001100'
                if(tempOnlyComp2 =='A'):
                    CompHold = '0110000'
                if(tempOnlyComp2 =='!D'):
                    CompHold = '0001101'
                if(tempOnlyComp2 =='!A'):
                    CompHold = '0110011'
                if(tempOnlyComp2 =='-D'):
                    CompHold = '0001111'
                if(tempOnlyComp2 =='-A'):
                    CompHold = '0110011'
                if(tempOnlyComp2 =='D+1'):
                    CompHold = '0011111'
                if(tempOnlyComp2 =='A+1'):
                    CompHold = '0110111'
                if(tempOnlyComp2 =='D-1'):
                    CompHold = '0001110'
                if(tempOnlyComp2 =='A-1'):
                    CompHold = '0110010'
                if(tempOnlyComp2 =='D+A'):
                    CompHold = '0000010'
                if(tempOnlyComp2 =='D-A'):
                    CompHold = '0010011'
                if(tempOnlyComp2 =='A-D'):
                    CompHold = '0000111'
                if(tempOnlyComp2 =='A&D'):
                    CompHold = '0000000'
                if(tempOnlyComp2 =='D|A'):
                    CompHold = '0010101'
                
                # When a= 1
                if(tempOnlyComp2 =='M'):
                    CompHold = '1110000'
                if(tempOnlyComp2 =='!M'):
                    CompHold = '1110001'
                if(tempOnlyComp2 =='-M'):
                    CompHold = '1110011'
                if(tempOnlyComp2 =='M+1'):
                    CompHold = '1110111'
                if(tempOnlyComp2 =='M-1'):
                    CompHold = '1110010'
                if(tempOnlyComp2 =='D+M'):
                    CompHold = '1000010'  
                if(tempOnlyComp2 =='D-M'):
                    CompHold = '1010011' 
                if(tempOnlyComp2 =='M-D'):
                    CompHold = '1000111' 
                if(tempOnlyComp2 =='D&M'):
                    CompHold = '1000000' 
                if(tempOnlyComp2 =='D|M'):
                    CompHold = '1010101' 


                
                #............................................
            
            
            binaryList.append(CConst+CompHold+DestHold+JumpHold+'\n')
            print(":"+ line + ":" + " In Binary is: " +CConst+ " " +CompHold +" " +DestHold + " " + JumpHold)
        
            
            #comp   when doing comp look for a semiccolon  and =. when there is no = sign the dest 000 
FirstPass(finalRaw)
AOrCInstruct(finalRaw)
WriteDoc = FileName[1+ FileName.find("/"):]
WriteDoc2 = WriteDoc[:WriteDoc.find(".")]
#print("hi: ", WriteDoc2)
file = open(WriteDoc2+".hack","w") 
 
#print("Hello World from Josh!")
#print(len(binaryList))
for line in binaryList:
     
    file.write(line)

file.close() 
 
print(binaryList)
# Write to a file, given the hack_filename "fixme.hack"
