class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None


class CircularSinglyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next
            if node == self.tail.next:
                break

    def createCSLL(self, nodeValue):
        node = Node(nodeValue)
        node.next = node
        self.head = node
        self.tail = node
        return "The CSLL has been created."

    def inserCSLL(self, value, location):
        if self.head is None:
            return "The head reference is None"
        if location < -1:
            return "Invalid location"
        else:
            newNode = Node(value)
            if location == 0:
                newNode.next = self.head
                self.head = newNode
                self.tail.next = newNode
            elif location == -1:
                newNode.next = self.tail.next
                self.tail.next = newNode
                self.tail = newNode
            else:
                tempNode = self.head
                index = 0
                while index < location - 1:
                    tempNode = tempNode.next
                    index += 1
                nextNode = tempNode.next
                tempNode.next = newNode
                newNode.next = nextNode
            return "The node has been successfully inserted."

    def traverse(self):
        if self.head is None:
            return
        tempNode = self.head
        print(tempNode.value)
        while tempNode.next != self.head:
            tempNode = tempNode.next
            print(tempNode.value)

    def traversalCSLL(self):
        if self.head is None:
            print("There is not any element for traversal.")
        else:
            tempNode = self.head
            while tempNode:
                print(tempNode.value)
                tempNode = tempNode.next
                if tempNode == self.tail.next:
                    break

    def searchCSLL(self, nodeValue):
        if self.head is None:
            return None
        tempNode = self.head
        while tempNode:
            if tempNode.value == nodeValue:
                return tempNode
            tempNode = tempNode.next
            if tempNode == self.tail.next:
                return None
        return None

    def deleteNode(self, location):
        if location < 0:
            return None
        if self.head is None:
            return None
        if location == 0:
            if self.head == self.tail:
                tmp = self.head
                self.head.next = None
                self.head = None
                self.tail = None
                return tmp
            else:
                temp = self.head.next
                self.head.next = None
                self.head = temp
                self.tail.next = temp
                return temp
        elif location == -1:
            node = self.head
            while node is not None:
                if node.next == self.tail:
                    break
                node = node.next
            node.next = self.head
            self.tail = node
            # return node
        else:
            tempNode = self.head
            for i in range(location-1):
                tempNode = tempNode.next
            nextNode = tempNode.next
            tempNode.next = nextNode.next
            # return tempNode

    def deleteEntireCSLL(self):
        self.head = None
        self.tail.next = None
        self.tail = None















circularSLL = CircularSinglyLinkedList()
print(circularSLL.createCSLL(1))
print(circularSLL.inserCSLL(5,0))
#print(circularSLL.inserCSLL(6,1))
# print(circularSLL.inserCSLL(7,-1))
# print(circularSLL.inserCSLL(8, -4))
# print([node.value for node in circularSLL])
#print(f"Head: {circularSLL.head.value} Tail: {circularSLL.tail.value}")

circularSLL.traverse()
#found = circularSLL.searchCSLL(7)
#print(f"{found.value if found is not None else None} is found." )

#circularSLL.traverse()


#circularSLL.deleteNode(2)
#circularSLL.deleteNode(1)
circularSLL.deleteNode(0)
print("****")
circularSLL.traverse()
