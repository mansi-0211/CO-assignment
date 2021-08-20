
import sys

global var_list
var_list=[]

global label_list
label_list=[]

global Error
Error =0

global register
register={"R0":"0000", "R1" :"0000" ,"R2" : "0000", "R3" : "0000", "R4" : "0000", "R5": "0000","R6" :"0000","FLAGS": "0000000000000000"}

def assembly_to_binary(l,c):
    global var_list
    global register
    global Error
    global label_list
    bin_=""
    
    FLAG = "0000000000000000"
    

    line = list(map(str ,l.split()))
    
    
    for i in c:
        if i=="hlt" and c.index(i)!= len(c)-1:
            Error=1
            return("hlt not being used as the last instruction")
    if "hlt" in c and c.index("hlt")!=len(c)-1:
        Error=1
        return("missing hlt statement")
    
    if "FLAGS" in line and "mov" not in line :
        Error =1
        return("illegal use of flags")
    key_values=[]   
    dictionary = {"R0":"000", "R1" : "001" ,"R2" : "010", "R3" : "011", "R4" : "100", "R5": "101","R6" : "110","FLAGS": "111"}
    for k in dictionary.keys():
        key_values.append(k)
    
    type_A = ["add","sub","mul","xor","or","and"]
    type_B = ["mov","rs","ls"]
    type_C = ["mov","div","not","cmp"]
    type_D = ["ld","st"]
    type_E = ["jmp","jlt","jgt","je"]
    type_F = ["hlt"]
    
    type_=type_A+type_B+type_C+type_D+type_E+type_F
    
    if (type_A.count(line[0]) > 0):
  
        if len(line)<4 :
            Error =1
            return("General Syntax Error")
        
        if (line[0] == "add"):
            bin_ = "00000"
            
            if len(register)!=0:
                register[line[1]]= int(register[line[2]])+int(register[line[3]])
                
                if int(register[line[1]])>255:
                    register[line[1]]=0
                    register[FLAG] = "0000000000001000"
                    
                
        elif(line[0] == "sub"):
            bin_ = "00001"
            
            if len(register)!=0:
                register[line[1]]= int(register[line[2]])- int(register[line[3]])
                 
                if int(register[line[1]])<0:
                    register[line[1]]=0
                    register[FLAG] = "0000000000001000"
                    
                
        elif(line[0] == "mul"):
            bin_ = "00110"
            
            if len(register)!=0:
                register[line[1]]= int(register[line[2]]) *int( register[line[3]])
                 
                if register[line[1]]>255:
                    register[line[1]]=0
                    register[FLAG]= "0000000000001000"
                    
                
        elif(line[0] == "xor"):
            bin_ = "01010"
        elif(line[0] == "or"):
            bin_ = "01011"
        elif(line[0] == "and"):
            bin_ = "01100"
        
            
            
        bin_ = bin_ + "00"
        if (key_values.count(line[1])>0 and key_values.count(line[2])>0 and key_values.count(line[3])>0): 
            bin_  = bin_ + dictionary[line[1]]
            bin_  = bin_ + dictionary[line[2]]
            bin_ = bin_ + dictionary[line[3]]
            
       
    elif (type_B.count(line[0]) > 0 and line[2] not in key_values):
   
        if(line[0] == "mov" and key_values.count(line[2]) == 0):
            bin_ = "00010"
            register[line[1]]=int(line[2][1:])
            
        elif(line[0] == "rs"):
            
            bin_ = "01000"
        elif(line[0] == "ls"):
            bin_ = "01001"
       
           
        else:
            Error =1
            return("General Syntax Error")
        
            
        
        bin_  = bin_ + dictionary[line[1]]
       
        a = int(line[2][1:])
  
        if (0 <= a <= 255): 
            bnr = bin(a).replace('0b','')
            x = bnr[::-1]
            while len(x) < 8:
                
                x += '0'
            bnr = x[::-1]
            bnr = str(bnr)
            bin_ = bin_ + bnr
         
        
        else:
            Error =1
            return("Illegal Immediate values")
            
        
        
    elif (type_C.count(line[0]) > 0):

        if(line[0] == "mov" and key_values.count(line[2]) == 1 ):
            bin_ = "00011"
            register[line[1]]=register[line[2]]
            
        elif(line[0] == "div"):
            bin_ = "00111"
        elif(line[0] == "not"):
            bin_ = "01101"
        elif(line[0] == "cmp"):
            bin_ = "01110"
            
            if int(register[line[1]]) > int(register[line[2]]):
                register[FLAG] = "0000000000000010"
                
            if int(register[line[1]]) < int(register[line[2]]):
                register[FLAG] = "0000000000000100"
              
            if int(register[line[1]]) > int(register[line[2]]):
                register[FLAG] = "0000000000000001"     
                
        
        bin_  = bin_ + "00000"
        bin_  = bin_ + dictionary[line[1]]
        bin_  = bin_ + dictionary[line[2]]
        
    elif (type_D.count(line[0]) > 0):
        if(line[0] == "ld"):
            bin_ = "00100"
            
            if(line[2] not in var_list ):
                Error =1
                return("Use of undefined variables")
            
        elif(line[0] == "st"):
            bin_ = "00101"
            if(line[2] not in var_list ):
                Error =1
                return("Use of undefined variables")
            
        bin_  = bin_ + dictionary[line[1]]
        mem_ad=str(bin(len(c)-1))
        mem_ad = mem_ad[2:]
        x = mem_ad[::-1]
        while len(x) < 8:
            x += '0'
        mem_ad = x[::-1]
        
        bin_  = bin_ + str(mem_ad)
        

        
    elif (type_E.count(line[0]) > 0):
      
        if(line[0] == "jmp"):
            bin_ = "011111"
        elif(line[0] == "jlt"):
            bin_ = "10000"
        elif(line[0] == "jgt"):
            bin_ = "10001"
        elif(line[0] == "je"):
            bin_ = "10010"
            
        bin_  = bin_ + "000"
 
       
        for i in c:
           
            
            if i[4:] == line[1] and line[0]!="je":
                
                mem_ad=str(bin(c.index(i)))
                mem_ad=mem_ad[2:]
                x = mem_ad[::-1]
                while len(x) < 8:
                    x += '0'
                mem_ad = x[::-1]
                bin_  = bin_ + mem_ad
                
        
                
        
    elif (type_F.count(line[0]) > 0):
        bin_ = "10011"
        bin_  = bin_ + ("0" * 11)
    
    
    
    
    
    elif (line[0][-1] == ":"):
        if type_.count(line[0][:-1]) > 0 :
            Error = 1
            return("Command name has been used as the name of label")
        elif (label_list.count(line[0][:-1]) > 0):
            Error = 1
            return("A label has already been assigned by this name")
    
        else:
            label_list.append(line[0][:-1])
            l2 = ""
            for i in line[1:]:
                l2 = l2 + i + " "
            return(assembly_to_binary(l2,c))
       
    
    
    
    return (bin_)
    
    
    


code=[]
while True :
    try:
        i=input()
       
        if len(i)!=0:
             code.append(i)
    except EOFError:
        break
    









for command in code:
    if command != "hlt":
        
        command=command[:-1]
   





for command in code:
    print(assembly_to_binary(command, code))
    
    
    if Error == 1:
        temp=assembly_to_binary(command, code)
        print(temp)
        break