directions = [
  (1, 0), # east
  (0, 1), # south
  (-1, 0), # west
  (0, -1) # north
]
def rotate(x, y, code, value):
  rotations = value // 90
  if code == 'R':
    for i in range(rotations):
      x, y = -y, x
  elif code == 'L':
    for i in range(rotations):
      x, y = y, -x
  return x, y

with open('day12.txt') as f:
  instr = [line.strip() for line in f]

def move():
  px, py = 0, 0 # position
  dx, dy = 1, 0 # direction

  for inst in instr:
    code = inst[0]
    value = int(inst[1:])
    if code == 'N':
      py -= value
    elif code == 'S':
      py += value
    elif code == 'E':
      px += value
    elif code == 'W':
      px -= value
    elif code == 'F':
      px += dx * value
      py += dy * value
    elif code == 'L' or code == 'R':
      dx, dy = rotate(dx, dy, code, value)
    else:
      raise Exception(f'unexpected code: {code}')
  return px, py

px, py = move()
print(abs(px) + abs(py))

def wmove():
  px, py = 0, 0
  wx, wy = 10, -1
  for inst in instr:
    code = inst[0]
    value = int(inst[1:])
    if code == 'N':
      wy -= value
    elif code == 'S':
      wy += value
    elif code == 'E':
      wx += value
    elif code == 'W':
      wx -= value
    elif code == 'F':
      px += wx * value
      py += wy * value
    elif code == 'L' or code == 'R':
      wx, wy = rotate(wx, wy, code, value)
    else:
      raise Exception(f'unexpected code: {code}')
  return px, py

px, py = wmove()
print(abs(px) + abs(py))
