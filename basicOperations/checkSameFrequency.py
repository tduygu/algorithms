# Same Frequency
# Define a function which takes two lists as parameters and check if two given lists have the same frequency of elements.


list1 = [1, 2, 3, 2, 1]
list2 = [3, 1, 2, 1, 2]

#check_same_frequency(list1, list2)
#Output:

#False

def check_same_frequency (list1, list2):
    list11 = list(set(list1))
    list22 = list(set(list2))

    if len(list11) != len(list22):
        return False

    dict1 = {}.fromkeys(list11, 0)
    dict2 = {}.fromkeys(list22, 0)

    for item in list1:
        dict1[item] += 1

    for item in list2:
        dict2[item] += 1

    if dict1 == dict2:
        return True
    else:
        return False


print(check_same_frequency(list1, list2))


def check_same_frequency2(list1, list2):
    def count_elements(lst):
        counter = {}
        for element in lst:
            counter[element] = counter.get(element, 0) + 1
        return counter

    return count_elements(list1) == count_elements(list2)

print(check_same_frequency2(list1, list2))