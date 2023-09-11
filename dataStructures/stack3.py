class Node:
    def __init__(self, nodeValue=None):
        self.value = nodeValue
        self.next = None


class singlyLinkedList:
    def __init__(self):
        self.head = None

    def __iter__(self):
        node = self.head
        while node:
            yield node
            node = node.next

    def createSinglyLinkedList(self, value):
        node = Node(value)
        self.head = node
        node.next = None

    def appendFirst(self,value):
        node = Node(value)
        node.next = self.head
        self.head = node

    def removeFirst(self):
        if self.head is not None:
            tmp = self.head.value
            self.head = self.head.next
            return tmp

    def deleteAll(self):
        self.head = None

class Stack:
    def __init__(self):
        self.sll = singlyLinkedList()

    def __str__(self):
        #return f"{[node.value for node in self.sll]}"
        values = [str(node.value) for node in self.sll]
        return "\n".join(values)

    def isEmpty(self):
        if self.sll.head is None:
            return True
        else:
            return False

    def push(self, value):
        self.sll.appendFirst(value)
        return f"The element {value} is added."

    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack."
        else:
            return self.sll.removeFirst()

    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack."
        else:
            return self.sll.head.value

    def delete(self):
        self.sll.deleteAll()




abs = Stack()
print(abs.isEmpty())
abs.push(1)
abs.push(2)
abs.push(3)
abs.push(4)
print(abs)
abs.pop()
print("***********")
print(abs)
print(f"The peek is {abs.peek()}")