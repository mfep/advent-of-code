import math
from collections import defaultdict

def read_data(path):
    with open(path) as f:
        lines = f.readlines()
    data = []
    for row, line in enumerate(lines):
        for col, char in enumerate(line.strip()):
            if char is '#':
                data.append((col, row))
    return data

def count_blocked(cx, cy, data):
    blocked_directions = defaultdict(lambda: [])
    sorted_data = sorted(data, key=lambda xy: abs(cx - xy[0]) + abs(cy - xy[1]))
    for x,y in sorted_data:
        diff = (x - cx, y - cy)
        gcd = math.gcd(diff[0], diff[1])
        if gcd == 0: continue
        diff_div = (int(diff[0] / gcd), int(diff[1] / gcd))
        blocked_directions[diff_div].append((x, y))
    return blocked_directions

def max_blocked(data):
    return max([count_blocked(cx, cy, data) for cx,cy in data], key=len)

def simulate_laser(station_data, iterations):
    sorted_dirs = sorted(station_data.keys(), key=lambda xy: math.atan2(xy[0],xy[1]), reverse=True)
    last = None
    for idx in range(iterations):
        direction = sorted_dirs[idx % len(sorted_dirs)]
        dir_list = station_data[direction]
        if dir_list:
            last = dir_list.pop(0)
    return last


station_data = max_blocked(read_data('day10.txt'))
print('part one', len(station_data))
print('part two', simulate_laser(station_data, 200))
