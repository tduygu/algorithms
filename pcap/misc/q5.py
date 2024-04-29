# A closure is a technique which allows the storing of values in spite of the fact that the context in which they have been created does not exist anymore.
# We have a closure in Python when  :
# - there is a nested function (function inside a function).
# - the nested function refers to a value defined in the enclosing function.
# - the enclosing function returns the nested function.
# So, in the above question, only the following statement is correct: A closure must have a nested function.

def func_multiplier_of(n):
    def multi(x):
        return x * n

    return multi


f = func_multiplier_of(3)
print(f(9))  # 27
