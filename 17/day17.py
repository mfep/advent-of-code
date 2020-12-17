with open('day17.txt') as f:
  lines = [line.strip() for line in f]

xmin,xmax,ymin,ymax,zmin,zmax = 0,0,0,0,0,0
active = set()

for row in range(len(lines)):
  for col in range(len(lines[0])):
    if lines[row][col] == '#':
      xmin = min(xmin, col)
      xmax = max(xmax, col)
      ymin = min(ymin, row)
      ymax = max(ymax, row)
      active.add((col, row, 0))

def count_active_neighbors(x,y,z):
  count = 0
  for layer in range(z - 1, z + 2):
    for row in range(y - 1, y + 2):
      for col in range (x - 1, x + 2):
        if layer == z and row == y and col == x:
          continue
        if (col, row, layer) in active:
          count += 1
  return count

ITER = 6
for iteration in range(ITER):
  active_copy = set(active)
  for layer in range(zmin - 1, zmax + 2):
    for row in range(ymin - 1, ymax + 2):
      for col in range(xmin - 1, xmax + 2):
        pos = (col, row, layer)
        current_is_active = pos in active
        active_neighbor_count = count_active_neighbors(*pos)
        if current_is_active and (active_neighbor_count < 2 or active_neighbor_count > 3):
          active_copy.remove(pos)
        elif not current_is_active and active_neighbor_count == 3:
          xmin = min(xmin, col)
          xmax = max(xmax, col)
          ymin = min(ymin, row)
          ymax = max(ymax, row)
          zmin = min(zmin, layer)
          zmax = max(zmax, layer)
          active_copy.add(pos)
  active = active_copy

print(len(active))
