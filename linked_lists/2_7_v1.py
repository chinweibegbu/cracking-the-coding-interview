from linked_list_utils import LinkedList, Node

def intersection(a, b):
    node_tracker = {}
    cur_a, cur_b = a.head, b.head
    
    # If either list is empty, there is no intersection
    if ((not cur_a) or (not cur_b)): return False
    
    # Parse a to track all nodes
    while (cur_a):
        if (cur_a not in node_tracker):
            node_tracker[cur_a] = 1
        else:
            node_tracker[cur_a] = node_tracker[cur_a] + 1
        cur_a = cur_a.next
    
    # Parse b until you reach an intersection or reach the end
    while (cur_b): 
        if (cur_b in node_tracker):
            # If b has a node that is in a, there is an intersection
            return True
        cur_b = cur_b.next
    # If no node in b is in a, there is no intersection
    return False

def create_node(elements):
    return [Node(element) for element in elements]

def create_linked_list(elements):
    ll = LinkedList()
    for i in range(len(elements)-1, -1, -1):
        # Add node to beginning of linked list
        new_head = elements[i]
        new_head.next = ll.head
        ll.head = new_head
    return ll

a_b_nodes = create_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11])
c_nodes = create_node([12, 13, 14])
a = create_linked_list(a_b_nodes[0:])
b = create_linked_list(a_b_nodes[4:9])
c = create_linked_list(c_nodes)
print("a >>> " + str(a))
print("b >>> " + str(b))
print("c >>> " + str(c))

print(intersection(a, b))   # Expected: True
print(intersection(a, c))   # Expected: False

"""
Runtime Analysis: 
    >> O(n)
    Space complexity: O(n)
    
    THOUGHTS: Just realised that I did not actually return the intersecting node
    
"""
