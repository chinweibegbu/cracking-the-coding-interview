from linked_list_utils import LinkedList

# Ver. 2: Using a counter + while loop instead of a for loop
def return_kth_to_last(ll, k):
    # Special case #1: Empty linked list
    if (not ll.head): return None
        
    # Get length, n,  of linked list (ll)
    n = get_length(ll)
    
    # Special case #2: k is larger than n
    if (k > n): return None
    
    # Traverse until you get to the kth index
    kth_index = n-k
    counter = 0
    cur = ll.head
    while (cur and (counter < kth_index)):
        cur = cur.next
        counter += 1
    
    # Return cur, which is element at kth_index position
    return cur.value

def get_length(ll):
    n = 0
    cur = ll.head
    while (cur):
        n += 1
        cur = cur.next
    return n

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
    Iterating until kth to last element: O(n-k)
    
    >> O(n)
    >> Space complexity: O(1) - no additional variables increasing as a factor of n
    CONCLUSION: Not different from V1 in terms of time comlpexity, space complexity, correctness, simplicity or verboseness
"""
