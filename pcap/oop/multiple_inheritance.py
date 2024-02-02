class Vehicle:
    def __init__(self):
        print("going")

    def introduce(self):
        print("I'm a vehicle.")

    def go(self):
        print("go go go")

class Flyable:
    def __init__(self):
        print("flying")

    def introduce(self):
        print("I'm a flyable")

    def fly(self):
        print("fly fly fly")

class Aeroplane(Vehicle, Flyable):
    pass

# class Aeroplane(Flyable, Vehicle):
#     def introduce(self):
#         print("I'm an aeroplane")


a = Aeroplane()
a.introduce()
a.go()
a.fly()

print(Aeroplane.__bases__)
print(Vehicle.__bases__)
print(Flyable.__bases__)