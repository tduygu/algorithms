def return_bigger(a, b):
    try:
        if b > a:
            return b
        else:
            return a
    except Exception as e:
        print(e)
        return None


# return_bigger(5, 'g')

for subclass in Exception.__subclasses__():
    print(subclass.__name__)


try:
    raise Exception
except Exception as e:
    print(e.args)

try:
    raise Exception('I do not like it', 'in fact I do not like it at all')
except Exception as e:
    print(e.args)


