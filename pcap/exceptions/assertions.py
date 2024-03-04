# Assertions are assumptions in our program that should always be true.
# USE assertions:
# 1. For debugging / testing your code
# 2. For documenting your code

# DO NOT:
# 1. Validate user input with assertions
# 2. Handle AssertionErrors in try...except

def calculate_inverse(number):
    assert(number != 0), 'Got 0 as a member!'
    return 1 / number

calculate_inverse(5)
calculate_inverse(0)

