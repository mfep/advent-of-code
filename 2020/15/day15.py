input = [15,12,0,14,3,1]

def iter(maxiter):
  spoken = {}
  for i in range(len(input) - 1):
    starting = input[i]
    spoken[starting] = i
  last = input[-1]
  for i in range(len(input) - 1, maxiter):
    current = last
    if last in spoken:
      last = i - spoken[last]
    else:
      last = 0
    spoken[current] = i
  print(current)

iter(2020)
iter(30000000)
