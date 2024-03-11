from linked_list_utils import LinkedList

def palindrome(ll):    
    # Special case: Empty list or 1 element
    if (not(ll.head) or not(ll.head.next)):
        return True
    
    # Flip linked list
    ll_flipped = flip(ll)
    
    # Check if lists are now the same
    return are_equal(ll, ll_flipped)

def flip(ll):
    cur = ll.head
    flipped = LinkedList()
    while (cur):
        flipped.insert_at_head(cur.value)
        cur = cur.next
    return flipped
    
def are_equal(a, b):
    # Parse a and b with pointers simultaneously to check if they are equal
    cur_a, cur_b = a.head, b.head
    
    # While both pointers are not None
    while (cur_a and cur_b):
        # If they are the same, update pointers and continue
        if (cur_a.value == cur_b.value):
            cur_a = cur_a.next
            cur_b = cur_b.next
        # Else, return False
        else:
            return False
    return True

def create_linked_list(arr):
    ll = LinkedList()
    for a in arr:
        ll.insert_at_head(a)
    return ll


# Creating testing operands
operand_1 = create_linked_list([6, 1, 6])
operand_2 = create_linked_list([8, 1, 6, 8])
operand_3 = create_linked_list([])
operand_4 = create_linked_list([8])

# 1. Testing non-empty list that is a palindrome
print(palindrome(operand_1))

# 2. Testing non-empty list that is NOT a palindrome
print(palindrome(operand_2))

# 3. Testing empty list case
print(palindrome(operand_3))

# 4. Testing single-element list case
print(palindrome(operand_4))

"""
Runtime Analysis:   
    flip(): O(n)
    are_equal(): O(n)
    
    n = length of b
 
    >> O(n)
    Space complexity: O(n)
    
"""
