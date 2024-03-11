from stacks_queues_utils import Stack

# Create stack
tester = Stack()
print(tester)

# Check if stack is empty
print("The stack is empty: " + str(tester.isEmpty()))

# Add nodes to stack
for element in [10, 5, 2, 1]:
    tester.push(element)
print(tester)

# Remove top node
top_node = tester.pop()
print(tester)
print("Removed TOP: " + str(top_node.data))

# View new TOP's data without removing it
print("New TOP: " + str(tester.peek()))

# Check if stack is empty
print("The stack is empty: " + str(tester.isEmpty()))
