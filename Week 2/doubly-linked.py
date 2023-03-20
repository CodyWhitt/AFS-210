class Node:
    # A doubly-linked node.
    def __init__(self, data=None):
        self.data = data
        self.next = None
        self.prev = None

class DoublyLinkedList:
    # A doubly-linked list.
    def __init__(self):
        # Create an empty list.
        self.tail = None
        self.head = None
        self.count = 0

    def iter(self):
        # Iterate through the list.
        currentent = self.head
        while currentent:
            val = currentent.data
            currentent = currentent.next
            yield val


    def size(self) -> int:
        # Returns the number of elements in the list
        return self.count

#2
    def addFirst(self, data) -> None:
        new = Node(data)
        if self.head is None:
            self.head = new
            self.tail = new
        else:
            new.next = self.head
            self.head.prev = new
            self.head = new
        self.count += 1

#2
    def addLast(self, data) -> None:
        new = Node(data)
        if self.tail is None:
            self.head = new
            self.tail = new
        else:
            new.prev = self.tail
            self.tail.next = new
            self.tail = new
        self.count += 1
  
#2
    def addAtIndex(self, data, index):
        # Add a node to the list at the given index position
        # If index equals to the length of linked list, the node will be appended to the end of linked list
        # If index is greater than the length, the data will not be inserted.
        # This function does not replace the data at the index, but pushes everything else down.
        if index > self.count:
            return
        elif index == 0:
            self.addFirst(data)
            return
        elif index == self.count:
            self.addLast(data)
            return
        else:
            new = Node(data)
            current = self.head
            for i in range(index-1):
                current = current.next
            new.next = current.next
            current.next.prev = new
            current.next = new
            new.prev = current
            self.count += 1

#2
    def indexOf(self, data):
        # Search through the list. Return the index position if data is found, otherwise return -1    
        current = self.head
        index = 0
        while current:
            if current.data == data:
                return index
            current = current.next
            index += 1
        return -1


    def add(self, data) -> None:
        # Append an item to the end of the list
        self.addLast(data)

    def clear(self) -> None:
        # Remove all of the items from the list
        self.head = None
        self.tail = None
        self.count = 0

    def deleteAtIndex(self, index) -> None:
        # Delete the node at the index-th in the linked list, if the index is valid.

        if (index > (self.count-1)):
            return
            
        current = self.head
        prev = self.head

        for n in range(index):
            prev = current
            current = current.next
            
        prev.next = current.next
        current.prev = prev
        self.count -= 1

        if (current == self.head):
            self.head = current.next
            current.prev = None
        elif (current == self.tail):
            prev.next = None
            self.tail = prev       

        return

    def delete(self, data) -> None:
        # Delete a node from the list who's value matches the supplied value
        currentent = self.head
        prev = self.head
        while currentent:
            if currentent.data == data:
                if currentent == self.tail:
                    prev.next = None
                    self.tail = prev
                elif currentent == self.head:
                    currentent.next.prev = None
                    self.head = currentent.next
                else:
                    prev.next = currentent.next
                    currentent.next.prev = prev
                self.count -= 1
                return
            prev = currentent
            currentent = currentent.next

    def __getitem__(self, index):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        currentent = self.head
        for n in range(index):
            currentent = currentent.next
        return currentent.data

    def __setitem__(self, index, value):
        if index > self.count - 1:
            raise Exception("Index out of range.")
        currentent = self.head
        for n in range(index):
            currentent = currentent.next
        currentent.data = value

    def __str__(self):
        myStr = ""
        for node in self.iter():
             myStr += str(node)+ " "
        return myStr

#4 Create list
words = DoublyLinkedList()
words.addFirst("the")
words.addLast("Force")
words.addLast("be")
words.addLast("with")
words.addLast("you")
words.addLast("!")
words.addFirst("May")

#3 Print list
print(words)

#5 Return the index position of "with" in the list and print this value
print(words.indexOf("with"))

#6 Change "you" into "us" on the list
index_of_you = words.indexOf("you")
words[index_of_you] = "us"

#7 Add "all" before "!" on the list 
index_of_exc = words.indexOf("!")
words.addAtIndex("all", index_of_exc)

#8 print the list
print(words)