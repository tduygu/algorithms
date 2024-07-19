# OOP Principles
# 1. encapsulation
# 2. abstraction
# 3. inheritance
# 4. polymorphism

# encapsulation:
# Objects should keep their state private and only expose a set of public functions to the outside world.

# abstraction:
# Objects should keep the details of how they work to themselves and only expose some high level operations to the outside world.



class Car:
    def __init__(self, model, colour, initial_speed = 0):
        self.model = model
        self.colour = colour
        if initial_speed < 0:
            # private property __
            self.__speed = 0
        else:
            self.__speed = initial_speed

    def speed_up(self):
        if self.__speed < 0:
            self.__speed = 0
        else:
            self.__speed += 5

    def slow_down(self):
        if self.__speed < 5:
            self.__speed = 0
        else:
            self.__speed -= 5

    def show_speed(self):
        print("Current speed:", self.__speed)

lovely_car = Car("Amarok", "black", -50)
lovely_car.speed_up()
lovely_car.show_speed()



class Dog():
    counter = 0
    def __init__(self, name, age):
        self.name = name
        self.age = age
        Dog.counter += 1

my_pet = Dog('Pati', 3)
print(my_pet.__dict__)
my_pet.colour = "white"
print(my_pet.__dict__)
del my_pet.name
print(my_pet.__dict__)

# bu silinen ve eklenen propertyler object variable ya da instance variable
# specifically related to an object
# peki eklenen, cikarilan proplarin olup olmadigini nasıl bilecegiz? : __dict__ ile

# peki ya class'da private property varsa, __dict__ onu da gösterir mi?


class Cat():
    def __init__(self, name, age):
        self.__name = name
        self.age = age

my_cat = Cat('Zeytin', 4)
print(my_cat.__dict__)

#out:
#{'_Cat__name': 'Zeytin', 'age': 4}
# name mangling
#print(my_pet.__name)

# bu hata alır fakat private olması beklenen __name özelliğine şu şekilde erişilit:
print(my_cat._Cat__name)

my_cat.__breed = "van kedisi"
print(my_cat.__dict__)
my_cat.__breed = "aaa"
print(my_cat.__dict__)

# class variables
# counter which counts created objecs in the Dog class

print(my_pet.counter)
# only one copy of class variable is shared among the objects
kates_pet = Dog('Fony', 5)
adams_pet = Dog('Luna', 1)
print(kates_pet.counter)
print(adams_pet.counter)

# __dict__ shows only the instance variable
print(Dog.counter)

# class variable da aynı şekilde private olabilir

print(Dog.__dict__)

if hasattr(Dog, 'counter'):
    print(Dog.counter)

if hasattr(my_pet, 'counter'):
    print(my_pet.counter)

if hasattr(my_pet, 'colour'):
    print(my_pet.colour)

print(type(my_pet))
print(type(my_pet).__name__)

print(Dog.__module__)


