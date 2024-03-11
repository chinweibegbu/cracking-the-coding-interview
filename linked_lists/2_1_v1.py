from linked_list_utils import LinkedList, Node

def remove_dups(linked_list):
    unique_values = get_unique_values(linked_list)
    return create_linked_list(unique_values)

def get_unique_values(linked_list):
    unique_values = []
    cur = linked_list.head
    while (cur):
        if (cur.value not in unique_values):
            unique_values.append(cur.value)
        cur = cur.next
    return unique_values
    
def create_linked_list(values):
    new_linked_list = LinkedList()
    for i in range(0, len(values)):
        new_linked_list.insert_at_head(values[i])
    return new_linked_list

tester = create_linked_list([5,17,8,5,32,5,2,10])
print(tester)
print(remove_dups(tester))

"""
Runtime Analysis:
    get_unique_values(): O(n^2)
    create_linked_list(): O(n)
    
    >> O(n^2)
"""
