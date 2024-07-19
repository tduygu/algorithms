class Vegetable:
    pass

class RootVegetable(Vegetable):
    pass

class Potato(RootVegetable):
    pass

print(Potato.__bases__)