import queue as q

myQ = q.Queue(maxsize=3)

myQ.put(1)
myQ.put(2)
myQ.put(3)

print(myQ.qsize())
print(myQ.full())
print(myQ.get())
print(myQ.qsize())