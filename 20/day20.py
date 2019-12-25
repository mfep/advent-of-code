import networkx as nx
import sys
from collections import defaultdict

sys.setrecursionlimit(100000000)

def direct_paths(lines):
    world = nx.Graph()
    for row,line in enumerate(lines):
        for col,obj in enumerate(line):
            if obj != '.':
                continue
            if line[col - 1] == '.':
                world.add_edge((col, row), (col - 1, row))
            if lines[row - 1][col] == '.':
                world.add_edge((col, row), (col, row - 1))
    return world

def search_portals(lines):
    portals = defaultdict(list)
    for row,line in enumerate(lines[:-1]):
        for col,obj in enumerate(line):
            if not obj.isalpha():
                continue
            if line[col + 1].isalpha():
                portals[obj + line[col + 1]].append((col + 2, row) if line[col + 2] == '.' else (col - 1, row))
            elif lines[row + 1][col].isalpha():
                portals[obj + lines[row + 1][col]].append((col, row - 1) if lines[row - 1][col] == '.' else (col, row + 2))
    return portals

def portal_paths(portal_list, world):
    for portals in portal_list.values():
        if len(portals) == 1:
            continue
        assert len(portals) == 2
        world.add_edge(portals[0], portals[1])

with open('day20.txt') as f:
    lines = f.readlines()
width = len(lines[0])
height = len(lines)
W = direct_paths(lines)
portal_connections = search_portals(lines)
portal_paths(portal_connections, W)
path = nx.dijkstra_path(W, portal_connections['AA'][0], portal_connections['ZZ'][0])
print('part one', len(path) - 1)

def is_outer(x, y):
    return x == 2 or y == 2 or x == width - 4 or y == height - 3

def accessible_portals(pos, portal_list, world):
    acc_outer, acc_inner = {}, {}
    for portal_id in portal_list.keys():
        if portal_id == 'AA':
            continue
        for portal_pos in portal_list[portal_id]:
            if portal_pos == pos:
                continue
            try:
                dst = nx.dijkstra_path_length(world, pos, portal_pos)
                accessible = acc_outer if is_outer(*portal_pos) else acc_inner
                assert portal_id not in accessible
                accessible[portal_id] = dst, portal_pos
            except nx.NetworkXNoPath:
                pass
    return acc_outer, acc_inner

def get_other_exit(portal_list, portal_id, current_pos):
    return [pos for pos in portal_list[portal_id] if pos != current_pos][0]

def pathfind_multilevel(pos, level, portal_list, world, history):
    print(level)
    def search_paths(accessible, dlevel):
        paths = []
        for pid, dst_pos in accessible.items():
            if pid == 'ZZ' or (pid, dst_pos[1], level) in history:
                continue
            distance_to_goal = pathfind_multilevel(get_other_exit(portal_list, pid, dst_pos[1]), level + dlevel, portal_list, world, history.union([(pid, dst_pos[1], level)]))
            paths.append(distance_to_goal + dst_pos[0] + 1 if distance_to_goal else None)
        paths = [path for path in paths if path]
        return min(paths) if paths else None

    acc_outer, acc_inner = accessible_portals(pos, portal_list, world)
    if level == 0 and 'ZZ' in acc_outer:
        return acc_outer['ZZ'][0]
    if level != 0 and acc_outer:
        outer_found = search_paths(acc_outer, -1)
        if outer_found:
            return outer_found
    return search_paths(acc_inner, 1)

W = direct_paths(lines)
result = pathfind_multilevel(portal_connections['AA'][0], 0, portal_connections, W, set())
print('part two', result)