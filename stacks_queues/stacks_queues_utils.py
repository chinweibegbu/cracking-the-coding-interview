class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = next

class Stack:
    def __init__(self):
        self.top = None
    
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