class InstanceCounter(object):

    def __init__(self, val):
        self.val = self.filterint(val)

    @staticmethod
    def filterint(value):
        if not isinstance(value, int):
            return 0
        else:
            return value

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter('hello')

for obj in (a, b, c):
    print(f"val of obj: {obj.val}")

