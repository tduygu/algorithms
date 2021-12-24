
class MyNum(object):
    def __init__(self):
        print("calling __init__")
        self.val = 0

    def increment(self):
        self.val += 1

dd = MyNum()
dd.increment()
# dd.val = 'ali'
dd.increment()
print(dd.val)

