import reg_file

def bit_8(a):
    bnr = bin(a).replace('0b','')
    x = bnr[::-1] 
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return(bnr)



def PC_update(count,instr):
    if (instr[:5] !="01111" and instr[:5] != "10000" and instr[:5] != "10001" and instr[:5] != "10010"):
        count += 1
    else:
        if (instr[:5] == "01111"):
            count = instr[8:]
            count = int(count,2)
        if (instr[:5] == "10000"):
            if (reg_file.F == reg_file.bit_16(4)):
                count = instr[8:]
                count = int(count,2)
            else:
                count += 1

        if (instr[:5] == "10001"):
            if (reg_file.F == reg_file.bit_16(2)):
                count = instr[8:]
                count = int(count,2)
            else:
                count += 1

        if (instr[:5] == "10010"):
            if (reg_file.F == reg_file.bit_16(1)):
                count = instr[8:]
                count = int(count,2)
            else:
                count += 1

    return(bit_8(count)) 

#def PC_br_update(count,instr):
#    count = instr[8:]

#    return(count) 

  