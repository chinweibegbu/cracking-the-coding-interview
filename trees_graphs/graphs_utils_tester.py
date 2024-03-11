from graphs_utils import Graph, Node

# Create graph   
alphabet = Graph()
# Create nodes
values = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
alphabet_nodes = [Node(val) for val in values]

# Add nodes to graph
for node in alphabet_nodes:
    alphabet.add_node(node)

# Connect nodes
alphabet.add_edge(alphabet.nodes['a'], alphabet.nodes['b'], 6)
alphabet.add_edge(alphabet.nodes['a'], alphabet.nodes['g'], 10)
alphabet.add_edge(alphabet.nodes['b'], alphabet.nodes['c'], 2)
alphabet.add_edge(alphabet.nodes['c'], alphabet.nodes['d'], 30)
alphabet.add_edge(alphabet.nodes['d'], alphabet.nodes['e'], 10)
alphabet.add_edge(alphabet.nodes['d'], alphabet.nodes['f'], 22)
alphabet.add_edge(alphabet.nodes['e'], alphabet.nodes['f'], 15)
alphabet.add_edge(alphabet.nodes['e'], alphabet.nodes['g'], 50)
alphabet.add_edge(alphabet.nodes['f'], alphabet.nodes['g'], 8)

# Print out all nodes and edges
alphabet.print()

# Carry out DFS
alphabet.dfs_traversal("a")

# Create another graph   
numbers = Graph(True)
# Create nodes
number_nodes = [Node(val) for val in range(6)]

# Add nodes to graph
for node in number_nodes:
    numbers.add_node(node)

# Connect nodes
numbers.add_edge(numbers.nodes[0], numbers.nodes[1])
numbers.add_edge(numbers.nodes[0], numbers.nodes[4])
numbers.add_edge(numbers.nodes[0], numbers.nodes[5])
numbers.add_edge(numbers.nodes[1], numbers.nodes[3])
numbers.add_edge(numbers.nodes[1], numbers.nodes[4])
numbers.add_edge(numbers.nodes[2], numbers.nodes[1])
numbers.add_edge(numbers.nodes[3], numbers.nodes[2])
numbers.add_edge(numbers.nodes[3], numbers.nodes[4])

# Print out all nodes and edges
numbers.print()

# Carry out DFS
numbers.dfs_traversal(0)
numbers.bfs_traversal(0)
# numbers.bfs_traversal(9)

