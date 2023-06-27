# Common Elements
# Write a function that takes two tuples and returns a tuple containing the common elements of the input tuples.

tuple1 = (1, 2, 3, 4, 5)
tuple2 = (4, 5, 6, 7, 8)
#output_tuple = common_elements(tuple1, tuple2)
#print(output_tuple)  # Expected output: (4, 5)

def common_elements(tuple1, tuple2):
    common = []
    for n in tuple2:
        if n in tuple1:
            common.append(n)
    return tuple(common)


    # Convert both input tuples into sets using the set() constructor,
    # then use the set intersection operator & to find the common elements between the two sets.
    # Convert the resulting set of common elements back to a tuple and return it.
def common_elements2(tuple1, tuple2):
    return tuple(set(tuple1) & set(tuple2))


print(common_elements2(tuple1, tuple2))