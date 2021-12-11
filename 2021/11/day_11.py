with open('day_11.txt') as f:
  energies = [[int(x) for x in row.strip()] for row in f.readlines()]

SIDE = len(energies)

def neighbours(cx, cy):
  for y in range(max(0, cy - 1), min(SIDE, cy + 2)):
    for x in range(max(0, cx - 1), min(SIDE, cx + 2)):
      if cx == x and cy == y:
        continue
      yield x,y

def update(cx, cy):
  global energies
  energies[cy][cx] += 1
  if energies[cy][cx] == 10:
    for nx,ny in neighbours(cx, cy):
      update(nx, ny)

total = 0
idx = 0
while(True):
  step_flash = 0
  for y in range(SIDE):
    for x in range(SIDE):
      update(x, y)
  for y in range(SIDE):
    for x in range(SIDE):
      if energies[y][x] > 9:
        energies[y][x] = 0
        total += 1
        step_flash += 1
  if idx == 99:
    print(total)
  idx += 1
  if step_flash == SIDE * SIDE:
    print(idx)
    break
