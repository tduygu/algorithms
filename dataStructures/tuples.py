newTuple = 'a', 'b', 'c'
newTuple2 = ('d', 'e', 'f', 'g')
newTuple3 = ('h',)
notTuple = ('f')
newTuple4 = tuple()
newTuple5 = tuple('abcde')
newTuple6 = tuple('123345')

print(newTuple)
print(newTuple2)
print(newTuple3)
print(notTuple)
print(newTuple4)
print(newTuple5)
print(newTuple6)

# time complexity for creating a tuple O(1)
# space complexity O(n)

print('b' in newTuple)
# print(newTuple.index('f')) # ValueError
print(newTuple2.index('f'))

print(newTuple2 + newTuple6)
print(newTuple * 4)

newTuple7 = (1,1,2,2,2,3)
print(newTuple7)
print(newTuple7.count(2))
print(max(newTuple7))

list8 = [1,1,2,2,2,3,4]
print(tuple(list8))
print(max(list8))
print(set(list8))

del list8[0]
print(list8)

# lists in a tuple
newTuple8 = ([1,2], [3,4,5], [80,90])
print(newTuple8)

# Tuples in a tuple
newTuple9 =((1,2), (4,5,6), (8,8,8))
print(newTuple9)