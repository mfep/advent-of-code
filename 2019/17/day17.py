import time
from os import system
from collections import defaultdict

class Cpu():
    def __init__(self, progdata):
        self.program = defaultdict(int)
        for i in range(len(progdata)):
            self.program[i] = progdata[i]
        self.iptr = 0
        self.relative = 0
        self.running = True

    def run(self, input_value):
        def get_digit(val, i):
            digits = str(val)
            r = 0 if i >= len(digits) else int(digits[-i - 1])
            return r

        def memget(pos, opspec):
            opnum = get_digit(opspec, pos + 2)
            if opnum == 0: # parameter mode
                return self.program[self.program[self.iptr + pos + 1]]
            elif opnum == 1: # immediate mode
                return self.program[self.iptr + pos + 1]
            elif opnum == 2: # relative mode
                return self.program[self.program[self.iptr + pos + 1] + self.relative]
            else:
                raise Exception('unknown opnum')

        def memset(pos, opspec, val):
            opnum = get_digit(opspec, pos + 2)
            if opnum == 0: # parameter mode
                self.program[self.program[self.iptr + pos + 1]] = val
            elif opnum == 1: # immediate mode
                raise Exception('memset cannot be invoked with direct access')
            elif opnum == 2: # relative mode
                self.program[self.program[self.iptr + pos + 1] + self.relative] = val
            else:
                raise Exception('unknown opnum')

        if not self.running:
            raise Exception('program already exited')

        output = []
        while True:
            opspec = self.program[self.iptr]
            opcode = int(str(opspec)[-2:])
            if opcode == 1: # ADD
                val = memget(0, opspec) + memget(1, opspec)
                memset(2, opspec, val)
                self.iptr += 4
            elif opcode == 2: # MUL
                val = memget(0, opspec) * memget(1, opspec)
                memset(2, opspec, val)
                self.iptr += 4
            elif opcode == 3: # INP
                if input_value is None:
                    return output
                memset(0, opspec, input_value)
                input_value = None
                self.iptr += 2
            elif opcode == 4: # OUT
                val = memget(0, opspec)
                output.append(val)
                self.iptr += 2
            elif opcode == 5: # JMP-T
                load1 = memget(0, opspec)
                if load1 == 0:
                    self.iptr += 3
                    continue
                load2 = memget(1, opspec)
                self.iptr = load2
            elif opcode == 6: # JMP-F
                load1 = memget(0, opspec)
                if load1 != 0:
                    self.iptr += 3
                    continue
                load2 = memget(1, opspec)
                self.iptr = load2
            elif opcode == 7: # LT
                load1 = memget(0, opspec)
                load2 = memget(1, opspec)
                val = 1 if load1 < load2 else 0
                memset(2, opspec, val)
                self.iptr += 4
            elif opcode == 8: # EQ
                load1 = memget(0, opspec)
                load2 = memget(1, opspec)
                val = 1 if load1 == load2 else 0
                memset(2, opspec, val)
                self.iptr += 4
            elif opcode == 9: # REL
                self.relative += memget(0, opspec)
                self.iptr += 2
            elif opcode == 99: # RET
                self.iptr += 1
                self.running = False
                break
            else:
                raise Exception('unexpected instruction', opcode)
        return output

with open('day17.txt') as f:
    program = [int(char) for char in f.readline().split(',')]

def is_intersection(world, x, y):
    width = len(world[0])
    height = len(world)
    if world[y][x] != '#':
        return False
    return x >= 1 and x < width - 1 and y >= 1 and y < height - 1 and world[y][x - 1] == '#' and world[y][x + 1] == '#' and world[y - 1][x] == '#' and world[y + 1][x] == '#'

def display(output):
    world = ''.join(chr(val) for val in output).splitlines()
    return [line for line in world if len(line)]

cpu = Cpu(program)
output = cpu.run(None)
world = display(output)
print('part one', sum(sum(col * row for col in range(len(world[0])) if is_intersection(world, col, row)) for row in range(len(world))))
#print('\n'.join(world))

inp = []
inp.append('A,A,B,C,B,C,B,C,B,A')
inp.append('L,10,L,8,R,8,L,8,R,6')
inp.append('R,6,R,8,R,8')
inp.append('R,6,R,6,L,8,L,10')
inp.append('n\n')
inp_queue = [ord(char) for char in '\n'.join(inp)]
program[0] = 2
cpu = Cpu(program)
output = cpu.run(None)
print('\n'.join(display(output)))

while inp_queue:
    output = cpu.run(inp_queue.pop(0))
    print('\n'.join(display(output[:-1])))
print('part two', output[-1])
