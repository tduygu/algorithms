#Insert at the Beginning
#Write a function that takes a tuple and a value, and returns a new tuple with the value inserted at the beginning of the original tuple.

input_tuple = (2, 3, 4)
value_to_insert = 1
# output_tuple = insert_value_front(input_tuple, value_to_insert)
#print(output_tuple)  # Expected output: (1, 2, 3, 4)

def insert_value_front(input_tuple, value_to_insert):
    input_list = list(input_tuple)
    input_list.reverse()
    input_list.append(value_to_insert)
    input_list.reverse()
    return tuple(input_list)

def insert_value_at_beginning2(input_tuple, value_to_insert):
    return (value_to_insert,) + input_tuple

print(input_tuple)
print(list(input_tuple))
print(insert_value_front(input_tuple,value_to_insert))