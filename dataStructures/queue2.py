# Queue with capacity

class Queue:
    def __init__(self, maxSize):
        self.items = maxSize * [None]
        self.maxSize = maxSize
        self.start = -1
        self.top = -1

    def __str__(self):
        values = [str(x) for x in self.items]
        return ' '.join(values)

    def isFull(self):
        if self.start - self.top == 1 or (self.start == 0 and self.top + 1 == self.maxSize):
            return True
        return False

    #-1 değeri enqueksnmış olamaz mı None yapılsa daha uygun değil mi
    def isEmpty(self):
        if self.top == -1:
            return True
        else:
            return  False

    def enqueue(self, value):
        if self.isFull():
            return "The queue is full"
        else:
            if self.top + 1 == self.maxSize:
                self.top = 0
            else:
                self.top += 1
                if self.start == -1:
                    self.start = 0
            self.items[self.top] = value
            return "The element is inserted at the end of Queue"

    def dequeue(self):
        if self.isEmpty():
            return "The queue is empty."
        removed = self.items[self.start]
        startindex = self.start
        if self.start == self.top:
            self.start = -1
            self.top = -1
        elif self.start == self.maxSize-1:
            self.start = 0
        else:
            self.start += 1

        self.items[startindex] = None
        return f"The element {removed} is removed from the beginning of the queue"

    def peek(self):
        if self.isEmpty():
            return "The queue is empty."
        else:
            return self.items[self.start]

    def delete(self):
        self.items = self.maxSize * [None]
        self.top = -1
        self.start = -1




customQueue = Queue(3)
customQueue.enqueue('a')
customQueue.enqueue(1)
print(customQueue.isFull())
customQueue.enqueue(6)
print(customQueue)
print(f"Is the queue full? {customQueue.isFull()}")
print(customQueue.dequeue())
print(customQueue.dequeue())
print(customQueue.peek())
print(customQueue.dequeue())
print(customQueue.peek())
print(customQueue.dequeue())
print(customQueue.dequeue())
print(customQueue.dequeue())
print(customQueue.dequeue())
print(f"Is the queue full? {customQueue.isFull()}")