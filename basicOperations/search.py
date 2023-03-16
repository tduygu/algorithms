class SearchOperations:
    def sequentialSearch(self, searchedOne, searchedInList):
        for indnum, num in enumerate(searchedInList):
            # print(f"{indnum} - {num}")
            if searchedOne == num:
                return indnum
        return -1


to_be_searched = (int)(input("Provide the integer number to be searched for:"))
s = SearchOperations()
found_index = s.sequentialSearch(to_be_searched, [1, 5, 4, 8, 2, 90, 67, 3])
str_result = f"The searched number {to_be_searched} is at index {found_index}" if found_index > -1 else f"The searched number does not exist in the list."
print(str_result)
