# 3 stacks in 1 Python list
class MultiStack:
    def __init__(self, stackSize):
        self.numberStacks = 3
        self.stacklist = [0] * (stackSize * self.numberStacks)
        self.lengths = [0] * self.numberStacks
        self.stackSize = stackSize

    def isFull(self, stackNum):
        if self.lengths[stackNum] == self.stackSize:
            return True
        else:
            return False

    def isEmpty(self, stackNum):
        if self.lengths[stackNum] == 0:
            return True
        else:
            return  False

    def indexOfTop(self, stackNum):
        offset = stackNum * self.stackSize
        return offset + self.lengths[stackNum] - 1

    def push(self, stackNum, value):
        if stackNum > self.numberStacks-1:
            return "Invalid stack number."
        elif self.isFull(stackNum):
            return "The stack is full"
        else:
            self.lengths[stackNum] += 1
            self.stacklist[self.indexOfTop(stackNum) ] = value
            return f"The element {value} is added to stack {stackNum} The stack size is now: {self.lengths[stackNum]}"

    def pop(self, stackNum):
        if self.isEmpty(stackNum):
            return f"The stack {stackNum} is empty."
        else:
            temp = self.stacklist[self.indexOfTop(stackNum)]
            self.stacklist[self.indexOfTop(stackNum)] = 0
            self.lengths[stackNum] -= 1
            return temp

    def peek(self, stackNum):
        if self.isEmpty(stackNum):
            return f"The stack {stackNum} is empty."
        else:
            return self.stacklist[self.indexOfTop(stackNum)]


s1 = MultiStack(3)

m = 0
for n in s1.stacklist:
    print(f"{m}. {n}")
    m += 1




print(s1.push(0, 'a'))
print(s1.push(0, 'b'))
print(s1.push(stackNum=0, value='c'))

print(s1.push(1, 'D'))
print(s1.push(1, 'E'))
print(s1.push(stackNum=1, value='F'))

print(s1.push(2, '66'))
print(s1.push(2, '67'))
print(s1.push(stackNum=2, value='68'))

print(s1.peek(0))
print(s1.peek(1))
print(s1.peek(2))

print(s1.pop(0))
print(s1.peek(0))
print(s1.isFull(0))


m = 0
for n in s1.stacklist:
    print(f"{m}. {n}")
    m += 1



