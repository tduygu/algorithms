myList1 = [x**x for x in range(4)]
print(myList1)
myList2 = tuple(filter(lambda x: x%2 != 0, myList1))
print(myList2)