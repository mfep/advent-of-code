import math

def calc_fuel(weight):
    return math.floor(weight / 3) - 2

def calc_fuel_rec(weight):
    dfuel = calc_fuel(weight)
    sfuel = 0
    while dfuel > 0:
        sfuel += dfuel
        dfuel = calc_fuel(dfuel)
    return sfuel

with open('day1.txt') as f:
    weights = [int(line) for line in f.readlines()]
result = sum([calc_fuel_rec(weight) for weight in weights])
print(result)
