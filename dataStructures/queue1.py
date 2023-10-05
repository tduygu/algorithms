# Queue with no size limit

class Queue:
    def __init__(self):
        self.items = []

    def __str__(self):
        if self.items is not None:
            values = [str(x) for x in self.items]
            return ' '.join(values)
        return ''

    def isEmpty(self):
        if self.items == []:
            return True
        else:
            return False

    def enqueue(self, value):
        self.items.append(value)
        return "The element is inserted at the end of the queue."

    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty."
        else:
            return self.items.pop(0)

    def peek(self):
        if self.isEmpty():
            return "The queue is empty."
        else:
            return self.items[0]

    def delete(self):
        if self.items:
            self.items = None



customQueue = Queue()
print(customQueue.isEmpty())
customQueue.enqueue(5)
customQueue.enqueue(6)
customQueue.enqueue(7)

print(customQueue)
print(customQueue.dequeue())
print(customQueue)

print(customQueue.peek())
print(customQueue)

print(customQueue.delete())
print(customQueue)