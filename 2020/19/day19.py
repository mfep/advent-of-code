with open('day19.txt') as f:
  rules = {}
  while True:
    line = f.readline().strip()
    if line == '':
      break
    colon_index = line.find(':')
    rule_index = int(line[:colon_index])
    rule_string = line[colon_index + 2:]
    tokens = rule_string.split(' ')
    if not tokens[0].isnumeric():
      rules[rule_index] = tokens[0][1]
    elif '|' in tokens:
      pipe_index = tokens.index('|')
      rules[rule_index] = ([int(x) for x in tokens[:pipe_index]], [int(x) for x in tokens[pipe_index + 1:]])
    else:
      rules[rule_index] = [int(x) for x in tokens]

  messages = [line.strip() for line in f.readlines()]

def is_valid_r(rule, message):
  if isinstance(rule, str):
    return int(message[0] == rule)
  elif isinstance(rule, tuple):
    return is_valid_r(rule[0], message) or is_valid_r(rule[1], message)
  else: # rule is list
    i = 0
    for subrule in rule:
      if i == len(message):
        return 0
      subresult = is_valid_r(rules[subrule], message[i:])
      if subresult == 0:
        return 0
      i += subresult
    return i

def is_valid(message):
  detected_len = is_valid_r(rules[0], message)
  return len(message) == detected_len

print(sum([1 for message in messages if is_valid(message)]))

rules[8] = ([42], [42, 8])
rules[11] = ([42, 31], [42, 11, 31])

def is_valid_2(message):
  num8s = 1
  while True:
    m = message
    rule = [42] * num8s
    offset = is_valid_r(rule, m)
    if offset == 0:
      return False
    m = m[offset:]
    if m == '':
      return False
    num11s = 1
    while num11s < 10:
      rule = [42] * num11s + [31] * num11s
      offset = is_valid_r(rule, m)
      if offset == len(m):
        return True
      num11s += 1
    num8s += 1

print(sum([1 for message in messages if is_valid_2(message)]))
