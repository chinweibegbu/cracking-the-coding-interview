from trees_utils import BinarySearchTreeNode

class BST(BinarySearchTreeNode):
    def __init__(self, data=None):
        BinarySearchTreeNode.__init__(self, data)
        self.parent = None

def successor(root, x):
    result = traverse(root, x, [])
    for i in range(len(result)):
        if ((result[i] == x) and (i < len(result)-1)):
            return result[i+1]
    return None
    
def traverse(root, x, result):
    if (root.left):
        traverse(root.left, x, result)
    result.append(root.data)
    if (root.right):
        traverse(root.right, x, result)
    return result

bst = BST()
for num in [6, 3, 9, 2, 5, 8, 10, 1, 4, 7]:
    bst.insert(num)

print(successor(bst, 2))
print(successor(bst, 6))
print(successor(bst, 10))
print(successor(bst, 12))
