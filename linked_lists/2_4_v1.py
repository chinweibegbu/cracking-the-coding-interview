from linked_list_utils import LinkedList

def partition(ll, x):
    # Parse linked list to get all elements
    elements = get_elements(ll)
    
    # Sort the elements
    sorted_elements = sort_elements(elements)
    
    # Create a new linked list with the sorted elements
    partitioned_linked_list = create_linked_list(sorted_elements)
    
    # Return the new linked list
    return partitioned_linked_list
    
def get_elements(ll):
    elements = []
    cur = ll.head
    while (cur):
        elements.append(cur.value)
        cur = cur.next
    return elements

def sort_elements(elements):
    return sorted(elements)

def create_linked_list(elements):
    new_linked_list = LinkedList()
    for i in range(len(elements)-1, -1, -1):
        new_linked_list.insert_at_head(elements[i])
    return new_linked_list

tester = LinkedList()
for x in [4, 7, 3, 12, 5, 17, 9]:
    tester.insert_at_head(x)
print(tester)
print(partition(tester, 12))

"""
Runtime Analysis:   
    get_elements(): O(n)
    sort_elements(): O(n logn)
    create_linked_list(): O(n)
 
    >> O(n logn)
    Space complexity: O(n)
    
    CONCLUSION:
    - While sorting does solve the problem, I do not use the partition element (x) in this approach, which makes me think I am doing something wrong
    - I think I could reduce the time complexity by using a pointer approach and partitioning the linked list as I traverse once
    - This would reduce the overall time complexity to O(n)
    
"""
