from math import sqrt as root


def my_root(x):
    try:
        return root(x)
    except:
        print('Function Error !')
        raise


x = -2
try:
    assert x + 2, "Wrong input !"
    print(my_root(x))
except Exception as e:
    print(e)
else:
    print('All good !')