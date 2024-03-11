from trees_utils import BinarySearchTreeNode

class BST(BinarySearchTreeNode):
    def __init__(self, data=None):
        BinarySearchTreeNode.__init__(self, data)
        self.parent = None

def successor(root, x, returnNext=False):
    """
        Idea: Carry out in_order traversal while keeping track of whether you want to return the next
        Recurse until you reach x or the end
        If you reach x, set returnNext to True
        If return_next is True, return data
        If you reach the end, return None
    """
    pass

bst = BST()
for num in [6, 3, 9, 2, 5, 8, 10, 1, 4, 7]:
    bst.insert(num)

print(successor(bst, 2))
print(successor(bst, 6))
print(successor(bst, 10))
print(successor(bst, 12))

"""
-- INCOMPLETE --

Runtime Analysis: Theorised to be O(n)
"""

