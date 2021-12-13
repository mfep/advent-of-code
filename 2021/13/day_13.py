coords = set()
folds = []

with open('day_13.txt') as f:
  read_folds = False
  for line in f.readlines():
    line = line.strip()
    if len(line) == 0:
      read_folds = True
      continue
    if read_folds:
      equal_idx = line.index('=')
      fold_dim = line[equal_idx - 1]
      fold_threshold = int(line[equal_idx+1:])
      folds.append((fold_dim, fold_threshold))
    else:
      xy = tuple(int(c) for c in line.split(','))
      coords.add(xy)

def fold_y(coords, threshold):
  new_coords = set()
  for cx,cy in coords:
    if cy < threshold:
      new_coords.add((cx, cy))
    else:
      new_y = 2 * threshold - cy
      new_coords.add((cx, new_y))
  return new_coords

def fold_x(coords, threshold):
  new_coords = set()
  for cx,cy in coords:
    if cx < threshold:
      new_coords.add((cx, cy))
    else:
      new_x = 2 * threshold - cx
      new_coords.add((new_x, cy))
  return new_coords

for dim,threshold in folds:
  if dim == 'x':
    coords = fold_x(coords, threshold)
  elif dim == 'y':
    coords = fold_y(coords, threshold)
  print(len(coords))

display = ''
for row in range(6):
  for col in range(40):
    if (col, row) in coords:
      display += '█'
    else:
      display += ' '
  display += '\n'

print(display)
