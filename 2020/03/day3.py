with open('day3.txt') as f:
  lines = [x.strip() for x in f.readlines()]

def get(x,y):
  return lines[y][x % len(lines[0])]

slopes = [(1,1), (3,1), (5,1), (7,1), (1,2)]
alltrees = []

for dx,dy in slopes:
  x,y,trees = 0,0,0
  while y < len(lines):
    if get(x,y) == '#':
      trees += 1
    x += dx
    y += dy
  alltrees.append(trees)

mul = 1
for tree in alltrees:
  mul *= tree

print(alltrees[1])
print(mul)
