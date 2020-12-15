with open('day13.txt') as f:
  lines = f.readlines()
start = int(lines[0])
ids = [int(id) for id in lines[1].split(',') if id != 'x']
xids = [-1 if id == 'x' else int(id) for id in lines[1].split(',')]

remainders = []
for id in ids:
  remainders.append(id - start % id)

minrem = min(remainders)
minidx = remainders.index(minrem)

print(minrem * ids[minidx])

def is_series(start, xids):
  for i in range(len(xids)):
    id = xids[i]
    if id == -1:
      continue
    if (start + i) % id != 0:
      return False
  return True

i = 0
increment = 1
cids = xids[:1]
for new in xids[1:]:
  last = i
  cids.append(new)
  if new == -1:
    continue
  while not is_series(i, cids):
    i += increment
  # increment = i - last

print(i)
