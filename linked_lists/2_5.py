from linked_list_utils import LinkedList

def sum_lists(a, b):
    cur_a, cur_b = a.head, b.head
    remainder = 0
    sum = LinkedList()
    while (cur_a or cur_b):
        if (cur_a and cur_b):
            part_sum = cur_a.value + cur_b.value + remainder
            cur_a = cur_a.next
            cur_b = cur_b.next
        elif (cur_a and (not cur_b)):
            part_sum = cur_a.value + remainder
            cur_a = cur_a.next
        elif ((not cur_a) and cur_b):
            part_sum = cur_b.value + remainder
            cur_b = cur_b.next
        
        # Add unit place of part_sum to sum LL
        sum.insert_at_head(part_sum%10)
        # Update the remainder with the tens place of part_sum
        remainder = part_sum//10
    
    # Add a remainder IF the last partial addition resulted in a value greater than 9
    if (remainder > 0):
        sum.insert_at_head(remainder)
    
    # Flip the sum LL
    flipped_sum = flip(sum)
    
    # Return the flipped sum
    return flipped_sum

def flip(ll):
    cur = ll.head
    flipped_ll = LinkedList()
    while (cur):
        flipped_ll.insert_at_head(cur.value)
        cur = cur.next
    return flipped_ll        

def create_linked_list(arr):
    ll = LinkedList()
    for a in arr:
        ll.insert_at_head(a)
    return ll


# Creating testing operands
operand_1 = create_linked_list([6, 1, 7])
operand_2 = create_linked_list([2, 9, 5])
operand_3 = create_linked_list([])
operand_4 = create_linked_list([1, 0, 1, 1, 0])

# 1. Testing general case
print(operand_1)
print(operand_2)
print(sum_lists(operand_1, operand_2))
print()

# 2. Testing one empty list case
print(operand_1)
print(operand_3)
print(sum_lists(operand_1, operand_3))
print()

# 3. Testing two empty lists case
print(operand_3)
print(operand_3)
print(sum_lists(operand_3, operand_3))
print()

# 4. Testing different length lists case
print(operand_1)
print(operand_4)
print(sum_lists(operand_1, operand_4))
print()

"""
Runtime Analysis:   
    Parsing linked lists: O(n)
    flip(): O(n)
    
    n = length of longer linked list
 
    >> O(n)
    Space complexity: O(n)
    THOUGHTS:
    - Could I flip the linked list in place?
    - I think O(n) is the BCR (Best Conceivable Runtime)
    
"""
