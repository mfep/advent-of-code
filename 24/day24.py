import re

ex = r'(ne)|(nw)|(w)|(sw)|(se)|(e)'
with open('day24.txt') as f:
  tiles = []
  for line in f:
    tile = []
    for match in re.finditer(ex, line):
      tile.append(match.group())
    tiles.append(tile)

def dir2coord(dir):
  if dir == 'ne':
    return (-1, 1)
  elif dir == 'nw':
    return (0, 1)
  elif dir == 'w':
    return (1, 0)
  elif dir == 'sw':
    return (1, -1)
  elif dir == 'se':
    return (0, -1)
  elif dir == 'e':
    return (-1, 0)
  else:
    assert(False)

black_tiles = set()
for tile in tiles:
  tx, ty = 0, 0
  for direction in tile:
    dx, dy = dir2coord(direction)
    tx += dx
    ty += dy
  if (tx, ty) in black_tiles:
    black_tiles.remove((tx, ty))
  else:
    black_tiles.add((tx, ty))

print(len(black_tiles))

directions = [(0, 1), (1, 0), (1, -1), (0, -1), (-1, 0), (-1, 1)]
def count_black_neighbors(tx, ty, tiles):
  count = 0
  for dx, dy in directions:
    if (tx + dx, ty + dy) in tiles:
      count += 1
  return count

for iter in range(100):
  copied_black_tiles = set(black_tiles)
  for txy in black_tiles:
    black_neighbour_count = count_black_neighbors(*txy, black_tiles)
    if black_neighbour_count == 0 or black_neighbour_count > 2:
      copied_black_tiles.remove(txy)
    for dx, dy in directions:
      white_tile = (txy[0] + dx, txy[1] + dy)
      if white_tile in black_tiles:
        continue
      black_neighbour_count = count_black_neighbors(*white_tile, black_tiles)
      if black_neighbour_count == 2:
        copied_black_tiles.add(white_tile)
  black_tiles = copied_black_tiles

print(len(black_tiles))
