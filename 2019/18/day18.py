import networkx as nx
import matplotlib.pyplot as plt

def parse_map(lines):
    def walkable(char):
        return char == '.' or char == '@' or char.islower()
    def connections(x,y):
        connected = []
        for dx,dy in [(-1, 0), (1, 0), (0, -1), (0, 1)]:
            symb = lines[y + dy][x + dx]
            if walkable(symb) or symb.isalpha():
                connected.append((x + dx, y + dy))
        return connected
    world = nx.Graph()
    keys = {}
    doors = {}
    for row,line in enumerate(lines):
        for col,char in enumerate(line):
            if walkable(char):
                if char == '@':
                    start = col, row
                if walkable(line[col - 1]):
                    world.add_edge((col, row), (col - 1, row))
                if walkable(lines[row - 1][col]):
                    world.add_edge((col, row), (col, row - 1))
                if char.islower():
                    keys[char] = col, row
            elif char.isupper():
                doors[char] = ((col, row), connections(col, row))
    return world, keys, doors, start

def reach_key(world, doors, key):
    door = key.upper()
    if door not in doors:
        return
    door_pos, door_connections = doors[key.upper()]
    for connection in door_connections:
        world.add_edge(door_pos, connection)

def reachable_keys(world, keys, pos):
    reachable = []
    for key in keys:
        try:
            dst = nx.dijkstra_path_length(world, pos, keys[key])
            reachable.append((key, dst))
        except nx.NetworkXNoPath:
            pass
    return reachable

def find_loop(world, keys, doors, start):
    to_check_paths = [(world, keys, doors, start, 0)]
    finish_path_lengths = []
    while to_check_paths:
        current_world, current_keys, current_doors, current_pos, current_path_length = to_check_paths.pop()
        if any(current_path_length >= finish_path_length for finish_path_length in finish_path_lengths):
            continue
        if not current_keys:
            assert not current_doors
            finish_path_lengths.append(current_path_length)
            continue
        for reachable_key, dst in reachable_keys(current_world, current_keys, current_pos):
            next_world = current_world.copy()
            next_keys = current_keys.copy()
            next_doors = current_doors.copy()
            next_pos = next_keys[reachable_key]
            next_path_length = current_path_length + dst
            reach_key(next_world, next_doors, reachable_key)
            next_keys.pop(reachable_key)
            if reachable_key.upper() in next_doors:
                next_doors.pop(reachable_key.upper())
            to_check_paths.append((next_world, next_keys, next_doors, next_pos, next_path_length))
    return min(finish_path_lengths)


with open('day18.txt') as f:
    lines = f.readlines()
world, keys, doors, start = parse_map(lines)
print(find_loop(world, keys, doors, start))