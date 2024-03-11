from trees_utils import BinarySearchTreeNode

def minimal_tree(arr):
    if (len(arr) == 0):
        return None
    elif (len(arr) == 1):
        return BinarySearchTreeNode(arr[0])
    else:
        bst = BinarySearchTreeNode()
        return insert_middle(bst, arr)

def insert_middle(bst, arr):
    # 1. If arr has nothing in it, return
    if (len(arr) == 0):
        return
    # 2. If arr has 1 element, insert that one element and return
    elif (len(arr) == 1):
        bst.insert(arr[0])
        return bst
    # 3. Else
    else:
        # 4. Get the index of the middle index and the length
        middle_index, length = len(arr)//2, len(arr)
        # 5. Get the left half, middle element and right half
        left, middle, right = arr[0:middle_index], arr[middle_index], arr[middle_index+1:length]
        # 6. Insert middle element into tree
        bst.insert(middle)
        print(middle)
        # 7. Call function recursively on left and right halves
        insert_middle(bst, left)
        insert_middle(bst, right)
        return bst

# Create elements
elements = [x for x in range(1, 11)]
# Create minimal-height MST with elements
minimal_bst = minimal_tree(elements)
# Print out traversals to ascertain whether its correct
print("In-order traversal: ", end="")
minimal_bst.in_order()
print("END")
print("Pre-order traversal: ", end="")
minimal_bst.pre_order()
print("END")
print("Post-order traversal: ", end="")
minimal_bst.post_order()
print("END")

# Compare results of method to result of manual insert
bst = BinarySearchTreeNode()
for num in [6, 3, 9, 2, 5, 8, 10, 1, 4, 7]:
    bst.insert(num)
print("\nIn-order traversal: ", end="")
bst.in_order()
print("END")
print("Pre-order traversal: ", end="")
bst.pre_order()
print("END")
print("Post-order traversal: ", end="")
bst.post_order()
print("END")    
    
"""
Runtime Analysis:
    Recursive calls (2 branches)
    Number of divisions = log n 
    
    >> O(2^(logn)) = O(n) ?????
    Space complexity: ??
    
    THOUGHTS: I really do not understand runtime analysis for graphs and trees
"""
