def mySortFunc(n):
    return abs(n - 50)

list1 = [100, 50, 65, 82, 23]
list1.sort()
print(list1)

list1.sort(reverse = True)
print(list1)

list1.sort(key = mySortFunc)
print(list1)

list2 = ["banana", "Orange", "Kiwi", "cherry"]
list2.sort()
print(list2)
list2.sort(key = str.lower)
print(list2)

list3 = ["banana", "Orange", "Kiwi", "cherry"]
list3.reverse()
print(list3)