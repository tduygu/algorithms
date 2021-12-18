# Binary Search
# required that searched_list is sorted


def binary_search(searched_list, target):
    left = 0
    right = len(searched_list)-1

    while left <= right:
        mid = (left + right) // 2

        if searched_list[mid] == target:
            return mid
        elif searched_list[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    # target not found
    return -1

list1 = [6, 7, 8, 9, 10, 12, 14, 15, 18]

# find index of 15
result = binary_search(list1, 15)

if result != -1:
    print("Element is present at index %d" % result)
else:
    print("Element is not present in array")

# what if list is a sorted character array
list2 = ["a", "b", "c", "d"]
result2 = binary_search(list2, "b")