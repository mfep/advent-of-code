import os
print(os.getcwd())

with open('day5.txt') as f:
    line = f.readline()
    data = [int(x) for x in line.split(',')]

def run_program(progdata, input_value):
    def get_digit(val, i):
        digits = str(val)
        r = 0 if i >= len(digits) else int(digits[-i - 1])
        return r

    program = progdata.copy()
    output = []
    iptr = 0
    while True:
        opspec = program[iptr]
        opcode = int(str(opspec)[-2:])
        if opcode == 1: # ADD
            load1 = program[iptr + 1] if get_digit(opspec, 2) == 1 else program[program[iptr + 1]]
            load2 = program[iptr + 2] if get_digit(opspec, 3) == 1 else program[program[iptr + 2]]
            program[program[iptr + 3]] = load1 + load2
            iptr += 4
        elif opcode == 2: # MUL
            load1 = program[iptr + 1] if get_digit(opspec, 2) == 1 else program[program[iptr + 1]]
            load2 = program[iptr + 2] if get_digit(opspec, 3) == 1 else program[program[iptr + 2]]
            program[program[iptr + 3]] = load1 * load2
            iptr += 4
        elif opcode == 3: # INP
            program[program[iptr + 1]] = input_value
            iptr += 2
        elif opcode == 4: # OUT
            load1 = program[iptr + 1] if get_digit(opspec, 2) == 1 else program[program[iptr + 1]]
            output.append(load1)
            iptr += 2
        elif opcode == 5: # JMP-T
            load1 = program[iptr + 1] if get_digit(opspec, 2) == 1 else program[program[iptr + 1]]
            if load1 == 0:
                iptr += 3
                continue
            load2 = program[iptr + 2] if get_digit(opspec, 3) == 1 else program[program[iptr + 2]]
            iptr = load2
        elif opcode == 6: # JMP-F
            load1 = program[iptr + 1] if get_digit(opspec, 2) == 1 else program[program[iptr + 1]]
            if load1 != 0:
                iptr += 3
                continue
            load2 = program[iptr + 2] if get_digit(opspec, 3) == 1 else program[program[iptr + 2]]
            iptr = load2
        elif opcode == 7: # LT
            load1 = program[iptr + 1] if get_digit(opspec, 2) == 1 else program[program[iptr + 1]]
            load2 = program[iptr + 2] if get_digit(opspec, 3) == 1 else program[program[iptr + 2]]
            program[program[iptr + 3]] = 1 if load1 < load2 else 0
            iptr += 4
        elif opcode == 8: # EQ
            load1 = program[iptr + 1] if get_digit(opspec, 2) == 1 else program[program[iptr + 1]]
            load2 = program[iptr + 2] if get_digit(opspec, 3) == 1 else program[program[iptr + 2]]
            program[program[iptr + 3]] = 1 if load1 == load2 else 0
            iptr += 4
        elif opcode == 99: # RET
            iptr += 1
            break
        else:
            raise Exception('unexpected instruction', opcode)
    return output

print(run_program(data, 5))