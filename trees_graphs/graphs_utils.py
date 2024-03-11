from collections import deque

class Node:
    def __init__(self, value):
        self.value = value
        # self.children = []
        self.edges = {}     # Maps neighbouring nodes to their weights
    
    # def add_child(self, node):
    #     self.children.append(node)
    
    def add_edge(self, destination, weight):
        self.edges[destination] = weight

class Graph:
    def __init__(self, directed=False):
        self.nodes = {}
        self.directed = directed
    
    def add_node(self, node):
        self.nodes[node.value] = node
        
    def add_edge(self, source, destination, weight=0):
        source.add_edge(destination, weight)
        if (not self.directed):
            destination.add_edge(source, weight)

    def dfs_traversal(self, start_value):
        if (start_value not in self.nodes):
            print("ERROR: Node with value {} not in graph".format(start_value))
            return
        
        print("DFS Traversal: ", end="")
        self.dfs(self.nodes[start_value])
        print("END\n")
        
    def dfs(self, node, visited=[]):
        # 1. Mark node as visited
        visited.append(node)
        # 2. Visit node
        print("{} > ".format(node.value), end="")
        # 3. For UNVISITED neighbour of node...
        for neighbour in node.edges.keys():
            # ...Repeat
            if (neighbour not in visited):
                self.dfs(neighbour, visited)
    
    def bfs_traversal(self, start_value):
        if (start_value not in self.nodes):
            print("ERROR: Node with value {} not in graph".format(start_value))
            return
        
        print("BFS Traversal: ", end="")
        self.bfs(self.nodes[start_value])
        print("END\n")
        
    def bfs(self, node):
        # 1. Create queue and visited array
        queue = deque()
        visited = []
        # 2. Mark node as visited
        visited.append(node)
        # 3. Add first node to queue
        queue.append(node)
        
        # 3. While the queue is not empty:
        while (len(queue) > 0):
            # 4. Get first node in the queue
            current_node = queue.popleft()
            # 5. Visit this node
            print("{} > ".format(current_node.value), end="")
            # 6. For each neighbour of currrent node
            for neighbour in current_node.edges.keys():
                # 7. If neighbour is unvisited...
                if (neighbour not in visited):
                    # 8. ...Mark node as visited
                    visited.append(neighbour)
                    # 9. ...Add to queue
                    queue.append(neighbour)
    
    def print(self):
        for node in self.nodes.values():
            print("{} >> Connected to: ".format(node.value), end="")
            if (len(node.edges) == 0): 
                print("N/A")
                continue
            for neighbour in node.edges.keys():
                neighbour_value = neighbour.value
                edge_weight = node.edges[neighbour]
                print("{}({}) ".format(neighbour_value, edge_weight), end="")
            print()
        print()
