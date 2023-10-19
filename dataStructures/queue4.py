from collections import deque

customQueue = deque(maxlen=3)
print(customQueue)

customQueue.append(1)
customQueue.append(2)
print(customQueue)

customQueue.append(3)
print(customQueue)
customQueue.append(4)
print(customQueue)

print(customQueue.popleft())
print(customQueue)

customQueue.clear()
print(customQueue)