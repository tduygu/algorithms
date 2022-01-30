thislist = ["apple", "banana", "cherry"]
mylist = thislist
mylist2 = thislist.copy()
mylist3 = list(thislist)

thislist.insert(2, "orange")
print(mylist)
print(mylist2)
print(mylist3)