from collections import defaultdict

height_map = []
with open('day_09.txt') as f:
  for line in f.readlines():
    height_map.append([int(x) for x in line.strip()])

WIDTH = len(height_map[0])
HEIGHT = len(height_map)

def adjacent(x, y):
  global height_map
  if x > 0: yield height_map[y][x - 1]
  if y > 0: yield height_map[y - 1][x]
  if x < WIDTH - 1: yield height_map[y][x + 1]
  if y < HEIGHT - 1: yield height_map[y + 1][x]

def adjacent_coord(x, y):
  global height_map
  if x > 0: yield height_map[y][x - 1], x-1, y
  if y > 0: yield height_map[y - 1][x], x, y-1
  if x < WIDTH - 1: yield height_map[y][x + 1], x+1, y
  if y < HEIGHT - 1: yield height_map[y + 1][x], x, y+1

risk = 0
lows = []
for cy in range(HEIGHT):
  for cx in range(WIDTH):
    current = height_map[cy][cx]
    if all(current < adj for adj in adjacent(cx, cy)):
      risk += current + 1
      lows.append((cx, cy))

print(risk)

# part 2
basins = [[-1 for _ in range(WIDTH)] for _ in range(HEIGHT)]
basin_idx = 0
basin_count = defaultdict(int)

while lows: # flood fill
  lx, ly = lows.pop()
  current_idx = basins[ly][lx]
  if current_idx < 0:
    basin_idx += 1
    current_idx = basin_idx
  
  for h,nx,ny in adjacent_coord(lx, ly):
    if h == 9: continue
    b = basins[ny][nx]
    if b >= 0:
      assert(b == current_idx)
    else:
      basins[ny][nx] = current_idx
      basin_count[current_idx] += 1
      lows.append((nx, ny))

counts = list(basin_count.values())
counts.sort()
print(counts[-1] * counts[-2] * counts[-3])
