program = []
with open('day8.txt') as f:
  for line in f:
    words = line.split()
    program.append((words[0], int(words[1])))

def run(program):
  iptr, acc = 0, 0
  execi = set()
  while iptr not in execi:
    if iptr == len(program):
      return True, acc
    execi.add(iptr)
    inst, arg = program[iptr]
    if inst == 'acc':
      acc += arg
      iptr += 1
    elif inst == 'jmp':
      iptr += arg
    elif inst == 'nop':
      iptr += 1
    else:
      raise Exception(f'Unexpected instruction: "{inst}"')
  return False, acc

print(run(program))

for changed_iptr in range(len(program)):
  program_copy = list(program)
  inst, arg = program_copy[changed_iptr]
  if inst == 'acc':
    continue
  elif inst == 'jmp':
    program_copy[changed_iptr] = ('nop', arg)
  elif inst == 'nop':
    program_copy[changed_iptr] = ('jmp', arg)
  result, acc = run(program_copy)
  if result:
    print(acc)
    break
