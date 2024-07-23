import random

class MyClass(object):
    var = 10

    def dothis(self):
        self.rand_val = random.randint(1, 10)

    def callme(self):
        print('calling "callme" method with instance: ')
        print(self)

# print("This object")
# this_obj = MyClass()
# print(this_obj)
# print(this_obj.var)
# this_obj.callme()
#
# print("That object")
that_obj = MyClass()
# print(that_obj)
# print(that_obj.var)
# that_obj.callme()
that_obj.dothis()
print(that_obj.rand_val)