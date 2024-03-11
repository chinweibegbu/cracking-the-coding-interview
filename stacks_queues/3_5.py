from stacks_queues_utils import Stack, StackNode

def sort_stack(stack):
    cur = stack.top
    helper = Stack()
    
    # If there is one or zero elements, return the stack
    if ((cur.next is None) or (cur is None)):
        return stack
    
    # Move everything to the helper stack
    while (cur):
        # Remove top of main stack
        popped = stack.pop()
        # Push pop()-ed element onto helper stack
        helper.push(popped.data)
        # Update cur to new top
        cur = stack.top
    
    # Insert back into main stack in the right position
    print(helper)
    cur = helper.top
    while (cur):
        # If stack is empty or is less than what is currently at the top, push
        if ((stack.top is None) or (cur.data < stack.top.data)):
            stack.push(cur.data)
            print(cur.data)
        else:
            # Go through stack like a linked list until you get to its appropriate position
            curr = stack.top
            while (curr):
                # If what we're inserting is greater than the traverser
                if (cur.data > curr.data):
                    # If we are at the bottom, insert it
                    if (curr.next is None):
                        cur.next = None
                        curr.next = cur
                        break
                    # Else, move down further
                    else:
                        curr = curr.next
                # Else, insert it
                else:
                    cur.next = curr.next
                    curr.next = cur
                    break
        # Update helper stack pointer
        cur = cur.next

# Create stack
tester = Stack()

# Add unordered elements to stack
for element in [4, 35, 12, 1]:
    tester.push(element)
    
# Print stack pre-ordering
print(tester)

# Order stack
sort_stack(tester)

# Print stack post-ordering
print(tester)

"""
-- INCOMPLETE --

Runtime Analysis: Theorised to be O(n^2) due to the nested while loops
"""
