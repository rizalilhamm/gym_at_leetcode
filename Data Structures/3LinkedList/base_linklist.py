class Node:
    def __init__(self, value):
        self.value = value
        self.next = None

class LinkedList:
    def __init__(self, value):
        self.head = Node(value)
        self.tail = self.head
        self.length = 1

    def append(self, value):
        newNode = Node(value)
        self.tail.next = newNode
        self.tail = newNode
        return
    
    def prepend(self, value):
        newNode = Node(value)
        newNode.next = self.head
        self.head = newNode
        self.length += 1
        return
    
    def printLinkedList(self):
        arr = []
        currNode = self.head

        while currNode != None:
            arr.append(currNode.value)
            currNode = currNode.next

        return arr

    def insert(self, index, value):
        if index >= self.length:
            return self.append(value)
        
        newNode = Node(value)
        

if __name__ == "__main__":
    newLinkedList = LinkedList(10)
    newLinkedList.append(12)
    newLinkedList.prepend(8)
    newLinkedList.prepend(9)
    newLinkedList.append(11)
    print(newLinkedList.printLinkedList())
