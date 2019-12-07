from itertools import permutations

def run_program(progdata, input_queue):
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
            program[program[iptr + 1]] = input_queue.pop(0)
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

def amplifier_chain(program, phases):
    val = 0
    for phase in phases:
        val = run_program(program, [phase, val])[0]
    return val

with open('day7.txt') as f:
    line = f.readline()
    program = [int(x) for x in line.split(',')]
phases_perm = permutations(range(5))
print('part one', max([amplifier_chain(program, phases) for phases in phases_perm]))
