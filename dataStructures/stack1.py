class Stack:
    def __init__(self):
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

    def push(self, value):
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
            return self.stacklist[len(self.stacklist)-1]

    def delete(self):
        self.stacklist = None

customStack = Stack()
customStack.push(1)
customStack.push(2)
customStack.push(3)
print(customStack)
print(f"{customStack.pop()} is popped")
print(f"The nextcomming element in the stack is {customStack.peek()}")

