from linked_list_utils import LinkedList

# Ver. 2: Using pointers, one traversal and O(1) space complexity
def partition(ll, x):
    # Define pointers
    divider = ll.head if (ll.head.value < x) else None  # Everything after this divider is >= x
    parser = ll.head                                    # Pointer moving through the linked list
    prev = None                                         # Pointer to the previous node of the parser
    
    # Continue until the end of the linked list
    while (parser):
        print("Divider: {} Parser: {} Prev: {}".format((divider.value if divider else "None"), parser.value, (prev.value if prev else "None")))
        if ((parser.value < x) and (not divider)):
            # Swap parser and HEAD values
            parser.value, ll.head.value = ll.head.value, parser.value
            
            # Assign divider to HEAD
            divider = ll.head
        
        if ((parser.value < x) and (divider)):
            # Move to divider pointer
            temp = parser
            if (prev):
                prev.next = temp.next
            else:
                prev = ll.head.next
            temp.next = divider.next
            divider.next = temp
            divider = temp
            
            # Update parser
            parser = prev.next
        else:
            # Update parser and prev
            if (prev):
                prev = prev.next
            else:
                prev = ll.head
            parser = parser.next
            
    return ll

tester = LinkedList()
for x in [1, -1, 2, 10, 5, 8, 5, 3]:
    tester.insert_at_head(x)

print("ORIGINAL: \n" + str(tester) + "\n")

print("TESTED")
print(partition(tester, 5))     # Testing regular case
print(partition(tester, 10))    # Testing partition = max(tester)
print(partition(tester, -1))    # Testing partition = min(tester)
print(partition(tester, 3))     # Testing partition is at beginning
print(partition(tester, 1))     # Testing partition is at end

"""
Runtime Analysis:   
    >> O(??)
    
    CONCLUSION: -- FAILED --
    
"""

    