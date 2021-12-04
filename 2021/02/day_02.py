depth = 0 # also aim
horizontal = 0
depth_2 = 0

FW = 'forward '
UP = 'up '
DW = 'down '

with open("day_02.txt") as f:
  for line in f.readlines():
    if line.startswith(FW):
      x = int(line[len(FW):])
      horizontal += x
      depth_2 += depth * x
    elif line.startswith(UP):
      depth -= int(line[len(UP):])
    elif line.startswith(DW):
      depth += int(line[len(DW):])
    else:
      raise Exception()

print(depth * horizontal)
print(depth_2 * horizontal)
