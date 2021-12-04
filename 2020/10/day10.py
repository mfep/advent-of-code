from collections import defaultdict

with open('day10.txt') as f:
  data = [int(x) for x in f]

data.append(0)
data.append(max(data) + 3)
data.sort()
differences = defaultdict(int)
for i in range(len(data) - 1):
  j = i + 1
  di, dj = data[i], data[j]
  differences[dj - di] += 1

print(differences[1] * differences[3])

data_reaches = defaultdict(int)
data_reaches[0] = 1
for current in data[1:]:
  data_reaches[current] = data_reaches[current - 1] + data_reaches[current - 2] + data_reaches[current - 3]

print(data_reaches[max(data)])
