# Find if there is an increasing subarray followed by a decreasing subarray

def is_it_mountain_array(arr) -> bool:
    if len(arr) < 3:
        return False

    i = 1
    # checking for the increasing sequence
    while i < len(arr) and arr[i] > arr[i-1]:
         i += 1

    if i == 1 or i == len(arr):
        return False

    # checking for the decreasing sequence
    while i < len(arr) and arr[i] < arr[i-1]:
        i += 1

    return i == len(arr)


ab = [0, 3, 2, 1]
print(is_it_mountain_array(ab))

ac = [0, 2, 4, 1, 4, 5]
print(is_it_mountain_array(ac))

ad = [0, 1, 2]
print(is_it_mountain_array(ad))


