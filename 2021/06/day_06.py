from collections import defaultdict

days = defaultdict(int)
with open('day_06.txt') as f:
  for remaining_day in [int(x) for x in f.readline().split(',')]:
    days[remaining_day] += 1


MAX_DAYS = 8

def simulate(days, turns):
  for _ in range(turns):
    new_days = defaultdict(int)
    for day in range(MAX_DAYS + 1):
      if day == 0:
        new_days[8] += days[day]
        new_days[6] += days[day]
      else:
        new_days[day - 1] += days[day]
    days = new_days

  print(sum(days.values()))

simulate(days, turns=80)
simulate(days, turns=256)
