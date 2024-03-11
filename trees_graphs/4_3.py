from trees_utils import BinaryTreeNode

class LinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    
    def __str__(self):
        return str(self.data)
    
class LinkedList:
    def __init__(self):
        self.head = None
    
    def insert_at_head(self, data):
        node = LinkedListNode(data)
        node.next = self.head
        self.head = node
    
    def __str__(self):
        cur = self.head
        result = "HEAD > "
        while (cur):
            result += str(cur.data) + " > "
            cur = cur.next
        result += "END"
        return result

def list_of_depths(root):
    # Get dictionary of depths with the nodes at said depths
    nodes_at_depth = get_nodes_at_depth(root)
    
    # For each depth, create a linked list, add its nodes and append to the function result
    result = []
    for depth in nodes_at_depth:
        ll = LinkedList()
        for node in nodes_at_depth[depth]:
            ll.insert_at_head(node)
        result.append(ll)
        
    # Return result
    return result

def get_nodes_at_depth(root, dict={}, depth=0):
    # If depth is not in depth dictionary, add as a key and initialise value to an empty array
    if (depth not in dict):
        dict[depth] = []
    
    # Add the current root to the array of its matching depth
    dict[depth].append(root)
    
    # If the current root has a left, call the function on said left with depth = depth_of_parent + 1
    if (root.left):
        get_nodes_at_depth(root.left, dict, depth+1)
        
    # If the current root has a right, call the function on said left with depth = depth_of_parent + 1
    if (root.right):
        get_nodes_at_depth(root.right, dict, depth+1)
    
    # Return depth dictionary
    return dict

# Create tester nodes
a, b, c, d, e, f, g, h = BinaryTreeNode("a"), BinaryTreeNode("b"), BinaryTreeNode("c"),BinaryTreeNode("d"), BinaryTreeNode("e"), BinaryTreeNode("f"), BinaryTreeNode("g"), BinaryTreeNode("h")
# Create binary tree via edges
a.left = b
a.right = c
b.left = d
c.left = f
c.right = e
f.left = g
g.left = h

# Test
linked_lists = list_of_depths(a)
for linked_list in linked_lists:
    print(linked_list)

"""
Runtime Analysis:
    Recursive calls (2 branches)
    Number of divisions = log n 
    
    >> O(2^(logn)) = O(n)
    Space complexity: O(n)
    
    CONCLUSION: Remember space taken for recursion stack in memory
"""
