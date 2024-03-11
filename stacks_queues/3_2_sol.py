import math

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = next
        self.prev_min = None

class Stack:
    def __init__(self):
        self.top = None
        self.min = math.inf
    
    def push(self, data):
        # Create new node
        new_node = StackNode(data)
        # Connect new node's next to the previous TOP
        new_node.next = self.top
        # Set prev_min to current min
        new_node.prev_min = self.min
        # Update TOP reference to new node
        self.top = new_node
        
        # Update min
        if (data <= self.min):
            self.min = data
            
    def pop(self):
        # Check if the stack is empty
        if self.isEmpty():
            return None
        # Save a reference to TOP
        node = self.top
        # Update TOP to the reference's next
        self.top = self.top.next
        
        # Update MIN
        if (node.data == self.min):
            self.min = node.prev_min
        
        # Return the saved reference
        return node
    
    def peek(self):
        # Check if the stack is empty
        if self.isEmpty():
            return None
        # Return the data in TOP
        return self.top.data

    def min(self):
        # Check if the stack is empty
        if self.isEmpty():
            return None
        # Return the MIN
        return self.min
    
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

# Create stack
tester = Stack()
print(tester)

# Check if stack is empty
print("The stack is empty: " + str(tester.isEmpty()))

# Add nodes to stack
for element in [10, 35, 1, 12, 1]:
    tester.push(element)
print(tester)

# Print out MIN 
print("MIN: " + str(tester.min))

# Remove top node
top_node = tester.pop()
print(tester)
print("Removed TOP: " + str(top_node.data))

# View new TOP's data without removing it
print("New TOP: " + str(tester.peek()))

# Print out MIN 
print("MIN: " + str(tester.min))

# Remove current MIN then print new MIN 
tester.pop()
tester.pop()
print(tester)
print("MIN: " + str(tester.min))

# Check if stack is empty
print("The stack is empty: " + str(tester.isEmpty()))

"""
Runtime Analysis:
    push(): O(1)
    pop(): O(1)
    min(): O(1)
    
    CONCLUSION:
    - Solved problem of the my approach by having each node push()-ed onto the stack remember the min as at when it joined.
    - min_count is no longer necessary and, thus, was removed.
"""
