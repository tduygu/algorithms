
class Node:
    def __init__(self, value):
        self.value = value
        self.next = None


class LinkedList:
    def __init__(self, value):
        temp_node = Node(value)
        self.head = temp_node
        self.tail = temp_node
        self.length = 1