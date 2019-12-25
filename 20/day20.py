import networkx as nx
from collections import defaultdict

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

W = direct_paths(lines)
portal_connections = search_portals(lines)
portal_paths(portal_connections, W)
path = nx.dijkstra_path(W, portal_connections['AA'][0], portal_connections['ZZ'][0])
print('part one', len(path) - 1)
