class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None

class Queue:
    def __init__(self):
        self.first = None
        self.last = None
    
    def enqueue(self, element):
        # Create new QueueNode
        new_node = QueueNode(element)
        
        # If queue is empty, assign new element to first and last
        if (self.isEmpty()):
            self.first = new_node
            self.last = self.first
        # Else 
        else:
            # Point last.next to new element
            self.last.next = new_node
            # Point last to new element
            self.last = new_node
    
    def dequeue(self):
        # Check if queue is empty
        if (self.isEmpty()):
            return None
        # Get the first element
        first = self.first
        # Set first to the former first's next
        self.first = self.first.next
        # Return the element
        return first
    
    def peek(self):
        return self.first
    
    def isEmpty(self):
        return self.first is None

    def __str__(self):
        cur = self.first
        result = "FIRST --> "
        while (cur):
            result += str(cur.data) + " --> "
            cur = cur.next
        result += "LAST"
        return result

class MultiQueue:
    def __init__(self):
        self.last_position = 1
        self.cats = Queue()
        self.dogs = Queue()
    
    def enqueue(self, name, type):
        # Assign position and name to Animal instance
        new_animal = Animal(name, type, self.last_position)
        
        # Add animal to appropriate queue
        if (type == "cat"):
            self.cats.enqueue(new_animal)
        elif(type == "dog"):
            self.dogs.enqueue(new_animal)
        else:
            raise Exception("Invalid animal type")
        
        # Increment last position
        self.last_position += 1
    
    def dequeueAny(self):
        # Check if queues are empty
        if (self.cats.isEmpty() and self.dogs.isEmpty()):
            return None
        
        # Check if any queue is empty
        if (self.cats.isEmpty()):
            return self.dequeueDog()
        if (self.dogs.isEmpty()):
            return self.dequeueCat()
        
        # If the first cat's position is less than the first dog's position, return the first cat
        if (self.cats.peek().data.position < self.dogs.peek().data.position):
            return self.dequeueCat()
        # Else, return the first dog
        else:
            return self.dequeueDog()
    
    def dequeueCat(self):
        return self.cats.dequeue()
    
    def dequeueDog(self):
        return self.dogs.dequeue()
    
    def peek(self):
        # Check if any queue is empty
        if (self.cats.isEmpty()):
            return self.dogs.peek()
        if (self.dogs.isEmpty()):
            return self.cats.peek()
        
        # If the first cat's position is less than the first dog's position, return the first cat
        if (self.cats.peek().data.position < self.dogs.peek().data.position):
            return self.cats.peek()
        # Else, return the first dog
        else:
            return self.dogs.peek()

    def isEmpty(self):
        return (self.cats.isEmpty() and self.dogs.isEmpty())
            
class Animal:
    def __init__(self, name, type, position):
        self.name = name
        self.type = type
        self.position = position

    def __str__(self):
        return self.name

# -- TEST: Queue --
# Create queue 
queue_tester = Queue()
# Add three elements - check enqueue()
queue_tester.enqueue("Chinwe")
print(queue_tester)
queue_tester.enqueue("Daby")
print(queue_tester)
queue_tester.enqueue("Didi")
print(queue_tester)
# Check dequeue() and peek()
print("Dequeued the first element: {}".format(queue_tester.dequeue().data))
print("New first element: {}".format(queue_tester.peek().data))
print()
print()

# -- TEST: MultiQueue --
# Create queue 
multi_queue_tester = MultiQueue()

# Check enqueue()
animals = [("Boots", "cat"), ("Captain", "dog"), ("Whiskers", "cat"), ("Robert", "cat"), ("Justin", "gerbil"), ("Princess", "dog"), ("Gidarouche", "cat"), ("Patra", "dog")]
for name, type in animals:
    try:
        multi_queue_tester.enqueue(name, type)
        print("Successfully enqueued {} the {}".format(name, type))
    except Exception:
        print(">> Invalid animal type: {} is not a cat or a dog".format(type))
        
# Check __str()__
print()
print("CATS: " + str(multi_queue_tester.cats))
print("DOGS: " + str(multi_queue_tester.dogs))
print()

# Check peek()
print("Oldest animal: {} - TYPE: {}".format(multi_queue_tester.peek().data, multi_queue_tester.peek().data))
print()

# Check dequeueDog() - Expected: Captain, dog
oldest_dog = multi_queue_tester.dequeueDog().data
print("Dequeued oldest dog: {} - TYPE: {}".format(oldest_dog.name, oldest_dog.type))
# Check dequeueCat() - Expected: Boots, cat
oldest_cat = multi_queue_tester.dequeueCat().data
print("Dequeued oldest cat: {} - TYPE: {}".format(oldest_cat.name, oldest_cat.type))
# Check dequeueAny() - Expected: Whiskers, cat
oldest_animal = multi_queue_tester.dequeueAny().data
print("Dequeued oldest animal: {} - TYPE: {}".format(oldest_animal.name, oldest_animal.type))

# Check __str()__ after dequeue()
print()
print("CATS: " + str(multi_queue_tester.cats))
print("DOGS: " + str(multi_queue_tester.dogs))
print()

"""
Runtime Analysis:
    Queue enqueue(): O(1)
    Queue dequeue(): O(1)
    Queue peek(): O(1)
    Queue is_empty(): O(1)
    
    MultiQueue enqueue(): O(1)
    MultiQueue dequeueAny(): O(1)
    MultiQueue dequeueCat(): O(1)
    MultiQueue dequeueDog(): O(1)
    MultiQueue peek(): O(1)
    MultiQueue is_empty(): O(1)
    
    THOUGHTS:
        - The solution is efficient and I did not need to use a linked list.
        - I made a lot of simple mistakes and forgot to talk at some point. 
"""
