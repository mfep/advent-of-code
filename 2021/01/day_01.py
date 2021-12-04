with open("day_01.txt") as f:
  data = [int(x) for x in f.readlines()]

def count_increased(data):
  pairs = zip(data, data[1:])
  increased = map(lambda x: x[0] < x[1], pairs)
  return sum(increased)

print(count_increased(data))

triplets = zip(data, data[1:], data[2:])
triplet_sum = list(map(sum, triplets))

print(count_increased(triplet_sum))
