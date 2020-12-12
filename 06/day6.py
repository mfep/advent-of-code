from collections import defaultdict

count = 0
with open('day6.txt') as f:
  s = set()
  for line in f:
    line = line.strip()
    if line == '':
      count += len(s)
      s = set()
    else:
      for ch in line:
        s.add(ch)

print(count)

count = 0
with open('day6.txt') as f:
  d = defaultdict(int)
  people = 0
  for line in f:
    line = line.strip()
    if line == '':
      for i in d.values():
        if i == people:
          count += 1
      d = defaultdict(int)
      people = 0
    else:
      people += 1
      for ch in line:
        d[ch] += 1

print(count)
