
# class YourClass(object):
#     classy = 'class value!'
#
# dd = YourClass()
# print(dd.classy)
#
# dd.classy = 'inst value!'
# print(dd.classy)
#
# del dd.classy
#
# print(dd.classy)

class InstanceCounter(object):
    count = 0

    def __init__(self, val):
        self.val = val #instance variable
        InstanceCounter.count += 1

    def set_val(self, newval):
        self.val = newval

    def get_val(self):
        return self.val

    def get_count(self):
        return InstanceCounter.count

a = InstanceCounter(5)
b = InstanceCounter(13)
c = InstanceCounter(17)

for obj in (a, b, c):
    print(f"val of obj: {obj.get_val()}") # initialized value (5, 13, etc)
    print("count: %s" % obj.get_count()) # always 3
