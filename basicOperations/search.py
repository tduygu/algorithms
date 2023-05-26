class SearchOperations:
    # linear search
    # binary search
    def sequentialSearch(self, searchedOne, searchedInList):
        for indnum, num in enumerate(searchedInList):
            # print(f"{indnum} - {num}")
            if searchedOne == num:
                return indnum
        return -1

    def linearSearch(self, searchedOne, searchedInList):
        for i in range(0, len(searchedInList)):
            if (searchedInList[i] == searchedOne):
                return i
        return -1


    def binarySearch(self, searchedOne, orderedList):
        left = 0
        right = len(orderedList) - 1

        while left <= right:
            middle = int((left + right) / 2)
            print(middle)
            if searchedOne == orderedList[middle]:
                return middle
            elif searchedOne > orderedList[middle]:
                left = middle + 1
            else:
                right = middle -1
        return -1


to_be_searched = (int)(input("Provide the integer number to be searched for:"))
s = SearchOperations()
# sequential search
# found_index = s.sequentialSearch(to_be_searched, [1, 5, 4, 8, 2, 90, 67, 3])
# found_index = s.linearSearch(to_be_searched, [1, 5, 4, 8, 2, 90, 67, 3])

# binary search
found_index = s.binarySearch(to_be_searched, [1,2,4,7,70,79,82,99,500])

str_result = f"The searched number does not exist in the list." if found_index == -1 else f"The searched number {to_be_searched} is at index {found_index}"
print(str_result)