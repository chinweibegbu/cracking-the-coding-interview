from linked_list_utils import LinkedList

# Create linked list
tester = LinkedList()

# Add any five (5) distinct values to the linked list
for x in [5, 34, -21, 85, 9]:
    tester.insert_at_head(x)
    print(tester)

# Flip linked list
print("\nLinked list (flipped):")
tester.flip()
print(tester)
tester.flip()   # Undo flip and continue tests

# Delete a specified node in the linked list
tester.delete_node(-21)

# Print the updated linked list
print("\nLinked list with deleted node:")
print(tester)

# Delete head node
tester.delete_node(9)

# Print the updated linked list
print("\nLinked list with deleted HEAD node:")
print(tester)
