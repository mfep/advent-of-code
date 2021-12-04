passes = []

with open('day5.txt') as f:
  for line in f:
    line = line.strip()
    rows = ''.join(['1' if x == 'B' else '0' for x in line[0:7]])
    cols = ''.join(['1' if x == 'R' else '0' for x in line[7:10]])
    passes.append((int(rows, 2), int(cols, 2)))

ids = [8 * row + col for row,col in passes]
print(max(ids))

ids = set(ids)

for i in range(1, 8 * 128 - 1):
  if i not in ids and i - 1 in ids and i + 1 in ids:
    print(i)
