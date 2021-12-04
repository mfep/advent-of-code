rules = {}
with open('classes.txt') as f:
  for line in f:
    colonidx = line.find(':')
    classname = line[:colonidx]
    minusidx = line.find('-', colonidx)
    min1 = int(line[colonidx + 1:minusidx])
    oridx = line.find('or', minusidx + 1)
    max1 = int(line[minusidx + 1:oridx])
    minusidx = line.find('-', oridx)
    min2 = int(line[oridx + 2:minusidx])
    max2 = int(line[minusidx + 1:])
    rules[classname] = (min1, max1, min2, max2)

with open('nearby.txt') as f:
  nearby_tickets = [[int(x) for x in line.split(',')] for line in f]

def matches_rule(value, min1, max1, min2, max2):
  return value >= min1 and value <= max1 or value >= min2 and value <= max2

valid_tickets = []
error_rate = 0
for ticket in nearby_tickets:
  ticket_valid = True
  for value in ticket:
    valid = False
    for rule in rules.values():
      if matches_rule(value, *rule):
        valid = True
        break
    if not valid:
      ticket_valid = False
      error_rate += value
  if ticket_valid:
    valid_tickets.append(ticket)

print(error_rate)

all_possible_classes = [set(rules.keys()) for i in range(len(rules))]
solutions = {}
while len(solutions) != len(rules):
  for column in range(len(rules)):
    possible_classes = all_possible_classes[column]
    if not possible_classes:
      continue
    for row in range(len(valid_tickets)):
      value = valid_tickets[row][column]
      for rulename in list(possible_classes):
        rule = rules[rulename]
        if not matches_rule(value, *rule):
          possible_classes.remove(rulename)
    if len(possible_classes) == 1:
      solution = possible_classes.pop()
      solutions[solution] = column
      for possible_class in all_possible_classes:
        if solution in possible_class:
          possible_class.remove(solution)

own = [137,173,167,139,73,67,61,179,103,113,163,71,97,101,109,59,131,127,107,53]
mul = 1
for sol_name, sol_idx in solutions.items():
  if sol_name.find('departure') >= 0:
    mul *= own[sol_idx]

print(mul)
