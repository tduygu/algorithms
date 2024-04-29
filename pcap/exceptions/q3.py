try:
    #raise ArithmeticError
    raise LookupError
except(ArithmeticError, LookupError):
    print('except branch')