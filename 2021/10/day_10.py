with open('day_10.txt') as f:
  lines = f.readlines()

total = 0
repair_scores = []
for line in lines:
  line = line.strip()
  stack = []
  valid = True  
  for ch in line:
    if ch == '(':
      stack.append(0)
    elif ch == '[':
      stack.append(1)
    elif ch == '{':
      stack.append(2)
    elif ch == '<':
      stack.append(3)
    elif ch == ')' and stack.pop() != 0:
      total += 3
      valid = False
      break
    elif ch == ']' and stack.pop() != 1:
      total += 57
      valid = False
      break
    elif ch == '}' and stack.pop() != 2:
      total += 1197
      valid = False
      break
    elif ch == '>' and stack.pop() != 3:
      valid = False
      total += 25137
      break
  if valid:
    repair_score = 0
    while stack:
      item = stack.pop()
      item_value = item + 1
      repair_score = repair_score * 5 + item_value
    repair_scores.append(repair_score)


print(total)

repair_scores.sort()
print(repair_scores[len(repair_scores) // 2])
