from linked_list_utils import LinkedList

def palindrome(a, b):
    # Flip b in-place
    flip_in_place(b)
    
    # Check if lists are now the same
    return are_equal(a, b)

def flip_in_place(ll):
    # Check if list is empty
    if (not ll.head):
        return ll
    
    prev, cur, next = None, ll.head, ll.head.next
    
    # Continue until the end of the linked list (i.e. next == None)
    while (next):
        # Move all pointers one place forward
        prev, cur, next = cur, next, next.next
        # Point cur to prev
        cur.next = prev
        # Point previous HEAD to None
        if (prev.next == cur):
            prev.next = None
    # Update the HEAD reference to the previous last element which is now stored in cur
    ll.head = cur

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
        
    # If both pointers point to None (i.e. they are the same length), return True. Else, return False
    return True if ((not cur_a) and (not cur_b)) else False

def create_linked_list(arr):
    ll = LinkedList()
    for a in arr:
        ll.insert_at_head(a)
    return ll


# Creating testing operands
operand_1 = create_linked_list([6, 1, 7])
operand_2 = create_linked_list([7, 1, 6])
operand_3 = create_linked_list([7, 1, 6, 8])
operand_4 = create_linked_list([])

# 1. Testing non-empty lists that are palindromes
print(palindrome(operand_1, operand_2))     # Expected: True

# 2. Testing non-empty lists that are NOT palindromes
print(palindrome(operand_1, operand_3))

# 3. Testing empty list case
print(palindrome(operand_1, operand_4))

"""
Runtime Analysis:   
    flip_in_place(): O(b)
    are_equal(): O(n), where n is the shorter of a and b
 
    >> O(n)
    Space complexity: O(n)
    
    THOUGHTS:
    - I solved the wrong fucking problem.
    - This reminds me of that one CRS CA where I narrated the Triumphant Entry instead of the transfiguration because I misread the instructions.
    - Jesus Christ, wow. I've made the changes but... ye.
    
"""
