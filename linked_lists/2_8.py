from linked_list_utils import LinkedList, Node

def loop_detection(ll):
    node_tracker = {}
    cur = ll.head
    while (cur):
        if (cur not in node_tracker):
            node_tracker[cur] = 1
            cur = cur.next
        else:
            return cur

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

# Create nodes
nodes = create_node([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])

# Create circular linked list
tester = create_linked_list([nodes[0], nodes[1], nodes[2], nodes[3], nodes[4]])
cur, counter = tester.head, 0
while (cur):
    if (counter == 4):
        cur.next = tester.head
        break
    cur = cur.next
    counter += 1

print("Node value: " + str(loop_detection(tester).value))
print("Node next: " + str(loop_detection(tester).next.value))

"""
Runtime Analysis: 
    >> O(n)
    Space complexity: O(n)
    
"""
