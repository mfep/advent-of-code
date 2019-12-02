import sys

with open('day2.txt') as f:
    line = f.readline()
    splitted = line.split(',')
    data = [int(x) for x in splitted]

def run_program(arg1, arg2):
    program = data.copy()
    program[1] = arg1
    program[2] = arg2
    iptr = 0
    while program[iptr] != 99:
        op, load1, load2, store = program[iptr], program[iptr + 1], program[iptr + 2], program[iptr + 3]
        if op == 1:
            program[store] = program[load1] + program[load2]
        elif op == 2:
            program[store] = program[load1] * program[load2]
        elif op != 99:
            raise Exception('unexpected instruction')
        iptr += 4
    return program[0]

for noun in range(0, 99):
    for verb in range(0, 99):
        if run_program(noun, verb) == 19690720:
            print(100 * noun + verb)
