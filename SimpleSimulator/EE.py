import reg_file
import memory
import PC


def execute(instruction,mem,count):
    #global mem_add
    #global count

    dictionary = {
        "000": reg_file.r0,
        "001": reg_file.r1,
        "010": reg_file.r2,
        "011": reg_file.r3,
        "100": reg_file.r4,
        "101": reg_file.r5,
        "110": reg_file.r6,
        "111": reg_file.F
    }
    
    if instruction[:5]=="00000":
        a=dictionary[instruction[7:10]]
        b=dictionary[instruction[10:13]]
        d=dictionary[instruction[13:]]
        B = reg_file.register_file.getvalue(b)
        D = reg_file.register_file.getvalue(d)
        value = reg_file.bit_16(int(D, 2) + int(B, 2))
        if ((int(D,2)+ int(B,2)) > 65535):
            reg_file.register_file.save(reg_file.F, reg_file.bit_16(8))

        reg_file.register_file.save(a, value)
    
    if (instruction[:5]=="00001"):
        a=dictionary[instruction[7:10]]
        b=dictionary[instruction[10:13]]
        d=dictionary[instruction[13:]]
        B = reg_file.register_file.getvalue(b)
        D = reg_file.register_file.getvalue(d)
        value = reg_file.bit_16(int(B, 2) - int(D, 2))
        if ((int(D,2) - int(B,2)) > 65535) or ((int(D,2) - int(B,2))< 0) :
            reg_file.register_file.save(reg_file.F, reg_file.bit_16(8))
        reg_file.register_file.save(a, value)

    if instruction[:5]=="00010": 
        b = dictionary[instruction[5:8]]
        d = instruction[8:]
        d = int(d,2)
        value = reg_file.bit_16(d)
        reg_file.register_file.save(b, value)
        

        
    if instruction[:5]=="00011":
      
        b=dictionary[instruction[10:13]]
        d=dictionary[instruction[13:]]
        D = reg_file.register_file.getvalue(d)
        reg_file.register_file.save(b, D)
        
    
    if instruction[:5]=="00100":
        
        d=dictionary[instruction[5:8]]
        value = memory.mem_value(instruction[8:],mem)
        reg_file.register_file.save(d, value)
       
    
    if instruction[:5]=="00101":
        
        d=dictionary[instruction[5:8]]
        a = reg_file.register_file.getvalue(d)
        mem[instruction[8:]] = a    
        
    if instruction[:5]=="00110":
        a=dictionary[instruction[7:10]]
        b=dictionary[instruction[10:13]]
        d=dictionary[instruction[13:]]
        B = reg_file.register_file.getvalue(b)
        D = reg_file.register_file.getvalue(d)
        value = reg_file.bit_16(int(D, 2) * int(B, 2))
        if ((int(D,2)+ int(B,2)) > 65535):
            reg_file.register_file.save(reg_file.F, reg_file.bit_16(8))
        reg_file.register_file.save(a, value)
        
    if instruction[:5]=="00111":
        a=dictionary[instruction[7:10]]
        b=dictionary[instruction[10:13]]
        d=dictionary[instruction[13:]]
        B = reg_file.register_file.getvalue(b)
        D = reg_file.register_file.getvalue(d)
        value = reg_file.bit_16(int(D, 2) / int(B, 2))
        reg_file.register_file.save(a, value)

    if instruction[:5]=="01000":
        
        d=dictionary[instruction[5:8]]
        D = reg_file.register_file.getvalue(d)
        value = reg_file.bit_16(int(D, 2) >> int(instruction[8:], 2))
        reg_file.register_file.save(d, value)
       
    
    if instruction[:5]=="01001":
        
        d=dictionary[instruction[5:8]]
        D = reg_file.register_file.getvalue(d)
        value = reg_file.bit_16(int(D, 2) << int(instruction[8:], 2))
        reg_file.register_file.save(d, value)

    if instruction[:5]=="01010":
        a=dictionary[instruction[7:10]]
        b=dictionary[instruction[10:13]]
        d=dictionary[instruction[13:]]
        B = reg_file.register_file.getvalue(b)
        D = reg_file.register_file.getvalue(d)
        value= reg_file.bit_16(int(B,2)^int(D,2))
        reg_file.register_file.save(a, value)

    if instruction[:5]=="01011":
        a=dictionary[instruction[7:10]]
        b=dictionary[instruction[10:13]]
        d=dictionary[instruction[13:]]
        B = reg_file.register_file.getvalue(b)
        D = reg_file.register_file.getvalue(d)
        value= reg_file.bit_16(int(B,2) | int(D,2))
        reg_file.register_file.save(a, value)

    if instruction[:5]=="01100":
        a=dictionary[instruction[7:10]]
        b=dictionary[instruction[10:13]]
        d=dictionary[instruction[13:]]
        B = reg_file.register_file.getvalue(b)
        D = reg_file.register_file.getvalue(d)
        value= reg_file.bit_16(int(B,2) & int(D,2))
        reg_file.register_file.save(a, value)

       
    if instruction[:5]=="01101":
      
        b=dictionary[instruction[10:13]]
        d=dictionary[instruction[13:]]
        D = reg_file.register_file.getvalue(d)

        a=""
        for i in D:
            if i=="1":
                a+="0"
            else:
                a+="1"
        value=a
        
        register_file.save(b, value)
        reg_file.register_file.save(b, value)

    if instruction[:5]=="01110":
        
        b = dictionary[instruction[10:13]]
        d = dictionary[instruction[13:]]
        B = reg_file.register_file.getvalue(b)
        D = reg_file.register_file.getvalue(d)
        
        if int(B, 2) > int(D, 2):
            
            value = reg_file.bit_16(2)
            b = dictionary["111"]
            reg_file.register_file.save(b, value)
            
        elif int(B, 2)<int(D, 2):
            value= reg_file.bit_16(4)
            b = dictionary["111"]
            reg_file.register_file.save(b, value)
            
        elif int(B, 2)==int(D, 2):
            value= reg_file.bit_16(1)
            c = bin(7).replace("0b","")
            b = dictionary[c]
            reg_file.register_file.save(reg_file.F, value)



    '''if instruction[:5]=="01111":
        count = int(PC.PC_br_update(count,instruction),2)


    if instruction[:5]=="10000":
        if reg_file.F =="0000000000000100":
            count = int(PC.PC_br_update(count,instruction),2)
        else:
            count += 1
        
    if instruction[:5]=="10001":
        if reg_file.F =="0000000000000010":
            count = int(PC.PC_br_update(count,instruction),2)
        else:
            count += 1
        
    if instruction[:5]=="10010":
        if reg_file.F =="0000000000000001":
            count = int(PC.PC_br_update(count,instruction),2)
        else:
            count += 1'''
        