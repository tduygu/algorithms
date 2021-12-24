
class MyNum(object):
    def __init__(self, value):
        print("calling __init__")
        try:
            value = int(value)
        except ValueError:
            value = 0
        self.val = value

    def increment(self):
        self.val += 1

dd = MyNum(5)
dd.increment()
# dd.val = 'ali'
dd.increment()
print(dd.val)

