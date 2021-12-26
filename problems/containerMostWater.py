"""
    Container With Most Water

    Find the maximum difference between x position multiplied by the height

    Think of a coordinate system, maximize the area between 2 buildings
    Think of a list:
    indexes - x axis
    values - y axis
"""
class ContainerMostValue:
    def calculate_area(self, arr):
        i = 0
        j = len(arr) - 1
        area_total = 0
        while i < j:
            x = j - i
            y = arr[j] if (arr[j] < arr[i]) else arr[i]
            area = x * y
            area_total = area if area > area_total else area_total
            if arr[i] > arr[j]:
                j -= 1
            else:
               i += 1

        return area_total


list1 = [2, 4, 6, 5, 3, 8]
abc = ContainerMostValue()
print(abc.calculate_area(list1))

list2 = [1, 8, 6, 2, 5, 4, 8, 3, 7]
print(abc.calculate_area(list2))


