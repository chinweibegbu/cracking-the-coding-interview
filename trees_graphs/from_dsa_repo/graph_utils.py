class Vertex:
  def __init__(self, value):
    self.value = value
    self.edges = {}
    self.visited = False

  def add_edge(self, vertex, weight = 0):
    print(f"Connecting {vertex} to {self.value}")
    self.edges[vertex] = weight

  def get_edges(self):
    return list(self.edges.keys())

  def __eq__(self, other):
    return self.value == other.value

  def __ne__(self, other):
    return self.value != other.value
  
  def __lt__(self, other):
    return ord(self.value[0]) < ord(other.value[0])
  
  def __le__(self, other):
    return ord(self.value[0]) <= ord(other.value[0])
  
  def __gt__(self, other):
    return ord(self.value[0]) > ord(other.value[0])
  
  def __ge__(self, other):
    return ord(self.value[0]) >= ord(other.value[0])

class Graph:
  def __init__(self, directed = False):
    self.vertices = {}
    self.directed = directed

  def add_vertex(self, vertex):
    print(f"Adding {vertex.value} to graph")
    self.vertices[vertex.value] = vertex

  def add_edge(self, from_vertex, to_vertex, weight = 0):
    self.vertices[from_vertex.value].add_edge(to_vertex.value, weight)
    if not self.directed:
      self.vertices[to_vertex.value].add_edge(from_vertex.value, weight)
  
  def dfs(self, node):
    # 1. If node a is null, return
    if (node is None):
      return
    
    # 2. Visit node a
    print(node.value, end=" > ")
    
    # 3. Set a's visited to True
    node.visited = True
    
    # 4. Iterate through a's neighbours
    for edge in node.get_edges():   
      # 5. Repeat for each unvisited neighbour of a node a
      neighbour = self.vertices[edge]
      if (neighbour.visited == False):
        self.dfs(neighbour)
  
  def bfs(self, start_value):
    pass

  def find_path(self, start_vertex, end_vertex):
    start = [start_vertex]
    seen = {}
    while len(start) > 0:
      current_vertex = start.pop(0)
      seen[current_vertex] = True
      print("Visiting " + current_vertex)
      if current_vertex == end_vertex:
        return True
      else:
        vertices_to_visit = set(self.vertices[current_vertex].edges.keys())
        start += [vertex for vertex in vertices_to_visit if vertex not in seen]
    return False
