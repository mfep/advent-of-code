with open('day11.txt') as f:
  seat_map = [[ch for ch in line.strip()] for line in f]

H = len(seat_map)
W = len(seat_map[0])

def count_occupied_around(x, y, seat_map):
  count = 0
  for row in range(y - 1, y + 2):
    for col in range(x - 1, x + 2):
      if row >= 0 and row < H and col >= 0 and col < W and not (row == y and col == x) and seat_map[row][col] == '#':
        count += 1
  return count

def copy(sm):
  return [[ch for ch in line] for line in sm]

def iter(seat_map):
  new_seat_map = copy(seat_map)
  for row in range(H):
    for col in range(W):
      if seat_map[row][col] == '.':
        continue
      occupied_around = count_occupied_around(col, row, seat_map)
      if occupied_around == 0:
        new_seat_map[row][col] = '#'
      elif occupied_around >= 4:
        new_seat_map[row][col] = 'L'
      else:
        new_seat_map[row][col] = seat_map[row][col]
  return new_seat_map

def diff(sm1, sm2):
  diff_count = 0
  for row in range(H):
    for col in range(W):
      if sm1[row][col] != sm2[row][col]:
        diff_count += 1
  return diff_count

def count_occupied(sm):
  count = 0
  for row in range(H):
    for col in range(W):
      if sm[row][col] == '#':
        count += 1
  return count


s1 = copy(seat_map)
s2 = iter(s1)

while diff(s1, s2) > 0:
  s1, s2 = s2, iter(s2)

print(count_occupied(s1))

def trace(x, y, dx, dy, sm):
  while True:
    x += dx
    y += dy
    if x < 0 or y < 0 or x >= W or y >= H:
      return None
    if sm[y][x] != '.':
      return x, y

directions = [
  (-1, -1),
  (-1, 1),
  (-1, 0),
  (0, -1),
  (0, 1),
  (1, -1),
  (1, 1),
  (1, 0)]
def trace_map(x, y, sm):
  dirmap = {}
  for dxy in directions:
    dirmap[dxy] = trace(x, y, *dxy, sm)
  return dirmap

def all_trace_maps(sm):
  all_trace_map = [[0 for j in range(W)] for i in range(H)]
  for row in range(H):
    for col in range(W):
      if sm[row][col] != '.':
        all_trace_map[row][col] = trace_map(col, row, sm)
  return all_trace_map

def occupied_traced(x, y, sm, tracemap):
  occupied = 0
  for xy in tracemap[y][x].values():
    if xy and sm[xy[1]][xy[0]] == '#':
      occupied += 1
  return occupied

def iter_traced(sm, tracemap):
  sm2 = copy(sm)
  for row in range(H):
    for col in range(W):
      if sm[row][col] == '.':
        continue
      occupied_around = occupied_traced(col, row, sm, tracemap)
      if occupied_around == 0:
        sm2[row][col] = '#'
      elif occupied_around >= 5:
        sm2[row][col] = 'L'
      else:
        sm2[row][col] = sm[row][col]
  return sm2

tm = all_trace_maps(seat_map)
s1 = copy(seat_map)
s2 = iter_traced(s1, tm)

while diff(s1, s2) > 0:
  s1, s2 = s2, iter_traced(s2, tm)

print(count_occupied(s1))
