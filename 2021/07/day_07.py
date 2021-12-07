with open('day_07.txt') as f:
  input = [int(x) for x in f.readline().split(',')]

max_pos = max(input)

def solve(costs):
  totals = []
  for target_pos in range(max_pos):
    total = sum(costs[abs(pos - target_pos)] for pos in input)
    totals.append(total)

  print(min(totals))

# part 1
solve(list(range(max_pos + 1)))

# part 2

costs = [0]
for i in range(1, max_pos + 1):
  costs.append(costs[i - 1] + i)

solve(costs)
