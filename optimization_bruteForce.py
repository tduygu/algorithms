
def maxSum(arr, k):
    max_sum = 0
    n = len(arr)
    for x in range(n-k+1):
        current_sum = 0
        for s in range(x, x+k):
            current_sum += arr[s]
            if current_sum > max_sum:
                max_sum = current_sum

    return max_sum

listA = [200, 550, 90, 100]
maxs = maxSum(listA, 2)
print(maxs)
