from itertools import product
# import re
# middle_comma_pattern = re.compile(r'^\[(?:\[.*\]|\d)(\,).*\]')

# def parse(str):
#   found = re.search(middle_comma_pattern, str)
#   if found:
#     comma_idx = found.start(1)
#     left = parse(str[1:comma_idx])
#     right = parse(str[comma_idx+1:-1])
#     return [left, right]
#   else:
#     return int(str)

def parse(line):
  ret = []
  for ch in line:
    try:
      val = int(ch)
      ret.append(val)
    except:
      ret.append(ch)
  return ret

def add(left, right):
  return ['['] + left + [','] + right + [']']

def explode(value):
  depth = 0
  for idx,ch in enumerate(value):
    if ch == '[': depth += 1
    elif ch == ']': depth -= 1

    if depth > 4:
      left = value[idx + 1]
      right = value[idx + 3]
      left_idx = idx - 1
      while left_idx > 0:
        if type(value[left_idx]) is int:
          value[left_idx] += left
          break
        left_idx -= 1
      right_idx = idx+5
      while right_idx < len(value) - 1:
        if type(value[right_idx]) is int:
          value[right_idx] += right
          break
        right_idx += 1
      for _ in range(5):
        value.pop(idx)
      value.insert(idx, 0)
      return True
  assert(depth == 0)
  return False

def split(value):
  for idx,ch in enumerate(value):
    if (type(ch) is int) and ch > 9:
      value.pop(idx)
      value.insert(idx, '[')
      value.insert(idx+1, ch // 2)
      value.insert(idx+2, ',')
      value.insert(idx+3, (ch+1) // 2)
      value.insert(idx+4, ']')
      return True
  return False

def reduce(value):
  ret = True
  while ret:
    ret = explode(value)
  ret = True
  while ret:
    ret = split(value)
    ret2 = True
    while ret2:
      ret2 = explode(value)

def magnitude(value):
  if len(value) == 1:
    return value[0]
  depth = 0
  for idx,ch in enumerate(value):
    if ch == '[': depth += 1
    elif ch == ']': depth -= 1
    elif ch == ',' and depth == 1:
      middle = idx
      break
  return 3 * magnitude(value[1:middle]) + 2 * magnitude(value[middle+1:-1])
  

with open('day_18.txt') as f:
  lines = [parse(line.strip()) for line in f.readlines()]

value = lines[0]
for line in lines[1:]:
  value = add(value, line)
  reduce(value)

# for v in value:
#   print(v, end='')
print('\n')
print(magnitude(value))

max_magnitude = 0
for idx1 in range(len(lines)):
  for idx2 in range(len(lines)):
    if idx1 == idx2: continue
    added = add(lines[idx1], lines[idx2])
    reduce(added)
    max_magnitude = max(max_magnitude, magnitude(added))

print(max_magnitude)
