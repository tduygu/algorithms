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

    # def remove(self, nodeIndex):
    #     if self.head is None:
    #         return None
    #     tempNode = self.head
    #     if nodeIndex == 0:
    #         if self.head == self.tail:
    #             tempNode.next = None
    #             self.head = None
    #             self.tail = None
    #         else:
    #             self.head = tempNode.next
    #             self.tail.next = self.head
    #
    #     for i in range(1, nodeIndex+1):
    #         pre_node = tempNode
    #         current_node = tempNode.next
    #         if i == nodeIndex:
    #             pre_node.next = current_node.next
    #             current_node.next = None
    #             if current_node== self.tail:
    #                 self.tail = pre_node







circularSLL = CircularSinglyLinkedList()
print(circularSLL.createCSLL(1))
print(circularSLL.inserCSLL(5,0))
print(circularSLL.inserCSLL(6,1))
# print(circularSLL.inserCSLL(7,-1))
# print(circularSLL.inserCSLL(8, -4))
# print([node.value for node in circularSLL])
print(f"Head: {circularSLL.head.value} Tail: {circularSLL.tail.value}")

circularSLL.traverse()
found = circularSLL.searchCSLL(7)
print(f"{found.value if found is not None else None} is found." )
circularSLL.remove(2)
circularSLL.traverse()
