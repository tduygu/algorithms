# Queue with linked lists

class Node:
    def __init__(self, value=None):
        self.value = value
        self.next = None

    def __str__(self):
        return str(self.value)

class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __iter__(self):
        currNode = self.head
        while currNode:
            yield currNode
            currNode = currNode.next

class Queue:
    def __init__(self):
        self.linkedList = LinkedList()

    def __str__(self):
        values = [str(x) for x in self.linkedList]
        return ' '.join(values)

    def enqueue(self, value):
        temp = Node()
        temp.value = value
        if self.linkedList.head is None:
            self.linkedList.head = temp
            self.linkedList.tail = temp
        else:
            lastNode = self.linkedList.tail
            lastNode.next = temp
            self.linkedList.tail = temp

    def isEmpty(self):
        if self.linkedList.head is None:
            return True
        else:
            return False

    def dequeue(self):
        if self.isEmpty():
            return "There is no element in the queue"
        else:
            returningNode =self.linkedList.head
            if returningNode.next:
                self.linkedList.head = returningNode.next
            else:
                self.linkedList.head = None
                self.linkedList.tail = None
            return returningNode

    def peek(self):
        if self.isEmpty():
            return "There is no element in the queue"
        return self.linkedList.head()

    def delete(self):
        self.linkedList.head = None
        self.linkedList.tail = None


myQueue = Queue()
myQueue.enqueue('a')
myQueue.enqueue('b')
myQueue.enqueue('c')
print(myQueue)
print(f"dequeued: {myQueue.dequeue()}")
print(myQueue)
print(f"dequeued: {myQueue.dequeue()}")
print(myQueue)
print(f"dequeued: {myQueue.dequeue()}")
print(myQueue)
print(f"dequeued: {myQueue.dequeue()}")
print(myQueue)
print(f"dequeued: {myQueue.dequeue()}")
print(myQueue)