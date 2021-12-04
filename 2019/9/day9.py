from collections import defaultdict

def run_program(progdata, input_value):
    def get_digit(val, i):
        digits = str(val)
        r = 0 if i >= len(digits) else int(digits[-i - 1])
        return r

    def memget(pos, opspec):
        opnum = get_digit(opspec, pos + 2)
        if opnum == 0: # parameter mode
            return program[program[iptr + pos + 1]]
        elif opnum == 1: # immediate mode
            return program[iptr + pos + 1]
        elif opnum == 2: # relative mode
            return program[program[iptr + pos + 1] + relative]
        else:
            raise Exception('unknown opnum')

    def memset(pos, opspec, val):
        opnum = get_digit(opspec, pos + 2)
        if opnum == 0: # parameter mode
            program[program[iptr + pos + 1]] = val
        elif opnum == 1: # immediate mode
            raise Exception('memset cannot be invoked with direct access')
        elif opnum == 2: # relative mode
            program[program[iptr + pos + 1] + relative] = val
        else:
            raise Exception('unknown opnum')

    program = defaultdict(lambda: 0)
    for i in range(len(progdata)):
        program[i] = progdata[i]
    output = []
    iptr = 0
    relative = 0
    while True:
        opspec = program[iptr]
        opcode = int(str(opspec)[-2:])
        if opcode == 1: # ADD
            val = memget(0, opspec) + memget(1, opspec)
            memset(2, opspec, val)
            iptr += 4
        elif opcode == 2: # MUL
            val = memget(0, opspec) * memget(1, opspec)
            memset(2, opspec, val)
            iptr += 4
        elif opcode == 3: # INP
            memset(0, opspec, input_value)
            iptr += 2
        elif opcode == 4: # OUT
            output.append(memget(0, opspec))
            iptr += 2
        elif opcode == 5: # JMP-T
            load1 = memget(0, opspec)
            if load1 == 0:
                iptr += 3
                continue
            load2 = memget(1, opspec)
            iptr = load2
        elif opcode == 6: # JMP-F
            load1 = memget(0, opspec)
            if load1 != 0:
                iptr += 3
                continue
            load2 = memget(1, opspec)
            iptr = load2
        elif opcode == 7: # LT
            load1 = memget(0, opspec)
            load2 = memget(1, opspec)
            val = 1 if load1 < load2 else 0
            memset(2, opspec, val)
            iptr += 4
        elif opcode == 8: # EQ
            load1 = memget(0, opspec)
            load2 = memget(1, opspec)
            val = 1 if load1 == load2 else 0
            memset(2, opspec, val)
            iptr += 4
        elif opcode == 9: # REL
            relative += memget(0, opspec)
            iptr += 2
        elif opcode == 99: # RET
            iptr += 1
            break
        else:
            raise Exception('unexpected instruction', opcode)
    return output

with open('day9.txt') as f:
    line = f.readline()
prog = [int(char) for char in line.split(',')]
print('part one', run_program(prog, 1))
print('part two', run_program(prog, 2))
