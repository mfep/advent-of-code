MOD = 20201227
initial_sub = 7
pub1 = 1327981
pub2 = 2822615

def transform(subject):
  value = 1
  while True:
    yield value
    value = (value * subject) % MOD

for i, value in enumerate(transform(initial_sub)):
  if value == pub1:
    loop1 = i
    break

# 14925185 too high
for i, value in enumerate(transform(pub2)):
  if i == loop1:
    print(value)
    break
