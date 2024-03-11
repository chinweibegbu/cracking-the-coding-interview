from linked_list_utils import LinkedList

# Ver. 3: Using a list and indexing to reduce the O(n-k) operation to O(1)
def return_kth_to_last(ll, k):
    # Special case #1: Empty linked list
    if (not ll.head): return None
        
    # Get length, n,  of linked list (ll)
    n, elements = get_length(ll)
    
    # Special case #2: k is larger than n
    if (k > n): return None
    
    # Return the value at position k_index in the elements array
    kth_index = n-k
    return elements[kth_index]

def get_length(ll):
    n = 0
    elements = []
    cur = ll.head
    while (cur):
        elements.append(cur.value)
        n += 1
        cur = cur.next
    return n, elements

test_basic = LinkedList()
for x in [4, 7, 3, 12, 5, 17, 9]:
    test_basic.insert_at_head(x)
print(test_basic)
print(return_kth_to_last(test_basic, 3))

print()
print(test_basic)
print(return_kth_to_last(test_basic, 11))

test_empty = LinkedList()
print()
print(test_empty)
print(return_kth_to_last(test_empty, 8))

"""
Runtime Analysis:
    get_length(): O(n)
    Getting the kth element: O(1)
    
    >> O(n)
    >> Space complexity: O(n)
    CONCLUSION: 
    - Addresses a bottleneck but does not affect the overall time complexity of the function
    - Simpler and less verbose than V1 and V2
    - Space complexity is worse than with V1 and V2 because of the need for an array of size n
    POTENTIAL IMPROVEMENTS:
    - Do input data validation e.g. check whether it is an int, whether it is positive or negative, etc.
"""
