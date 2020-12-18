example0 = '1 + 2 * 3 + 4 * 5 + 6'
example = '2 * 3 + (4 * 5)'
example1 = '5 + (8 * 3 + 9 + 3 * 4 * 3)'
example2 = '5 * 9 * (7 * 3 * 3 + 9 * 3 + (8 + 6 * 4))'
example3 = '((2 + 4 * 9) * (6 + 9 * 8 + 6) + 6) + 2 + 4 * 2'

# only single digit numbers
def preprocess(expression_str):
  symbol_list = [symbol for symbol in expression_str if symbol != ' ']
  return symbol_list

def find_after_closing_parens(symbol_list):
  assert(symbol_list[0] == '(')
  level = 1
  for i, symbol in enumerate(symbol_list[1:]):
    if symbol == '(':
      level += 1
    elif symbol == ')':
      level -= 1
    if level == 0:
      return i + 1
  assert(False)

def evaluate(symbol_list):
  i = 0
  result = 0
  op = '+'
  while True:
    symbol = symbol_list[i]
    if symbol == '(':
      close = find_after_closing_parens(symbol_list[i:])
      value = evaluate(symbol_list[i + 1 : i + close])
      i += close + 1
    else:
      value = int(symbol)
      i += 1
    if op == '*':
      result *= value
    elif op == '+':
      result += value
    else:
      assert(False)
    if i >= len(symbol_list):
      return result
    op = symbol_list[i]
    i += 1
  assert(False)

# print(evaluate(preprocess(example)))
# print(evaluate(preprocess(example1)))
# print(evaluate(preprocess(example2)))
# print(evaluate(preprocess(example3)))

with open('day18.txt') as f:
  print(sum([evaluate(preprocess(line.strip())) for line in f]))

def evaluate2(symbol_list):
  i = 1
  while i < len(symbol_list):
    if symbol_list[i] == '+':
      j = i - 1
      level = 1 if symbol_list[j] == ')' else 0
      while level != 0:
        j -= 1
        if symbol_list[j] == '(':
          level -= 1
        elif symbol_list[j] == ')':
          level += 1
      symbol_list.insert(j, '(')

      j = i + 2
      if j >= len(symbol_list):
        symbol_list.append(')')
        return symbol_list
      level = 1 if symbol_list[j] == '(' else 0
      while level != 0:
        j += 1
        if symbol_list[j] == ')':
          level -= 1
        elif symbol_list[j] == '(':
          level += 1
      symbol_list.insert(j + 1, ')')
      i += 1
    i += 1
  return symbol_list

# x0 = ' '.join(evaluate2(preprocess(example0)))
# print(x0, '=', eval(x0))
# x = ' '.join(evaluate2(preprocess(example)))
# print(x, '=', eval(x))
# x1 = ' '.join(evaluate2(preprocess(example1)))
# print(x1, '=', eval(x1))
# x2 = ' '.join(evaluate2(preprocess(example2)))
# print(x2, '=', eval(x2))
# x3 = ' '.join(evaluate2(preprocess(example3)))
# print(x3, '=', eval(x3))

def eval2(exp):
  return eval(' '.join(evaluate2(preprocess(exp))))

with open('day18.txt') as f:
  print(sum([eval2(line.strip()) for line in f]))
