preamble = 25

with open('day9.txt') as f:
  data = [int(x) for x in f.readlines()]

def check(data, pos):
  value = data[pos]
  for i in range(pos - preamble, pos):
    for j in range(pos - preamble + 1, pos):
      if i == j:
        continue
      if data[i] + data[j] == value:
        return True
  return False

for i in range(preamble, len(data)):
  if not check(data, i):
    xxx = data[i]
    break

print(xxx)

for i in range(len(data)):
  for j in range(i + 2, len(data)):
    array = data[i:j]
    if sum(array) == xxx:
      print(min(array) + max(array))
