from trees_utils import *

# Create binary tree to test traversal functions
a, s, f, t, g, k = BinaryTreeNode("a"), BinaryTreeNode("s"), BinaryTreeNode("f"),BinaryTreeNode("t"), BinaryTreeNode("g"), BinaryTreeNode("k")
g.left = k
f.left = g
f.right = t
a.left = s
a.right = f
print("In-order Traversal:")
a.in_order()
print("END\n")

print("Pre-order Traversal:")
a.pre_order()
print("END\n")

print("Post-order Traversal:")
a.post_order()
print("END\n")

# Create binary search tree and insert into it
bst = BinarySearchTreeNode()
for num in [8, 12, 31, 2, 25, 14, 75]:
    bst.insert(num)
    bst.in_order()
    print("END")
