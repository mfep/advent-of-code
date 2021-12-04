class Board(object):
  def __init__(self, lines):
    assert(len(lines) == 5)
    self.data = []
    for line in lines:
      self.data += [int(x) for x in line.split()]
    assert(len(self.data) == 25)
    self.drawn = [False for _ in self.data]

  def score(self, drawn):
    return sum([0 if self.drawn[idx] else self.data[idx] for idx in range(25)]) * drawn

  def update(self, x):
    try:
      idx = self.data.index(x)
      self.drawn[idx] = True
      row = idx // 5
      col = idx % 5
      row_indices = range(5 * row, 5 * row + 5)
      col_indices = range(col, 25, 5)
      if sum(map(lambda idx: self.drawn[idx], row_indices)) == 5 \
        or sum(map(lambda idx: self.drawn[idx], col_indices)) == 5:
        return self.score(x)
      else:
        return None
    except ValueError:
      return None


with open('day_04.txt') as f:
  lines = f.readlines()

num_boards = (len(lines) - 1) // 6
deck = [int(x) for x in lines[0].split(',')]

def part1():
  boards = []
  for i in range(num_boards):
    boards.append(Board(lines[2+6*i:1+6*(i+1)]))

  for drawn in deck:
    for board in boards:
      score = board.update(drawn)
      if score:
        print(score)
        return

def part2():
  boards = []
  for i in range(num_boards):
    boards.append(Board(lines[2+6*i:1+6*(i+1)]))

  for drawn in deck:
    boards_to_remove = []
    for board in boards:
      score = board.update(drawn)
      if score:
        if len(boards) == 1:
          print(score)
          return
        boards_to_remove.append(board)
    while len(boards) > 1 and boards_to_remove:
      boards.remove(boards_to_remove.pop(0))

part1()
part2()
