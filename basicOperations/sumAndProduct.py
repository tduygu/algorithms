# Sum and Product
# Write a function that calculates the sum and product of all elements in a tuple of numbers.

input_tuple = (1, 2, 3, 4)
# sum_result, product_result = sum_product(input_tuple)
# print(sum_result, product_result)  # Expected output: 10, 24

def sum_product(input_tuple):
    if len(input_tuple) == 0:
        return None, None
    product_result = 1
    sum_result = 0
    for i in input_tuple:
        sum_result += i
        product_result *= i
    return sum_result, product_result

print(sum_product(input_tuple))


input_tuple2 = ()
print(sum_product(input_tuple2))