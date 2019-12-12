from math import gcd
import re
from itertools import product, count

def parse_line(line):
    query = r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>'
    matches = re.search(query, line)
    return [int(matches[1]), int(matches[2]), int(matches[3])]

with open('day12.txt') as file:
    data = [parse_line(line) for line in file.readlines()]

def cmp(x, y):
    return (x > y) - (x < y)

def simulate(initial_positions, iterations):
    positions = [pos.copy() for pos in initial_positions]
    velocities = [[0,0,0] for _ in positions]
    calc_pairs = list(product(range(len(positions)), range(len(positions)), range(3)))
    for _ in range(iterations):
        # update velocities
        for moon1, moon2, coord in calc_pairs:
            coord1 = positions[moon1][coord]
            coord2 = positions[moon2][coord]
            velocities[moon1][coord] += cmp(coord2, coord1)
        # update positions
        for idx, vel in enumerate(velocities):
            positions[idx][0] += vel[0]
            positions[idx][1] += vel[1]
            positions[idx][2] += vel[2]
    return positions, velocities

def energy(positions, velocities):
    return sum(sum(abs(p) for p in pos) * sum(abs(v) for v in vel) for pos, vel in zip(positions, velocities))

def all_of_index_equal(a, b, index):
    return all(ea[index] == eb[index] for ea,eb in zip(a, b))

def simulate_loop(initial_positions):
    positions = [pos.copy() for pos in initial_positions]
    initial_velocities = [[0,0,0] for _ in positions]
    velocities = [[0,0,0] for _ in positions]
    calc_pairs = list(product(range(len(positions)), range(len(positions)), range(3)))
    dim_periods = {}
    for iter_idx in count(1):
        # update velocities
        for moon1, moon2, coord in calc_pairs:
            coord1 = positions[moon1][coord]
            coord2 = positions[moon2][coord]
            velocities[moon1][coord] += cmp(coord2, coord1)
        # update positions
        for idx, vel in enumerate(velocities):
            positions[idx][0] += vel[0]
            positions[idx][1] += vel[1]
            positions[idx][2] += vel[2]
        if iter_idx == 1:
            continue
        for dim in range(3):
            if all_of_index_equal(positions, initial_positions, dim) and all_of_index_equal(velocities, initial_velocities, dim) and dim not in dim_periods.keys():
                dim_periods[dim] = iter_idx
        if len(dim_periods) is 3:
            return dim_periods

def lcm(a,b):
    return int(a*b/gcd(a,b))

print('part one', energy(*simulate(data, 100)))
periods = simulate_loop(data)
print('part two', lcm(lcm(periods[0], periods[1]), periods[2]))
