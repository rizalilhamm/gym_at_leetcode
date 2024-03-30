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

        curr_node = self.traverseToIndex(index-1)
        holdingPointer = curr_node.next
        curr_node.next = newNode
        newNode.next = holdingPointer
        return self.printLinkedList()
        
    def traverseToIndex(self, index):
        counter = 0
        currNode = self.head

        while (counter != index):
            currNode = currNode.next
            counter += 1

        return currNode

    def remove(self, idx):
        curr_node = self.traverseToIndex(idx-1)
        unwatched_node = curr_node.next
        curr_node.next = unwatched_node.next
        self.length -= 1


if __name__ == "__main__":
    newLinkedList = LinkedList(10)
    newLinkedList.append(12)
    newLinkedList.prepend(8)
    newLinkedList.prepend(9)
    newLinkedList.append(11)
    print(newLinkedList.printLinkedList())
    newLinkedList.insert(2, 1000)
    print(newLinkedList.printLinkedList())
    newLinkedList.remove(2)
    print(newLinkedList.printLinkedList())