import memory
import EE
import PC
import reg_file
import bonus


mem = {}
mem = memory.memory_load(mem)

programm_counter = 0


halted = False

cycle = 0
while(not halted):
    Instruction = memory.mem_value(PC.bit_8(programm_counter),mem)
    EE.execute(Instruction,mem,programm_counter)
    p = bonus.question(cycle,programm_counter)
    print(PC.bit_8(programm_counter),end = " ")

    

    if Instruction[:5] != "01110" and Instruction[:5] != "00000" and Instruction[:5] != "00001" and Instruction[:5] != "00110":
        reg_file.register_file.save(reg_file.F,reg_file.bit_16(0))

    reg_file.reg_dump(reg_file.L)
    print()
        
    cycle +=1
    if (Instruction == "1001100000000000"):
        halted = True

    else:
        halted = False
        programm_counter = int(PC.PC_update(programm_counter,Instruction),2)
        

memory.mem_dump(mem)
p = p.save("testcase.png")

