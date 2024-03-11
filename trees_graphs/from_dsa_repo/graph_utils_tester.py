from random import randrange
from graph_utils import *

def print_graph(graph):
  for vertex in graph.vertices:
    print(vertex + " connected to")
    vertex_neighbors = graph.vertices[vertex].edges
    if len(vertex_neighbors) == 0:
      print("No edges!")
    for adjacent_vertex in vertex_neighbors:
      print("=> " + adjacent_vertex)


# Create an undirected graph
g = Graph(False)
vertices = []
for val in ['a', 'b', 'c', 'd', 'e', 'f', 'g']:
  vertex = Vertex(val)
  vertices.append(vertex)
  g.add_vertex(vertex)

for v in range(len(vertices)):
  v_idx = randrange(0, len(vertices) - 1)
  v1 = vertices[v_idx]
  v_idx = randrange(0, len(vertices) - 1)
  v2 = vertices[v_idx]
  g.add_edge(v1, v2, randrange(1, 10))
  
print_graph(g)

# Carry out DFS on graph
print("\nDFS Traversal:")
start_vertex = g.vertices['b']
g.dfs(start_vertex)
print("END")

# Carry out BFS on graph
