shoppingList = ['Milk', 'Cheese', 'Butter']

for i in range(len(shoppingList)):
    print(shoppingList[i])

for n in shoppingList:
    print(n)
##################
print('Milk' in shoppingList)
print('Bread' in shoppingList)
print(shoppingList[-1])
##################
for i in range(len(shoppingList)):
    shoppingList[i] = shoppingList[i] + " - ok"
##################
print(shoppingList)
print('Milk' in shoppingList)
##################
shoppingList.insert(0, 'Bread')
# O(n) time complexity - space O(1)
print(shoppingList)
shoppingList.insert(6, 'Coke')
print(shoppingList)
##################
shoppingList.append('Eggs')
# O(1) time complexity - space O(1)
print(shoppingList)
##################
newShoppingList =['Cucumber', 'Eggplant']
# O(m) time compexity - m number of elements of the new list - space comp O(m)
shoppingList.extend(newShoppingList)
print(shoppingList)
##################
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g']
print(letters[:2])
letters[0:2] = ['x', 'y']
print(letters)

##################
letters.pop(1) # works based on index if given
print(letters)
letters.pop()
print(letters)
##################
del letters[2]
print(letters)

del letters[1:3]
print(letters)
##################
letters.remove('f')
print(letters)
##################
list1 = [2, 5, 4, 10, 6, 15, 6, 20]
if 4 in list1:
    print(f"4 is in the list")

#####################
# linear search
def linear_search(p_list, p_target):
    for i, value in enumerate(p_list):
        if value == p_target:
            return i
    return -1

print(f"4 is at index {linear_search(list1, 4)}")

##################
a = [1, 2, 3]
b = [4, 5, 6]
c = a + b
print(c)
##################
d = [0, 1]
e = d * 4
print(e)
##################
print(f"Max element in list b is {max(b)}")
print(f"Sum of the elemnts in list b is {sum(b)}")
##################

myList = list()
while(True):
    inp = input('Enter a number: ')
    if inp=='done': break
    value = float(inp)
    myList.append(value)
if len(myList) > 0:
    average = sum(myList) / len(myList)
    print(f"Average is {average}")

##################

k = 'spam'
m = list(k)
print(m)

kkm = 'kitap kahve muhabbet'
aile = 'duygu-özgür-rüzgar'
kkm_list = kkm.split()
aile_list = aile.split('-')
print(kkm_list)
print(aile_list)
delimiter = '_'
kkm_list.extend(aile_list)
print(kkm_list)
print(delimiter.join(kkm_list))

##################
# docs.python.org

##################

list123 = [4, 9, 2, 1, 1, 0 ,56, 3]
original_list123 = list123[:]
list123.sort()
print(original_list123)
print(list123)
print(sorted(original_list123))
print(original_list123)

##################
import numpy as np

myArray = np.array([1,2,3,4,5,6])
myArray2 = np.array([1,2,3,4,5,6])
myList = [1,2,3,4,5,6]
myList2= [1,2,3,4,5,6]

print(myArray/2)

# unsupported operand
# print(myList/2)

print(myArray+myArray2)
print(myList+myList2)






