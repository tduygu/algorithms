import array

my_array = array.array('i')
print(my_array)
my_array1 = array.array('i', [1,2,3,4])
print(my_array1)

# pip3 install numpy
import numpy as np

np_array = np.array([], dtype=int)
print(np_array)

np_array1 = np.array([1, 2, 3, 4])
print(np_array1)

print(my_array1)
# my_array1.insert(0, 6)
my_array1.insert(4, 6)
# my_array1.insert(100, 6)
# print(my_array1)
# complexity of element insertion time complexity : O(n), space complexity : O(1)

def traversalArray(array):
    for i in array:
        print(i)

traversalArray(my_array1)





