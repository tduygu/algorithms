class Stack:
    def __init__(self, maxSize):
        self.maxSize = maxSize
        self.stacklist = []

    def __str__(self):
        values = self.stacklist.reverse()
        values = [str(x) for x in self.stacklist]
        return "\n".join(values)

    def isEmpty(self):
        if self.stacklist == []:
            return True
        else:
            return False

    def isFull(self):
        if len(self.stacklist) == self.maxSize:
            return True
        else:
            return False

    def push(self, value):
        if self.isFull():
            return "The stack is full"
        else:
            self.stacklist.append(value)
            return f"The element {value} is added."

    def pop(self):
        if self.isEmpty():
            return "There is not any element in the stack."
        else:
            return self.stacklist.pop()

    def peek(self):
        if self.isEmpty():
            return "There is not any element in the stack."
        else:
            return self.stacklist[len(self.stacklist) - 1]

    def delete(self):
        self.stacklist = None

cs = Stack(4)
print(cs.isEmpty())
cs.push(1)
cs.push(2)
cs.push(3)
cs.push(4)
print(cs.push(4))
print(cs.isFull())