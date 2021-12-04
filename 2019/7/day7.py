from itertools import permutations, cycle

class Cpu(object):
    def __init__(self, program):
        self._program_state = program.copy()
        self._exited = False
        self._iptr = 0

    def run(self, input_queue):
        def get_digit(val, i):
            digits = str(val)
            r = 0 if i >= len(digits) else int(digits[-i - 1])
            return r
        if self._exited:
            raise Exception('Execution has finished already')
        program = self._program_state
        while True:
            opspec = program[self._iptr]
            opcode = int(str(opspec)[-2:])
            if opcode == 1: # ADD
                load1 = program[self._iptr + 1] if get_digit(opspec, 2) == 1 else program[program[self._iptr + 1]]
                load2 = program[self._iptr + 2] if get_digit(opspec, 3) == 1 else program[program[self._iptr + 2]]
                program[program[self._iptr + 3]] = load1 + load2
                self._iptr += 4
            elif opcode == 2: # MUL
                load1 = program[self._iptr + 1] if get_digit(opspec, 2) == 1 else program[program[self._iptr + 1]]
                load2 = program[self._iptr + 2] if get_digit(opspec, 3) == 1 else program[program[self._iptr + 2]]
                program[program[self._iptr + 3]] = load1 * load2
                self._iptr += 4
            elif opcode == 3: # INP
                program[program[self._iptr + 1]] = input_queue.pop(0)
                self._iptr += 2
            elif opcode == 4: # OUT
                load1 = program[self._iptr + 1] if get_digit(opspec, 2) == 1 else program[program[self._iptr + 1]]
                self._iptr += 2
                return load1
            elif opcode == 5: # JMP-T
                load1 = program[self._iptr + 1] if get_digit(opspec, 2) == 1 else program[program[self._iptr + 1]]
                if load1 == 0:
                    self._iptr += 3
                    continue
                load2 = program[self._iptr + 2] if get_digit(opspec, 3) == 1 else program[program[self._iptr + 2]]
                self._iptr = load2
            elif opcode == 6: # JMP-F
                load1 = program[self._iptr + 1] if get_digit(opspec, 2) == 1 else program[program[self._iptr + 1]]
                if load1 != 0:
                    self._iptr += 3
                    continue
                load2 = program[self._iptr + 2] if get_digit(opspec, 3) == 1 else program[program[self._iptr + 2]]
                self._iptr = load2
            elif opcode == 7: # LT
                load1 = program[self._iptr + 1] if get_digit(opspec, 2) == 1 else program[program[self._iptr + 1]]
                load2 = program[self._iptr + 2] if get_digit(opspec, 3) == 1 else program[program[self._iptr + 2]]
                program[program[self._iptr + 3]] = 1 if load1 < load2 else 0
                self._iptr += 4
            elif opcode == 8: # EQ
                load1 = program[self._iptr + 1] if get_digit(opspec, 2) == 1 else program[program[self._iptr + 1]]
                load2 = program[self._iptr + 2] if get_digit(opspec, 3) == 1 else program[program[self._iptr + 2]]
                program[program[self._iptr + 3]] = 1 if load1 == load2 else 0
                self._iptr += 4
            elif opcode == 99: # RET
                self._iptr += 1
                self._exited = True
                return None
            else:
                raise Exception('unexpected instruction', opcode)

def amplifier_chain(program, phases):
    val = 0
    for phase in phases:
        cpu = Cpu(program)
        val = cpu.run([phase, val])
    return val

def amplifier_feedback(program, phases):
    num_cpus = 5
    cpus = [Cpu(program) for _ in range(num_cpus)]
    used_indices = set()
    val = 0
    for cpu_idx in cycle(range(num_cpus)):
        if all([cpu._exited for cpu in cpus]):
            return val
        if cpu_idx not in used_indices:
            input = [phases[cpu_idx], val]
            used_indices.add(cpu_idx)
        else:
            input = [val]
        ret = cpus[cpu_idx].run(input)
        val = ret if ret else val

program = [3,26,1001,26,-4,26,3,27,1002,27,2,27,1,27,26,27,4,27,1001,28,-1,28,1005,28,6,99,0,0,5]
assert 139629729 == amplifier_feedback(program, [9,8,7,6,5])
program = [3,52,1001,52,-5,52,3,53,1,52,56,54,1007,54,5,55,1005,55,26,1001,54,
    -5,54,1105,1,12,1,53,54,53,1008,54,0,55,1001,55,1,55,2,53,55,53,4,
    53,1001,56,-1,56,1005,56,6,99,0,0,0,0,10]
assert 18216 == amplifier_feedback(program, [9,7,8,5,6])

with open('day7.txt') as f:
    line = f.readline()
    program = [int(x) for x in line.split(',')]
phases_perm = permutations(range(5))
print('part one', max([amplifier_chain(program, phases) for phases in phases_perm]))
phases_perm = permutations(range(5, 10))
print('part two', max([amplifier_feedback(program, phases) for phases in phases_perm]))
