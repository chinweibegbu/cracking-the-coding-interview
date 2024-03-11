# 1. Regular tree
class Node:
    def __init__(self, data):
        self.data = data
        self.children = []        

# 2. Binary tree
class BinaryTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None
        
    def in_order(self):
        # Order: Left, Parent, Right
        if (self.left):
            self.left.in_order()
        print(self.data, end=" > ")
        if (self.right):
            self.right.in_order()
    
    def pre_order(self):
        # Order: Parent, Left, Right
        print(self.data, end=" > ")
        if (self.left):
            self.left.pre_order()
        if (self.right):
            self.right.pre_order()
    
    def post_order(self):
        # Order: Left, Right, Parent
        if (self.left):
            self.left.post_order()
        if (self.right):
            self.right.post_order()
        print(self.data, end=" > ")
    
    def __str__(self):
        return self.data

# 3. Binary Search Tree
class BinarySearchTreeNode(BinaryTreeNode):    
    def __init__(self, data=None):
        BinaryTreeNode.__init__(self, data)
               
    def insert(self, data):
        # If the current node has no data (i.e. empty tree), insert at current node
        if not self.data:
            self.data = data
            return
        
        # If the data is already in the BST, do not insert it
        if self.data == data:
            return

        # If the data is less than the current node's data
        if data < self.data:
            # If the current node has a left, call insert() on that left node
            if self.left:
                self.left.insert(data)
                return
            # Else, set the left of the current node to a new node holding the data
            self.left = BinarySearchTreeNode(data)
            return
        
        # Else, If the current node has a right, call insert() on that right node
        if self.right:
            self.right.insert(data)
            return
        
        # Else, set the right of the current node to a new node holding the data
        self.right = BinarySearchTreeNode(data)
        
    def search(self, toFind):
        # If the current node's data is equal to toFind, return True
        if toFind == self.data:
            return True

        # If the toFind is less than the current node's data
        if toFind < self.data:
            # If the current node does not have a left, return False
            if self.left == None:
                return False
            # Else, call search() on the left node
            return self.left.search(toFind)

        # Else, If the current node does not have a right, return False 
        if self.right == None:
            return False
        # Else, call search() on the right side
        return self.right.exists(toFind)
    
# 4. Binary heap (min-heap)
class MinHeap:
    def __init__(self):
        self.min = None
    
    def insert(self, data):
        # Will insert a BinaryTreeNode
        pass
    
    def remove_min(self, data):
        pass
        
# 5. Trie (a.k.a. prefix tree)
class TrieNode():
    def __init__(self):
        self.data = None
    
class Trie:
    def __init__(self):
        self.root = None