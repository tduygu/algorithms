class Vehicle:
    class_message = 'This is the message from Vehicle class'
    def __init__(self, speed: object) -> object:
        self.speed = speed

class LandVehicle(Vehicle):
    def __init__(self, wheel_count):
        self.wheel_count = wheel_count
        print(super().class_message)

class WaterVehicle(Vehicle):
    def __init__(self, speed, colour):
        # Vehicle.__init__(self, speed)
        super().__init__(speed)
        self.colour = colour

    def speed_up(self):
        self.speed += 5

class Car(LandVehicle):
    pass

class Boat(WaterVehicle):
    def super_speed(self):
        print("Super speed activated.")
        super().speed_up()
        super().speed_up()
        super().speed_up()

print(issubclass(Car, LandVehicle))
print(issubclass(LandVehicle, Vehicle))
print(issubclass(Car, Vehicle))

my_car = Car(5)
print(my_car.__dict__)

my_boat = Boat(10, 'blue')
print(my_boat.__dict__)
print(my_boat.speed)
print(my_boat.class_message)
my_boat.super_speed()
print(my_boat.__dict__)
my_boat.speed_up()
print(my_boat.__dict__)