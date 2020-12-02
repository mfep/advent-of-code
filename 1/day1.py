with open('day1.txt') as f:
  data = [int(x) for x in f.readlines()]

for i in range(len(data)):
  for j in range(i, len(data)):
    x,y = data[i], data[j]
    if x + y == 2020:
      print(x * y)

for i in range(len(data)):
  for j in range(i, len(data)):
    for k in range(j, len(data)):
      x,y,z = data[i], data[j], data[k]
      if x + y + z == 2020:
        print(x * y * z)
