def bit_8(a):
    bnr = bin(a).replace('0b','')
    x = bnr[::-1] 
    while len(x) < 8:
        x += '0'
    bnr = x[::-1]
    return(bnr)

def bit_16(a):
    bnr = bin(a).replace('0b','')
    #bnr =str(a)
    x = bnr[::-1] 
    while len(x) < 16:
        x += '0'
    bnr = x[::-1]
    return(bnr)

def memory_load(mem):
    binary = []
    while True :
        try:
            i=input()
            binary.append(i)
            if (i == '1001100000000000'):
                break
            else:
                continue
        except EOFError:
            break
    j = 0
    while (j < len(binary)):
        mem[bit_8(j)] = binary[j]
        j +=1
    return(mem) 

def mem_value(c, mem):
    return(mem[c])

def mem_dump(mem):
    W = list(mem.values())
    while len(W)< 256:
        W.append(bit_16(0))
    for value in W:
        print(value)
        