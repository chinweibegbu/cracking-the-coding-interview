class Node:
    def __init__(self, v):
        self.value = v
        self.next = None
    
class LinkedList:
    def __init__(self, head=None):
        self.head = head
    
    def insert_at_head(self, value):
        new_head = Node(value)
        new_head.next = self.head
        self.head = new_head
    
    def delete_node(self, value):
        prev, cur = None, self.head
        
        # If head is current, update head reference
        if (cur.value == value):
            new_head = self.head.next
            self.head = new_head
            return
            
        while(cur.next):
            if (cur.value == value):
                prev.next = cur.next
            prev = cur
            cur = cur.next
    
    def get_node(self, value):
        cur = self.head
        while (cur and cur.value!=value):
            cur = cur.next
        return cur    

    def flip(self):        
        prev, cur, next = None, self.head, self.head.next
        
        while (next):
            # Shift prev and cur one node forward
            prev, cur = cur, next
            # Update next
            next = next.next
            # Point the new cur to the new prev
            cur.next = prev
            # For the first flip, point the old head to None
            if (prev.next == cur):
                prev.next = None
        
        # Set the head to the perviously last item
        self.head = cur
    
    def __str__(self):
        cur = self.head
        if (cur == None):
            return "-- Empty linked list --"
        
        output = "HEAD: "
        while(cur):
            output += str(cur.value) + " --> "
            cur = cur.next
        output += "END"
        return output