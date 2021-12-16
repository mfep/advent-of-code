from functools import reduce
from operator import mul
import sys

def hex_to_bits(hex):
  if hex == '0': return [0, 0, 0, 0]
  if hex == '1': return [0, 0, 0, 1]
  if hex == '2': return [0, 0, 1, 0]
  if hex == '3': return [0, 0, 1, 1]
  if hex == '4': return [0, 1, 0, 0]
  if hex == '5': return [0, 1, 0, 1]
  if hex == '6': return [0, 1, 1, 0]
  if hex == '7': return [0, 1, 1, 1]
  if hex == '8': return [1, 0, 0, 0]
  if hex == '9': return [1, 0, 0, 1]
  if hex == 'A': return [1, 0, 1, 0]
  if hex == 'B': return [1, 0, 1, 1]
  if hex == 'C': return [1, 1, 0, 0]
  if hex == 'D': return [1, 1, 0, 1]
  if hex == 'E': return [1, 1, 1, 0]
  if hex == 'F': return [1, 1, 1, 1]

def bits_to_decimal(bits):
  result = 0
  for idx in range(len(bits)):
    bit = bits[-1-idx]
    if bit > 0:
      result += 1 << idx
  return result

with open('day_16.txt') as f:
  bits = []
  for hex_char in f.readline().strip():
    bits += hex_to_bits(hex_char)

version_sum = 0

def parse_packet(bits):
  global version_sum
  index = 0
  version = bits_to_decimal(bits[index:index+3])
  version_sum += version
  index += 3
  type_id = bits_to_decimal(bits[index:index+3])
  index += 3
  if type_id == 4:
    offset, value = parse_literal(bits[index:])
    index += offset
  else:
    offset, value = parse_operator(bits[6:], type_id)
    index += offset
  return index, value

def parse_literal(bits):
  not_last_group = True
  index = 0
  value = []
  while not_last_group:
    not_last_group = bool(bits[index])
    value += bits[index + 1:index + 5]
    index += 5
  return index, bits_to_decimal(value)

def parse_operator(bits, type_id):
  index = 0
  length_type_id = bits[index]
  index += 1
  values = []
  if length_type_id == 0:
    total_subpacket_length = bits_to_decimal(bits[index:index+15])
    index += 15
    subpacket_offset = 0
    while subpacket_offset < total_subpacket_length:
      offset, value = parse_packet(bits[index + subpacket_offset:])
      subpacket_offset += offset
      values.append(value)
    index += total_subpacket_length
  elif length_type_id == 1:
    num_subpackets = bits_to_decimal(bits[index:index+11])
    index += 11
    for _ in range(num_subpackets):
      offset, value = parse_packet(bits[index:])
      index += offset
      values.append(value)

  if type_id == 0:
    value = sum(values)
  elif type_id == 1:
    value = reduce(mul, values, 1)
  elif type_id == 2:
    value = reduce(min, values, sys.maxsize)
  elif type_id == 3:
    value = reduce(max, values, 0)
  elif type_id == 5:
    assert(len(values) == 2)
    value = int(values[0] > values[1])
  elif type_id == 6:
    assert(len(values) == 2)
    value = int(values[0] < values[1])
  elif type_id == 7:
    assert(len(values) == 2)
    value = int(values[0] == values[1])
  else:
    raise Exception()

  return index, value

_, value = parse_packet(bits)
print(version_sum, value)
