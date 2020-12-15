import itertools as it

BITS = 36

def parse_mask(mask):
  mask_rev = mask[::-1]
  mask_val = 0
  mask_mask = 0
  for i in range(len(mask_rev)):
    if mask_rev[i] == '1':
      mask_val |= 1 << i
      mask_mask |= 1 << i
    elif mask_rev[i] == '0':
      mask_mask |= 1 << i
  return mask_val, mask_mask

def apply_mask(mask_val, mask_mask, value):
  return (value & ~mask_mask) | mask_val

memory = {}
with open('day14.txt') as f:
  for line in f:
    line = line.strip()
    if line[:7] == 'mask = ':
      mask_val, mask_mask = parse_mask(line[7:])
    elif line[:4] == 'mem[':
      closing = line.find(']')
      address = int(line[4:closing])
      value = int(line[closing + 4:])
      memory[address] = apply_mask(mask_val, mask_mask, value)

print(sum(memory.values()))

def floating_addresses(mask_val, mask_mask, address):
  masked_address = (address | mask_val) & mask_mask
  xindices = [i for i in range(BITS) if (1 << i) & ~mask_mask != 0]
  for size in range(len(xindices) + 1):
    for combination in it.combinations(xindices, size):
      current_val = masked_address
      for i in range(BITS):
        digit = 1 << i
        if i in combination:
          current_val |= digit
      yield current_val

memory = {}
with open('day14.txt') as f:
  for line in f:
    line = line.strip()
    if line[:7] == 'mask = ':
      mask_val, mask_mask = parse_mask(line[7:])
    elif line[:4] == 'mem[':
      closing = line.find(']')
      address = int(line[4:closing])
      value = int(line[closing + 4:])
      for add in floating_addresses(mask_val, mask_mask, address):
        memory[add] = value

print(sum(memory.values()))
