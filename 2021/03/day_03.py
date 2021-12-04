with open('day_03.txt') as f:
  length = len(f.readline()) - 1

with open('day_03.txt') as f:
  data = [int(x, 2) for x in f.readlines()]

def count_bits(data):
  gamma = 0
  epsilon = 0

  for bit_idx in range(length):
    bit = 1 << bit_idx
    count = 0
    for entry in data:
      if entry & bit != 0:
        count += 1
    if count >= len(data) / 2:
      gamma |= bit
    elif count <= len(data) / 2:
      epsilon |= bit
  return gamma, epsilon

gamma, epsilon = count_bits(data)
print(gamma * epsilon)

# part 2
filtered = data
for bit_cnt in range(length):
  mask = 1 << length - bit_cnt - 1
  gamma, epsilon = count_bits(filtered)
  filtered = list(filter(lambda x: (x & mask) ^ (gamma & mask) == 0, filtered))
  if len(filtered) == 1:
    o2 = filtered[0]
    break

filtered = data
for bit_cnt in range(length):
  mask = 1 << length - bit_cnt - 1
  gamma, epsilon = count_bits(filtered)
  filtered = list(filter(lambda x: (x & mask) ^ (epsilon & mask) == 0, filtered))
  if len(filtered) == 1:
    co2 = filtered[0]
    break

print(o2 * co2)
