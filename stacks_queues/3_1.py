# QUESTION
# Three in One: Describe how you could use a single array to implement three stacks.

class Stack:
    def __init__(self, bottom_index, capacity):
        self.top_index = bottom_index
        self.bottom_index = bottom_index
        self.capacity = capacity
        self.count = 0
    
    def push(self, data):
        # If there is no space in the stack, do not allow
        if (self.count >= self.capacity):
            raise Exception("Stack is full")
        else:
            # If it an not empty stack, point to the next None slot
            # REMEMBER: top_index points to the current top, not the next open slot
            if (arr[self.top_index] != None):
                self.top_index += 1
            # Add the data to the top_index
            arr[self.top_index] = data
            # Increment count
            self.count += 1
        
    def pop(self):
        # Check if the stack is empty
        if self.isEmpty():
            return None
        # Save a reference to TOP
        removed = arr[self.top_index]
        # Replace content with None
        arr[self.top_index] = None
        # Update the top_index and count
        self.top_index -= 1
        self.count -= 1
        # Return the saved reference
        return removed
    
    def peek(self):
        # Check if the stack is empty
        if self.isEmpty():
            return None
        # Return the data at top_index
        return arr[self.top_index]
    
    def isEmpty(self):
        # Check if top index and bottom index are the same and TOP is null
        return ((self.top_index == self.bottom_index) and (arr[self.top_index == None]))
    
    def __str__(self):
        cur = self.top
        result = "TOP >>> "
        while (cur):
            result += str(cur.data) + " --> "
            cur = cur.next
        result += "BOTTOM"
        return result

def create_array(size):
    return [None]*size

def create_3_stacks(arr):
    stacks = []
    
    stack_size = len(arr) // 3
    remnant = len(arr) % 3
    bottom_index = 0
    for i in range(3):
        capacity = stack_size if (i < 2) else stack_size + remnant
        stacks.append(Stack(bottom_index, capacity))
        bottom_index += stack_size
    # Return three created stacks
    return stacks[0], stacks[1], stacks[2]

# Create array and stacks
arr = create_array(12)
stack_1, stack_2, stack_3 = create_3_stacks(arr)

print(arr)
stack_1.push(23)
stack_2.push(31)
stack_3.push(89)
print(arr)

stack_1.push(21)
stack_2.push(30)
stack_3.push(88)
print(arr)

stack_1.push(20)
stack_2.push(29)
stack_3.push(87)
print(arr)

stack_1.push(19)
stack_2.push(28)
stack_3.push(86)
print(arr)

# Uncomment the following lines to see the error-throwing when the stack is full
# stack_1.push(18)
# stack_2.push(27)
# stack_3.push(85)
# print(arr)

popped_1, popped_2, popped_3 = stack_1.pop(), stack_2.pop(), stack_3.pop()
print("pop()-ed {}, {} and {} from stack_1, stack_2 and stack_3, respectively".format(popped_1, popped_2, popped_3))
print(arr)

print("stack_1 TOP: {}".format(stack_1.peek()))
print("stack_2 TOP: {}".format(stack_2.peek()))
print("stack_3 TOP: {}".format(stack_3.peek()))