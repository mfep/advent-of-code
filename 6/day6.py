input = """COM)B
B)C
C)D
D)E
E)F
B)G
G)H
D)I
E)J
J)K
K)L"""

with open('day6.txt') as f:
    input = ''.join(f.readlines())

def build_tree(inp):
    data = {}
    for line in inp.splitlines():
        center,_,orbital = line.partition(')')
        if center not in data: data[center] = []
        data[center].append(orbital)
    return data


orbitnums = []
def count_orbitnum(tree, current, depth):
    orbitnums.append(depth)
    if current in tree:
        for orbital in tree[current]:
            count_orbitnum(tree, orbital, depth + 1)
    
tree = build_tree(input)
count_orbitnum(tree, 'COM', 0)
print('part one', sum(orbitnums))

def build_parent_tree(inp):
    data = {}
    for line in inp.splitlines():
        center,_,orbital = line.partition(')')
        data[orbital] = center
    return data

# input = """COM)B
# B)C
# C)D
# D)E
# E)F
# B)G
# G)H
# D)I
# E)J
# J)K
# K)L
# K)YOU
# I)SAN"""

parent_tree = build_parent_tree(input)

def build_path(parent_tree, current):
    path = []
    length = 0
    while current in parent_tree:
        current = parent_tree[current]
        length += 1
        path.append((current, length))
    return path

you_path = build_path(parent_tree, 'YOU')
san_path = build_path(parent_tree, 'SAN')

def distance():
    for ycurrent,ylength in you_path:
        for scurrent,slength in san_path:
            if ycurrent == scurrent:
                return ylength + slength - 2

print('part two', distance())
