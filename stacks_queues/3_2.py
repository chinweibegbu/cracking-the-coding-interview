import math

class StackNode:
    def __init__(self, data):
        self.data = data
        self.next = next
        self.sorted_next = None

class Stack:
    def __init__(self):
        self.top = None
        self.min = math.inf
        self.min_count = 0
    
    def pop(self):
        # Check if the stack is empty
        if self.isEmpty():
            return None
        # Save a reference to TOP
        node = self.top
        # Update TOP to the reference's next
        self.top = self.top.next
        
        # Update MIN and MIN_COUNT
        if ((node.data == self.min) and (self.min_count > 1)):
            self.min_count -= 1
        if ((node.data == self.min) and (self.min_count == 1)):
            self.min, self.min_count = self.next_min()
        
        # Return the saved reference
        return node

    def next_min(self):
        if (self.isEmpty()):
            return math.inf, 0
        cur = self.top
        min, min_count = math.inf, 0
        while (cur):
            if (cur.data < min):
                min = cur.data
                min_count = 1
            elif (cur.data == min):
                min_count = 2
            cur = cur.next
        return min, min_count
    
    def push(self, data):
        # Create new node
        new_node = StackNode(data)
        # Connect new node's next to the previous TOP
        new_node.next = self.top
        # Update TOP reference to new node
        self.top = new_node
        
        # Update min
        if (data < self.min):
            self.min = data
            self.min_count = 1
        elif (data == self.min):
            self.min_count += 1
    
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

# Print out minimum 
print("MIN: " + str(tester.min))
print("MIN count: " + str(tester.min_count))

# Remove top node
top_node = tester.pop()
print(tester)
print("Removed TOP: " + str(top_node.data))

# View new TOP's data without removing it
print("New TOP: " + str(tester.peek()))

# Print out minimum 
print("MIN: " + str(tester.min))
print("MIN count: " + str(tester.min_count))

# Remove current MIN then print new MIN and MIN count
tester.pop()
tester.pop()
print(tester)
print("MIN: " + str(tester.min))
print("MIN count: " + str(tester.min_count))

# Check if stack is empty
print("The stack is empty: " + str(tester.isEmpty()))

"""
Runtime Analysis:
    push(): O(1)
    pop(): O(n) worst case, O(1) average case (amortized)
    min(): O(1)
    
    >> O(1) ??
    >> Space complexity: O(n)
    CONCLUSION: 
    - I simply could not think of any to keep track of the next min in a way that was not too expensive
    - I settled on an O(n) operation in the worst case scenario
        - The worst case scenario is that you pop() the current min, in which you case you have to traverse the whole stack to find the new min and min_count
        - Note that if there are more than 1 occurence of the min, min_count eliminates you from searching for a new one by simply decreasing itself by 1
    - I consider this worst case scenario amortized over time because the likelihood that you are pop()-ing the min is low
        - Unless you somehow entered a sorted list into your stack such that everytime you pop, you are pop()-ing the min
        - But that's low possibility, right? Very low, right?...
    - This made me think that if you kept track of the entries in sorted order then you could have O(1) accesss to the min element
        - This could be kept in an array or a linked list 
        - This idea has two problems:
            - There is no way to sort in less than O(n logn) time after adding a new element
            - If you say you will place the element directly in its sorted position, it only reduces from O(n logn) to O(n)
            - What do you do when you pop() elements that are not the min? You would still need to find its position in the sorted data structure then delete which is O(n)
    - I am kind of looking forward to the solution for this one because I think I gave it a lot of thought but I couldn't solve it
"""
