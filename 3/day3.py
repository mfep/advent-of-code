def parse_wire(raw_string):
    dir_list = raw_string.split(',')
    return [(instr[0], int(instr[1:])) for instr in dir_list]

def get_direction(dir_char):
    if dir_char == 'L':
        return (-1, 0)
    elif dir_char == 'R':
        return (1, 0)
    elif dir_char == 'U':
        return (0, 1)
    elif dir_char == 'D':
        return (0, -1)
    else:
        raise Exception('unexpected direction char')

def get_wire_locations(wiredata):
    locations = {}
    current_pos = (0, 0)
    wire_length = 0
    for dir_char,length in wiredata:
        direction = get_direction(dir_char)
        for step in range(1, length + 1):
            current_pos = (current_pos[0] + direction[0], current_pos[1] + direction[1])
            wire_length += 1
            locations[current_pos] = wire_length
    return locations

def get_intersections(locations_a, locations_b):
    intersections = {}
    for loc_a in locations_a.keys():
        if loc_a in locations_b.keys():
            intersections[loc_a] = locations_a[loc_a] + locations_b[loc_a]
    return intersections

def manhattan(xy):
    return abs(xy[0]) + abs(xy[1])

def closest_intersection(intersections):
    return min([manhattan(xy) for xy in intersections.keys()])

def shortest_intersection(intersections):
    return min(intersections.values())

with open('day3.txt') as datafile:
    wiredata1 = parse_wire(datafile.readline())
    wiredata2 = parse_wire(datafile.readline())

loc1 = get_wire_locations(wiredata1)
loc2 = get_wire_locations(wiredata2)

intersections = get_intersections(loc1, loc2)

# part one
print(closest_intersection(intersections))

# part two
print(shortest_intersection(intersections))
