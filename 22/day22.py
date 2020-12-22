player1 = []
player2 = []
player = player1

with open('day22.txt') as f:
  for line in f:
    line = line.strip()
    if line == '':
      player = player2
    else:
      player.append(int(line))

def score(player):
  sum = 0
  for i in range(len(player)):
    sum += player[i] * (len(player) - i)
  return sum

def combat(player1, player2):
  player1, player2 = list(player1), list(player2)
  while player1 and player2:
    p1 = player1.pop(0)
    p2 = player2.pop(0)
    if p1 > p2:
      player1.append(p1)
      player1.append(p2)
    elif p2 > p1:
      player2.append(p2)
      player2.append(p1)
    else:
      assert(False)
  return score(player1), score(player2)

def combat_r(player1, player2):
  player1, player2 = list(player1), list(player2)
  turn_hashes = set()
  while player1 and player2:
    current_hash = hash((tuple(player1), tuple(player2)))
    if current_hash in turn_hashes:
      return (1, 0)
    turn_hashes.add(current_hash)

    p1 = player1.pop(0)
    p2 = player2.pop(0)
    assert(p1 != p2)
    if len(player1) >= p1 and len(player2) >= p2:
      subgame_result = combat_r(player1[:p1], player2[:p2])
      winner = 2 if subgame_result[0] == 0 else 1
    else:
      winner = 1 if p1 > p2 else 2
    if winner == 1:
      player1.append(p1)
      player1.append(p2)
    else:
      player2.append(p2)
      player2.append(p1)
  return score(player1), score(player2)

print(combat(player1, player2))
print(combat_r(player1, player2))
