from array import *

arr1 = array('i', [1,2,3,4,5,6])

# time complexity O(1)
# space complexity O(1)
def accessElement(array, index):
    if index >= len(array):
        print('There is not any element in this index')
    else:
        print(array[index])

def linear_search(arr, element):
    n = 0
    for i in arr:
        if i == element:
            return n
        n +=1
    return -1

def linear_search2(arr,element):
    for n in range(len(arr)):
        if element == arr[n]:
            return n
    return -1

accessElement(arr1, 10)
accessElement(arr1, 6)
accessElement(arr1, 3)

print("Find element 4 in array")
print(linear_search(arr1, 4))
print(linear_search2(arr1, 4))
print("Find element 19 in array")
print(linear_search(arr1, 19))
print(linear_search2(arr1, 19))

arr1.remove(3)
print(arr1)
