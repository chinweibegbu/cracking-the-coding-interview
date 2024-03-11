from trees_utils import BinaryTreeNode

def validate_bst(root):
    if ((not root.left) and (not root.right)):
        return True
    
    if (root.left and (root.left.data <= root.data)):
        validate_bst(root.left)
    elif (root.left and (root.left.data > root.data)):
        return False
    
    if (root.right and (root.right.data > root.data)):
        validate_bst(root.right)
    elif (root.right and (root.right.data <= root.data)):
        return False
    
    return True

one, two, three, four = BinaryTreeNode(1), BinaryTreeNode(2), BinaryTreeNode(3), BinaryTreeNode(4)
three.left = one
three.right = four
one.right = two
print(validate_bst(three))      # Expected: True

five, six, seven, eight = BinaryTreeNode(5), BinaryTreeNode(6), BinaryTreeNode(7), BinaryTreeNode(8)
seven.left = six
seven.right = five
five.right = eight
print(validate_bst(seven))      # Expected: False

zero = BinaryTreeNode(0)
print(validate_bst(zero))       # Expected: True

"""
Runtime Analysis:
    Recursive calls (2 branches)
    Number of divisions = log n 
    
    >> O(2^(logn)) = O(n)
    Space complexity: O(n)
"""
