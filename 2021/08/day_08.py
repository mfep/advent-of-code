from itertools import permutations

with open('day_08.txt') as f:
  lines = f.readlines()

searched_lengths = [2, 3, 4, 7]
count = 0
for line in lines:
  colon_idx = line.index('|')
  outputs = line[colon_idx + 1:].split()
  for output_str in outputs:
    output_length = len(output_str)
    if output_length in searched_lengths:
      count += 1

print(count)

# part 2

ZERO = set([0, 1, 2, 4, 5, 6])
ONE = set([2, 5])
TWO = set([0, 2, 3, 4, 6])
THREE = set([0, 2, 3, 5, 6])
FOUR = set([1, 2, 3, 5])
FIVE = set([0, 1, 3, 5, 6])
SIX = set([0, 1, 3, 4, 5, 6])
SEVEN = set([0, 2, 5])
EIGHT = set([0, 1, 2, 3, 4, 5, 6])
NINE = set([0, 1, 2, 3, 5, 6])

def get_digit(segment_set):
  if segment_set == ZERO: return 0
  elif segment_set == ONE: return 1
  elif segment_set == TWO: return 2
  elif segment_set == THREE: return 3
  elif segment_set == FOUR: return 4
  elif segment_set == FIVE: return 5
  elif segment_set == SIX: return 6
  elif segment_set == SEVEN: return 7
  elif segment_set == EIGHT: return 8
  elif segment_set == NINE: return 9
  else: return -1

def check_permutation(items, permutation):
  assert(len(items) == 10)
  assert(len(permutation) == 7)
  digits = set()
  for item in items:
    permuted_item = set(permutation[i] for i in item)
    digit = get_digit(permuted_item)
    if digit < 0: return False
    digits.add(digit)
  return len(digits) == 10

A_IDX = ord('a')

def parse(s):
  return set(ord(c) - A_IDX for c in s)

total = 0
for line in lines:
  colon_idx = line.index('|')
  items = [parse(s) for s in line[:colon_idx].split()]
  for permutation in permutations(range(7)):
    if check_permutation(items, permutation):
      break

  output_items = [parse(s) for s in line[colon_idx+1:].split()]
  radix = 10**(len(output_items) - 1)
  for output_item in output_items:
    permuted_item = set(permutation[i] for i in output_item)
    total += radix * get_digit(permuted_item)
    radix /= 10

print(int(total))
