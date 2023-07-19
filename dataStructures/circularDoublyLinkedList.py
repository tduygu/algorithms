class Node:
    def __init__(self, nodeValue=None):
        self.value = nodeValue
        self.prev = None
        self.next = None

class circularDoublyLL:
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

    def createCircularDoublyLL(self, value):
        node = Node(value)
        node.next = node
        node.prev = node
        self.head = node
        self.tail = node
        return "Circular doubly linked list is created"

cdll = circularDoublyLL()
print(cdll.createCircularDoublyLL(12))
print([node.value for node in cdll])
