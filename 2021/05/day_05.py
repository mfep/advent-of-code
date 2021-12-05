from collections import defaultdict

segments = []
with open('day_05.txt') as f:
  for line in f.readlines():
    arrow_idx = line.find('->')
    left = tuple(int(x) for x in line[:arrow_idx].split(','))
    right = tuple(int(x) for x in line[arrow_idx+2:].split(','))
    segments.append((left, right))

# sort by x
segments = list(map( \
  lambda segment: (segment[0], segment[1]) if segment[0][0] < segment[1][0] else (segment[1], segment[0]),\
    segments))

def is_not_diagonal(segment):
  (x1, y1), (x2, y2) = segment
  return x1 == x2 or y1 == y2

# part 1

not_diagonal_segments = list(filter(is_not_diagonal, segments))
board = defaultdict(int)
for ((x1, y1), (x2, y2)) in not_diagonal_segments:
  if x1 != x2:
    assert(y1 == y2)
    xdir = 1 if x1 < x2 else -1
    for x in range(x1, x2 + xdir, xdir):
      board[(x, y1)] += 1
  else:
    assert(y1 != y2)
    ydir = 1 if y1 < y2 else -1
    for y in range(y1, y2 + ydir, ydir):
      board[(x1, y)] += 1

print(sum(map(lambda c: 1 if c > 1 else 0, board.values())))

# part 2

board = defaultdict(int)
for ((x1, y1), (x2, y2)) in segments:
  assert(x1 <= x2)
  if x1 == x2: # vertical
    ydir = 1 if y1 < y2 else -1
    for y in range(y1, y2 + ydir, ydir):
      board[(x1, y)] += 1
  elif y1 == y2: # horizontal
    for x in range(x1, x2 + 1):
      board[(x, y1)] += 1
  else:
    assert(abs(x2 - x1) == abs(y2 - y1)) # 45deg
    ydir = 1 if y1 < y2 else -1
    for t in range(x2 - x1 + 1):
      board[(x1 + t, y1 + t * ydir)] += 1

print(sum(map(lambda c: 1 if c > 1 else 0, board.values())))

