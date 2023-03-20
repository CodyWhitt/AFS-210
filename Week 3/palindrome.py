class Node: 
    def __init__(self, data=None): 
        self.data = data 
        self.next = None 

class Stack:
    def __init__(self):
        self.top = None
        self.length = 0
        
    def push(self, data):
       node = Node(data) 
       if self.top: 
           node.next = self.top 
           self.top = node                 
       else: 
           self.top = node 
       self.length += 1 
        
    def pop(self): 
        if self.top: 
            data = self.top.data 
            self.length -= 1  
            if self.top.next: 
                self.top = self.top.next 
            else: 
                self.top = None 
            return data 
        else: 
            return None 
        
    def size(self):
        return self.length
    
    def isEmpty(self):
        return self.length == 0
    
    def peek(self): 
        if self.top:
            return self.top.data 
        else: 
            return None 

class Queue:
    def __init__(self):
        self.items = []
        
    def enqueue(self, element):
        self.items.append(element)
        
    def dequeue(self):
        if not self.isEmpty():
            return self.items.pop(0)
        
    def size(self):
        return len(self.items)
    
    def isEmpty(self):
        return len(self.items) == 0
    
    def peek(self):
        if not self.isEmpty():
            return self.items[0]

def isPalindrome(string):
    stack = Stack()
    queue = Queue()
    
    for char in string:
        stack.push(char)
        queue.enqueue(char)
    
    while not stack.isEmpty():
        if stack.pop() != queue.dequeue():
            return False
        
    return True

words = ["racecar", "noon", "python", "madam"]

for letters in words:
    if isPalindrome(letters):
        print("True")
    else:
        print("False")