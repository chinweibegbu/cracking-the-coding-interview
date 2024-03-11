from stacks_queues_utils import Stack

class MyQueue:
    def __init__(self):
        self.main = Stack()
        self.helper = Stack()
    
    def enqueue(self, data):
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
        # IDEA: Use the second stack to hole the values in opposite order then get the first value which is what was entered first
        cur = self.main.top
        while (cur):
            # Remove cur from main stack
            node = self.main.pop()
            # Add cur to helper stack
            self.helper.push(node.data)
            # Update cur
            cur = cur.next
            
        # Remove and save top of helper stack
        peeked = self.helper.peek()
        
        # Re-insert everything into main stack
        cur = self.helper.top
        while (cur):
            # Remove cur from helper stack
            node = self.helper.pop()
            # Add cur back to main stack
            self.main.push(node.data)
            # Update cur
            cur = cur.next
            
        # Return the saved dequeued node's value 
        return peeked

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
    MyQueue peek(): O(n)
    MyQueue is_empty(): O(1)
    
    Space complexity: O(n)
    
    CONCLUSION: 
    - Bottleneck: dequeue() and peek()
    - POTENTIAL ALTERNATIVES:
        - peek(): Update when you enqueue() or dequeue() and track independently
    - Using two stacks, I cannot think of any improvement for dequeue()
"""
