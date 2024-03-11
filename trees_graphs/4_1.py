from collections import deque
from graphs_utils import Graph, Node

def route_between_nodes(graph, source_val, dest_val):
    if (source_val not in graph.nodes) or (dest_val not in graph.nodes):
        return "Source or destination not in graph"
    else: 
        source, dest = graph.nodes[source_val], graph.nodes[dest_val]
        return bfs_route_finder(source, dest)

def bfs_route_finder(source, dest):
    # 1. Create queue and visited tracker
    queue = deque()
    visited = []
    # 2. Add source to visited
    visited.append(source)
    # 3. Add source to queue
    queue.append(source)
    
    # 4. While the queue is not empty
    while (len(queue) > 0):
        # 5. dequeue()
        cur = queue.popleft()
        # 6. Visit the dequeued node --> NOT NECESSARY
        # 7. For neighbour of dequeued node
        for neighbour in cur.edges.keys():
            # 8a. If the neighbour == dest, return true (there is a route)
            if (neighbour == dest):
                return True
            # 8b. If the neighbour is unvisited,
            if (neighbour not in visited):
                # 9. Add neighbour to visited
                visited.append(neighbour)
                # 10. Add neighbour to queue
                queue.append(neighbour)
    
    # 11. Return False if you make it here
    return False
                
# Create graph
tester = Graph(True)
# Create nodes
nodes = [Node(val) for val in ['a', 'b', 'c', 'd', 'e', 'f']]
# Add nodes to graph
for node in nodes:
    tester.add_node(node)
# Connect nodes
tester.add_edge(tester.nodes['b'], tester.nodes['c'])
tester.add_edge(tester.nodes['b'], tester.nodes['d'])
tester.add_edge(tester.nodes['c'], tester.nodes['e'])
tester.add_edge(tester.nodes['c'], tester.nodes['f'])
tester.add_edge(tester.nodes['f'], tester.nodes['e'])

# Print graph
tester.print()

# Test cases:
print(route_between_nodes(tester, 'b', 'f'))    # Expected: True
print(route_between_nodes(tester, 'a', 'e'))    # Expected: False
print(route_between_nodes(tester, 'f', 'b'))    # Expected: False

"""
Runtime Analysis:
    if block: O(s + d)
    else block:
        bfs_route_finder: O(n*k) ??
    
    >> O(n*k) ??
    Space complexity: O(n)
"""
