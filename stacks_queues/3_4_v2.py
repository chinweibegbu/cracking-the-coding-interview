from stacks_queues_utils import Stack

# Update when you enqueue() or dequeue() and track independently
class MyQueue:
    def __init__(self):
        self.main = Stack()
        self.helper = Stack()
        self.first = None
    
    def enqueue(self, data):
        # If queue is empty, set the first to the newly added data
        if (self.main.isEmpty()):
            self.first = data
        
        # Add data to the main stack
        self.main.push(data)

    def dequeue(self):
        # IDEA: Use the second stack to hold the values in opposite order then get the first value which is what was entered first
        cur = self.main.top
        while (cur):
            # Remove cur from main stack
            node = self.main.pop()
            # Add cur to helper stack
            self.helper.push(node.data)
            # Update cur
            cur = cur.next
            
        # Remove and save top of helper stack
        dequeued = self.helper.pop()
        
        # Re-insert everything into main stack
        cur = self.helper.top
        # Update the first to cur's data or None depending on if cur is None
        self.first = cur.data if cur else None
        while (cur):
            # Remove cur from helper stack
            node = self.helper.pop()
            # Add cur back to main stack
            self.main.push(node.data)
            # Update cur
            cur = cur.next
            
        # Return the saved dequeued node's value 
        return dequeued
    
    def peek(self):
        # If the queue is empty, return None --> Is this redundant because the default value of self.first is None?
        if (self.main.isEmpty()):
            return None
        
        # Return self.first
        return self.first

    def is_empty(self):
        return self.main.isEmpty()
    
# Create a queue
tester = MyQueue()

# Add any three elements e.g. ["Chinwe", "Michelle", "Ibegbu"]
for name in ["Chinwe", "Michelle", "Ibegbu"]:
    tester.enqueue(name)

# Peek the first element --> Expected: "Chinwe"
print("Current first element in queue is {}".format(tester.peek()))

# Dequeue the first element
dequeued = tester.dequeue()

# Peek the new first element --> Expected: "Michelle"
print("Current first element in queue is {}".format(tester.peek()))

"""
Runtime Analysis:
    MyQueue enqueue(): O(1)
    MyQueue dequeue(): O(n)
    MyQueue peek(): O(1)
    MyQueue is_empty(): O(1)
    
    Space complexity: O(n)
    
    CONCLUSION: 
    - Addresses the peek() bottleneck in Ver. 1
"""
