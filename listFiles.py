#!/usr/bin/python
print("Types")
myBool = True
myNone = None
myInt = 5
myStr = 'hello you 2 i l u'
myList = {'a', 'b', 'c', 'c'}
myList2 = ['a', 'b', 'c', 'c']


def typeList() -> None:
    print("lists os files")
    print(type(myBool))
    print(type(myNone))
    print(type(myList))
    print(type(myList2))
    print(type(myInt))
    print(type(myStr))
    print(type(typeList))

def printListContents() -> None:
    print(myList)
    print(myList2)

typeList()
printListContents()