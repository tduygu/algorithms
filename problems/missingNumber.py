# How to find the missing number in an integer array of 1 to 100?

from array import *

def find_missing(arr):
    for i in range(len(arr)-1):
        if arr[i+1] - arr[i] > 1:
            return arr[i] + 1
            # index at
            # return (i+1, arr[i+1])
    return "No missing"

# Find the missing number int the first n natural numbers in the array
def missing_number(arr, n):
    # Calculate the sum of first n natural numbers
    total = n * (n + 1) // 2
    # Calculate the sum of numbers in the array
    sum_arr = sum(arr)
    # Find the missing number by subtracting sum_arr from total
    missing = total - sum_arr
    return missing


arr1 = [1, 2, 3, 4, 6, 7, 8, 9]
arr2 = [0, 2, 3, 4, 5, 6, 7, 8, 9]
arr3 = [1, 2, 3, 4, 5, 6, 7, 8, 12]
arr4 = [-1, -2, -3, -4, -6, -7, -8]
arr5 = [1, 2, 3, 4, 5, 6, 7, 8, 9]

print(find_missing(arr3))
print(missing_number(arr3, 9))

