from linked_list_utils import LinkedList, Node

def delete_middle(middle):
    # Replace value with neighbour's value
    middle.value = middle.next.value
    
    # Delete the neighbour, which has now been "copied"
    middle.next = middle.next.next or None
    
    
tester = LinkedList()
for x in [4, 7, 3, 12, 5, 17, 9]:
    tester.insert_at_head(x)
    
middle_basic, middle_second, middle_second_to_last = tester.get_node(12), tester.get_node(17), tester.get_node(7)

for node in [middle_basic, middle_second, middle_second_to_last]:
    print(tester)
    print("Node value: {} | Node next: {}".format(node.value, node.next.value))
    delete_middle(node)
    print(tester)
    print()

"""
THOUGHTS: 
    I am a fraud. After thinking about the problem for one minute, I decided I couldn't think of a way to solve it and went to the solution page. 
    Very, very deplorable.
    The solution they suggested that was to replace the value of the middle with the value of the next and return
        and it's a O(1) solution
    I feel extremely pathetic, I cannot lie.
    I am just going to implement it straight away

Runtime Analysis:    
    >> O(1)
    CONCLUSION: Consider values as well as nodes. Yes, we interact with nodes but what happens if you cannot?
    
"""
