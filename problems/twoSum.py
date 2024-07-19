# Write a program to find all pairs of integers whose sum is equal to a given number

def find_two_sum(arr, target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            #if distinct nums are required
            #if arr[i] == arr[j]:
             #   continue
            if arr[i] + arr[j] == target:
                return [i, j]
    return []

arr1 = [2,6,3,9,11,2]
print(find_two_sum(arr1, 9))
print(find_two_sum(arr1, 13))
print(find_two_sum(arr1, 3))
print(find_two_sum(arr1, 4))
