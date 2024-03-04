def return_bigger(a, b):
    if not isinstance(a, int) or not isinstance(b, int):
        raise ValueError
    if b > a:
        return b
    else:
        return a
#return_bigger(4, 'a')

try:
    value = int(input("Enter an int: "))
    print(1/value)
    # return_bigger(value, 6)
except:
    print("Something went wrong")
    raise
else:
    print("Everything is perfect")
finally:
    print("Ok.")
