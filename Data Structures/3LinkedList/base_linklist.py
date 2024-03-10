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
        self.head.next = newNode
        self.tail = newNode
        self.length += 1
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

    def 


if __name__ == "__main__":
    newLinkedList = LinkedList(10)
    # newLinkedList.append(12)
    print(newLinkedList.printLinkedList())
