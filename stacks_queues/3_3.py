class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
        self.next = None
    
    def pop(self):
        # Check if the stack is empty
        if self.isEmpty():
            return None
        # Save a reference to TOP
        node = self.top
        # Update TOP to the reference's next
        self.top = self.top.next
        # Return the saved reference
        return node
    
    def push(self, data):
        # Create new node
        new_node = StackNode(data)
        # Connect new node's next to the previous TOP
        new_node.next = self.top
        # Update TOP reference to new node
        self.top = new_node
    
    def peek(self):
        # Check if the stack is empty
        if self.isEmpty():
            return None
        # Return the data in TOP
        return self.top.data
    
    def isEmpty(self):
        # Check if TOP is null
        return (self.top == None)
    
    def __str__(self):
        cur = self.top
        result = "TOP >>> "
        while (cur):
            result += str(cur.data) + " --> "
            cur = cur.next
        result += "BOTTOM"
        return result

class SetOfStacks():
    def __init__(self, capacity):
        self.capacity = capacity
        self.current_stack = Stack()
        self.current_count = 0
    
    def push(self, data):
        # If the current stack is full, create a new stack
        if (self.current_count >= self.capacity):
            self.push_stack()
        # Add new TOP to current top stack
        self.current_stack.push(data)
        # Update the current count
        self.current_count += 1
    
    def pop(self):
        # Save and pop() the current top of current_stack
        old_top = self.current_stack.pop()
        # If the current stack is empty and it was an added stack
        if ((self.current_stack.isEmpty()) and (self.current_stack.next is not None)):
            self.pop_stack()
        # Else, just decrement the count
        else:
            self.current_count -= 1
        # Return the old TOP
        return old_top.data
    
    def push_stack(self):
        # Create a new stack
        new_stack = Stack()
        
        # Add new TOP to SetOfStacks
        new_stack.next = self.current_stack
        self.current_stack = new_stack
        
        # Reset the current_count
        self.current_count = 0
    
    def pop_stack(self):
        # Remove it from SetOfStacks
        self.current_stack = self.current_stack.next
        # Update the count to the count of a full stack, which is capacity
        self.current_count = self.capacity
    
    def peek(self):
        return self.current_stack.peek()
    
    def __str__(self):
        cur = self.current_stack        
        result = "SUPER TOP\n" if (cur) else "SUPER TOP\n"
        while (cur):
            result += str(cur) + "\n"
            cur = cur.next
        result += "SUPER BOTTOM\n\n"
        return result

# Create SetOfStacks
tester = SetOfStacks(3)
print(tester)

# Push 3 elements
tester.push("Daby")
tester.push("Didi")
tester.push("Gloria")
print(tester)

# Push another element
tester.push("Miracle")
print(tester)

# Push another element and peek()
tester.push("Chinenye")
print(tester)
print("{} is currently at the top of SetOfStacks".format(tester.peek()))
print("\n")

# Pop 3 elements then print
for i in range(3):
    print("pop()-ed {} from SetOfStacks".format(tester.pop()))
print("\n")
print(tester)

# Pop last 2 elements
for i in range(2):
    print("pop()-ed {} from SetOfStacks".format(tester.pop()))
print("\n")
print(tester)

# Add a new element and print
tester.push("Chinwe")
print(tester)

"""
Runtime Analysis:
    SetOfStacks push(): O(1)
    SetOfStacks pop(): O(1)
    SetOfStacks push_stack(): O(1)
    SetOfStacks pop_stack(): O(1)
    SetOfStacks peek(): O(1)
    SetOfStacks __str__(): O(n*c), where n is the number of stacks and c is the capacity of each stack
    
    CONCLUSION: 
    - This went well; things to make sure I do:
        - Have a concrete example
        - Do a proper walkthrough
        - Modularise your code
    - I need to pay more attention to the way I talk while thinking through the problem
    - I really need to think about how I'm going to show my writing out to the interviewer
        - POTENTIAL SOLUTION: Set up a camera over a piece of paper
    - What happens when you pop() from the bottom stack of the SetOfStacks? (-- ADDRESSED --)
"""
