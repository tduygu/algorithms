# Elementwise Sum
# Create a function that takes two tuples and returns a tuple containing the element-wise sum of the input tuples.

tuple1 = (1, 2, 3, 6)
tuple2 = (4, 5, 6)
# output_tuple = tuple_elementwise_sum(tuple1, tuple2)
# print(output_tuple)  # Expected output: (5, 7, 9)

def tuple_elementwise_sum(tuple1, tuple2):
    len_tuple = len(tuple1) if len(tuple1) < len(tuple2) else len(tuple2)
    sum_list = [0] * len_tuple
    for i in range(len_tuple):
        sum_list[i] = tuple1[i] + tuple2[i]
    return tuple(sum_list)

print(tuple_elementwise_sum(tuple1, tuple2))

def tuple_elementwise_sum2(tuple1, tuple2):
    if len(tuple1) != len(tuple2):
        raise ValueError("Input tuples must have the same length.")

    result = tuple(a + b for a, b in zip(tuple1, tuple2))
    return result

def tuple_elementwise_sum3(tuple1, tuple2):
    return tuple(map(sum, zip(tuple1, tuple2)))