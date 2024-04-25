class Mammal:
    def __init__(self, val):
        self.__name = val

class Feline(Mammal):
    pass

class Cat(Feline):
    __bases=[2,3]
    def __str__(self):
        return self.name

mycat = Cat('Garfield')

print(Cat.__bases__[0].__name__)
print(len(Cat.__bases__))