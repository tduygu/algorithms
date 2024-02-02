class Vehicle:
    model = "Wolksvagen"
    def __init__(self, speed):
        self.__speed = speed + 5




car = Vehicle(10)
# print(car.__speed)

print(hasattr(Vehicle,'model'))

class Device:
    pass

print(issubclass(Device,Device))