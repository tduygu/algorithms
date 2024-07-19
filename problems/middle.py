# Write a function called middle that takes a list and returns a new list
# that contains all but the first and last elements

def middle(arr):
    return arr[1:-1]
    #return arr[1:len(arr)-1]

myList = [1,2,3,4]
myList2 = [1,3]
print(middle(myList))

def diagonal_sum(arr2d):
    product = 0
    for i in range(len(arr2d)):
        for j in range(len(arr2d[0])):
            if i == j:
                product += arr2d[i][j]
    return product

def diagonal_sum2(arr2d):
    product = 0
    for i in range(len(arr2d)):
        product += arr2d[i][i]
    return product

import numpy
arr1 = numpy.array([[1,2,3], [4,5,6], [7,8,9]])
print(diagonal_sum(arr1))
print(diagonal_sum2(arr1))

# Given a list, write a function to get first, second and best scores
# from the list. List may contain duplicates.
def best_score(my_list):
    if len(my_list) < 1:
        return
    my_list.sort(reverse=True)
    print(my_list[:2])
    #my_list.sort()
    #print(my_list[-2:])

arr2 = [7, 8, 5, 3, 1, 2]
arr3 = [84,85,86,87,85,90,85,83,23,45,84,1,2,0]
best_score(arr3)

def first_second(my_list):
    max1, max2 = float('-inf'), float('-inf')

    for i in my_list:
        if i > max1:
            max2 = max1
            max1 = i
        elif i > max2 and i != max1:
            max2 = i
    return max1, max2

print(first_second(arr2))

# Write a function to remove the duplicate numbers on given integer array/list.
def remove_duplicates(arr):
    return list(set(arr))

def remove_duplicates2(arr):
    index_arr = []
    for i in range(len(arr)):
        for j in range(i+1, len(arr)):
            if arr[i] == arr[j]:
                index_arr.append(j)
    # print(index_arr)
    for i in index_arr:
        arr.pop(i)

    return arr

def remove_duplicates3(arr):
    unique_lst = []
    seen = set()
    for item in arr:
        if item not in seen:
            unique_lst.append(item)
            seen.add(item)
    return unique_lst

arr4 = [1, 1, 2, 2, 3, 4, 5]
print(arr4)
print(remove_duplicates(arr4))

arr5 = [1, 1]
arr6 = [1, 2, 2, 4, 5]
print(arr5)
print(remove_duplicates(arr5))
print(remove_duplicates2(arr6))
print(remove_duplicates3(arr4))



# Pairs
# Write a function to find all pairs of an integer array whose sum is equal to a given number. Do not consider commutative pairs.

# Example:
#pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7)
#Output : ['2+5', '4+3', '3+4', '-2+9']


def pair_sum(arr, total):
    totol_list = []
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i] + arr[j] == total:
                totol_list.append(f"{arr[i]}+{arr[j]}")

    return totol_list

print(pair_sum([2, 4, 3, 5, 6, -2, 4, 7, 8, 9],7))


# Contains Duplicate
# Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
def contains_duplicate(nums):
    if len(set(nums)) != len(nums):
        return True
    return False

print(contains_duplicate(arr5))

