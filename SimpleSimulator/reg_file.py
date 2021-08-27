def bit_16(a):
    bnr = bin(a).replace('0b','')
    #bnr =str(a)
    x = bnr[::-1] 
    while len(x) < 16:
        x += '0'
    bnr = x[::-1]
    return(bnr)



class register_file:
    def __init__(self, val):
        self.val = bit_16(val)
    def getvalue(self):
        return(self.val)
    def save(self, new_val):
        self.val = new_val
         

r0 = register_file(0)
r1 = register_file(0)
r2 = register_file(0)
r3 = register_file(0)
r4 = register_file(0)
r5 = register_file(0)
r6 = register_file(0)
F = register_file(0)

L = [r0,r1,r2,r3,r4,r5,r6,F]
def reg_dump(L):
    for i in L:
        print(register_file.getvalue(i),end=" ")

