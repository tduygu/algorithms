from random import randint
class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None
        self.prev = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self, values = None):
        self.head = None
        self.tail = None

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next

    def __str__(self):
        values = [str(x.value) for x in self]
        return ' -> '.join(values)

    def __len__(self):
        result = 0
        node = self.head
        while node:
            result += 1
            node = node.next
        return result

    def add(self, value):
        newNode = Node(value)
        if self.head is None:
            self.head = newNode
            self.tail = newNode
        else:
            self.tail.next = newNode
            self.tail = newNode
        return self.tail

    def generate(self, n, min_value, max_value):
        self.head = None
        self.tail = None
        for i in range(n):
            self.add(randint(min_value, max_value))
        return self

    def findFromEnd(self, n):
        if n < 0:
            return "n is not in the proper index range"
        temp1 = self.head
        temp2 = self.head
        for _ in range(n-1):
            if temp2.next:
                temp2 = temp2.next
            else:
                return "n is not in the proper index range"

        while temp2:
            if temp2 == self.tail:
                return temp1
            else:
                temp2 = temp2.next
                temp1 = temp1.next


customLL = LinkedList()
customLL.generate(10, 0, 99)
print(customLL)
print(len(customLL))
print(customLL.findFromEnd(10))







