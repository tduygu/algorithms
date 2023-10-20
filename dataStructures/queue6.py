from multiprocessing import Queue

myQ = Queue(maxsize=3)
myQ.put(1)
print(myQ.get())