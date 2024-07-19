x = 'France'

def func(x):
    return x[:-3]

try:
    for i in range(3):
        x = func(x)
        print(x)
        assert x
    print(x, end='!')
except IndexError:
    print('Error 1')
except LookupError:
    print('Error 2')
except:
    print('Error 3')