class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

class doublyLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createDLL(self, nodeValue):
        node = Node(nodeValue)
        node.prev = None
        node.next = None
        self.head = node
        self.tail = node
        return "The doubly linked list is created."

    def insertNode(self, nodeValue, indexValue):
        if self.head is None:
            print("The node cannot be inserted")
            return
        node = Node(nodeValue)
        if indexValue == 0:
            node.prev = None
            node.next = self.head
            self.head.prev = node
            self.head = node
        elif indexValue == -1:
            node.next = None
            node.prev = self.tail
            self.tail.next = node
            self.tail = node
        else:
            preNode =self.head
            for i in range(indexValue - 1):
                if preNode == self.tail:
                    print("Can not move further and can not insert")
                    return
                if preNode:
                    preNode = preNode.next

            if preNode.next:
                node.next = preNode.next
                preNode.next.prev = node
            else:
                node.next = None
                self.tail = node
            node.prev = preNode
            preNode.next = node

    def traverse(self):
        tempNode = self.head
        while tempNode:
            print(tempNode.value)
            tempNode = tempNode.next



doublyLL = doublyLinkedList()
print(doublyLL.createDLL('R'))
doublyLL.insertNode('Ü',1)
doublyLL.insertNode('Z',2)
doublyLL.insertNode('G',3)
doublyLL.insertNode('R',-1)
doublyLL.insertNode('A',4)
doublyLL.insertNode('A',10)
print(f"{[n.value for n in doublyLL]}")
print("*******************")
doublyLL.traverse()
























































