import networkx as nx

graph = nx.Graph()

max_row = 0
max_col = 0
with open('day_15.txt') as f:
  for row,line in enumerate(f.readlines()):
    max_row = max(row, max_row)
    for col,ch in enumerate(line.strip()):
      max_col = max(col, max_col)
      val = int(ch)
      graph.add_node((col, row), weight=val)
      if row > 0:
        graph.add_edge((col, row), (col, row - 1))
      if col > 0:
        graph.add_edge((col, row), (col - 1, row))

def weight_fun(start, end, attribs):
  return graph.nodes[end]['weight']

path = nx.dijkstra_path(graph, (0, 0), (max_col, max_row), weight=weight_fun)

total = sum(graph.nodes[node]['weight'] for node in path[1:])
print(total)

width = max_col + 1
height = max_row + 1
for tile_y in range(0, 5):
  for tile_x in range(0, 5):
    if tile_y == 0 and tile_x == 0: continue
    for row in range(tile_y * height, (tile_y + 1) * height):
      max_row = max(row, max_row)
      for col in range(tile_x * width, (tile_x + 1) * width):
        max_col = max(col, max_col)
        if col >= width:
          new_weight = graph.nodes[(col - width, row)]['weight'] + 1
        elif row >= height:
          new_weight = graph.nodes[(col, row - height)]['weight'] + 1
        else:
          raise Exception()
        new_weight = 1 if new_weight > 9 else new_weight
        
        graph.add_node((col, row), weight=new_weight)
        if col > 0:
          graph.add_edge((col, row), (col-1, row))
        if row > 0:
          graph.add_edge((col, row), (col, row-1))

path = nx.dijkstra_path(graph, (0, 0), (max_col, max_row), weight=weight_fun)
total = sum(graph.nodes[node]['weight'] for node in path[1:])
print(total)
