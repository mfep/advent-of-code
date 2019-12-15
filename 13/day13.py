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
                memset(0, opspec, input_value)
                self.iptr += 2
            elif opcode == 4: # OUT
                val = memget(0, opspec)
                self.iptr += 2
                return val
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
        return None

with open('day13.txt') as f:
    program = [int(char) for char in f.readline().split(',')]

cpu = Cpu(program)
output = []
while cpu.running:
    output.append(cpu.run(None))
print('part one', sum(1 for idx,elem in enumerate(output) if idx % 3 == 2 and elem == 2))
