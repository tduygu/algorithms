from array import *

# 1. Create and array and traverse
arr1 = array('i', [1, 3, 5, 7, 9, 9])

for i in arr1:
    print(i)

# 2. Access individual elements through indexes
def access_array(arr, ind):
    if ind >= len(arr):
        print("No element at this index")
        return -1
    else:
        return arr[ind]


print(f"There is {access_array(arr1, 4)} at index 4")

print(arr1[2])

# 3. Append any value to the array using append() method
arr1.append(13)
print(arr1)

# 4. Insert value in an array using insert() method
arr1.insert(5, 11)
print(arr1)

# 5. Extend python array using extend() method
arr2 = array('i', [21,22,23])
arr1.extend(arr2)
print(arr1)

# 6. Add items from list into array using fromlist() method
#list1 = [50, 51, 52, 'a']
list1 = [50, 51, 52]
print(list1)
arr1.fromlist(list1)
print(arr1)

# 7. Remove any array element using remove() method
arr1.remove(51)
print(arr1)

# 8. Remove last array element using pop() method
arr1.pop()
print(arr1)

# 9. Fetch any element through its index using index() method
print(f"22 is at index {arr1.index(22)}")

# 10. Reverse a python array using reverse() method
arr1.reverse()
print(arr1)

# 11. Get array buffer information through buffer_info() method
print(arr1.buffer_info())
# gives memory start address and number of elements

# 12. Check for number of occurrences of an element using count() method
print(f"9 has {arr1.count(9)} occurances in the array")

# 13. Convert array to string using tostring() method
strTemp = arr1.tostring()
print(strTemp)
ints = array('i')
ints.fromstring(strTemp)
print(ints)

# 14. Convert array to a python list with same elements using tolist() method
#print(arr1.tolist())

# 15. Append a string to char array using fromstring() method

# 16. Slice elements from an array
print(arr1[1:4])
print(arr1[:5])
print(arr1[:])
print(arr1[10:])
# index olarak bak ilk index dahil sonuncusu dahil değil

# Reverse array
def reverse(arr):
    for i in range(0, int(len(arr)/2)):
        other = len(arr) - i - 1
        temp = arr[i]
        arr[i] = arr[other]
        arr[other] = temp
    #return arr

# O(n/2) -> O(n) time complexity

nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(nums1)
# print(reverse(nums1))
reverse(nums1)
print(nums1)