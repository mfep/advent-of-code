import re
from itertools import product

def parse_line(line):
    query = r'<x=(-?\d+), y=(-?\d+), z=(-?\d+)>'
    matches = re.search(query, line)
    return [int(matches[1]), int(matches[2]), int(matches[3])]

with open('day12.txt') as file:
    data = [parse_line(line) for line in file.readlines()]

def cmp(x, y):
    return (x > y) - (x < y)

def simulate(initial_positions, iterations):
    positions = initial_positions.copy()
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

print('part one', energy(*simulate(data, 1000)))
