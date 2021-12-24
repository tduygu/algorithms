class MoveZeroes:
    def move_zeros_right(self, arr):
        j = 0
        n = len(arr)
        for item in arr:
            if item != 0:
                arr[j] = item
                j += 1

        for i in range(j, n):
            arr[i] = 0

        print(arr)


list1 = [1, 5, 0, 7, 0, 3]
print(list1)
mz = MoveZeroes()
mz.move_zeros_right(list1)

list2 = [0]
mz.move_zeros_right(list2)