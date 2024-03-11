from trees_utils import BinaryTreeNode

def check_balanced(root):
    height, balanced = depth(root)
    return balanced

def depth(root, balanced=True):
    if (root is None):
        return (0, balanced)
    if ((not root.left) and (not root.right)):
        return (1, balanced)
    
    height_left, height_right = depth(root.left, balanced), depth(root.right, balanced)
    if abs(height_left[0] - height_right[0]) > 1:
        balanced = False    
    return (max(height_left[0], height_right[0])+1, balanced)

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

print(check_balanced(a))        # Expected: False 

g.left = None
print(check_balanced(a))        # Expected: True 

c.right = None
a.in_order()
print(check_balanced(a))        # Expected: False (??)

print(check_balanced(g))        # Expected: True

"""
Runtime Analysis:
    Recursive calls (2 branches)
    Number of divisions = log n 
    
    >> O(2^(logn)) = O(n)
    Space complexity: O(n)
"""
