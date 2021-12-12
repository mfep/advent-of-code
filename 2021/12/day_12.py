import networkx as nx
from collections import defaultdict

graph = nx.Graph()

with open('day_12.txt') as f:
  for line in f.readlines():
    line = line.strip()
    dash_idx = line.index('-')
    node1 = line[:dash_idx]
    node2 = line[dash_idx+1:]
    graph.add_edge(node1, node2)

paths = []
def process(path, visited_small):
  global graph
  global paths
  current_node = path[-1]
  for adjacent_node in graph.adj[current_node]:
    if adjacent_node == 'end':
      new_path = path.copy()
      new_path.append(adjacent_node)
      paths.append(new_path)
    elif adjacent_node not in visited_small:
      new_path = path.copy()
      new_path.append(adjacent_node)
      new_visited_small = visited_small.copy()
      if adjacent_node.islower():
        new_visited_small.add(adjacent_node)
      process(new_path, new_visited_small)

process(['start'], set(['start']))

print(len(paths))

# part 2

paths = []
def process2(path, visited_small, double_selected):
  global graph
  global paths
  current_node = path[-1]
  for adjacent_node in graph.adj[current_node]:
    if adjacent_node == 'start':
      continue
    elif adjacent_node == 'end':
      new_path = path.copy()
      new_path.append(adjacent_node)
      paths.append(new_path)
    elif adjacent_node not in visited_small or not double_selected:
      if adjacent_node in visited_small:
        new_double_selected = adjacent_node
      elif double_selected:
        new_double_selected = double_selected
      else:
        new_double_selected = None
      new_path = path.copy()
      new_path.append(adjacent_node)
      new_visited_small = visited_small.copy()
      if adjacent_node.islower():
        new_visited_small.add(adjacent_node)
      process2(new_path, new_visited_small, new_double_selected)

process2(['start'], set(), None)

print(len(paths))
