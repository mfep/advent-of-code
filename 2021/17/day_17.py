X_MIN = 209
X_MAX = 238
Y_MIN = -86
Y_MAX = -59

def find_vx_range():
  global X_MIN
  global X_MAX
  vx = 1
  while True:
    x_dst = (vx * (vx + 1)) // 2
    if x_dst <= X_MAX and x_dst >= X_MIN:
      yield vx
    elif x_dst > X_MAX:
      break
    vx += 1

def find_vy_range(vx_start):
  global X_MIN
  global X_MAX
  global Y_MIN
  global Y_MAX
  vy_start = Y_MIN

  while vy_start < 1000:
    x = 0
    y = 0
    vx = vx_start
    vy = vy_start
    y_max = 0
    while True:
      x += vx
      y += vy
      y_max = max(y, y_max)
      vy -= 1
      if vx > 0:
        vx -= 1

      if x >= X_MIN and x <= X_MAX and y >= Y_MIN and y <= Y_MAX:
        yield vy_start, y_max
        break
      elif x > X_MAX or y < Y_MIN:
        break
    vy_start += 1

# for vx in find_vx_range():
#   for vy, y_max in find_vy_range(vx):
#     print(vx, vy, y_max)

def find_full_range():
  global X_MIN
  global X_MAX
  global Y_MIN
  global Y_MAX

  for vx_start in range(1,500):
    for vy_start in range(Y_MIN, 300):
      x = 0
      y = 0
      vx = vx_start
      vy = vy_start
      y_max = 0
      while True:
        x += vx
        y += vy
        y_max = max(y, y_max)
        vy -= 1
        if vx > 0:
          vx -= 1

        if x >= X_MIN and x <= X_MAX and y >= Y_MIN and y <= Y_MAX:
          yield vx_start, vy_start, y_max
        elif x > X_MAX or y < Y_MIN:
          break

total = 0
for vx,vy,x_max in set(find_full_range()):
  total += 1
  print(vx, vy)

print(total)
