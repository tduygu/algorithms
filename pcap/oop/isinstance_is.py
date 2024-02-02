class Vehicle():
    def __init__(self, speed):
        self.speed = speed

class LandVehicle(Vehicle):
    def __init__(self, speed, wheel_count):
        super().__init__(speed)
        self.wheel_count = wheel_count

class Car(LandVehicle):
    pass


a = Vehicle(10)
b = LandVehicle(8,4)
c = Car(6,4)

print(isinstance(a, Vehicle))
print(isinstance(b, Vehicle))
print(isinstance(c, Vehicle))
print()
print(isinstance(a, LandVehicle))
print(isinstance(b, LandVehicle))
print(isinstance(c, LandVehicle))
print()
print(isinstance(a, Car))
print(isinstance(b, Car))
print(isinstance(c, Car))
print()
####
first_num = 5
second_num = 5
print(first_num is second_num)

third_num = 3
third_num += 2
print(first_num is third_num)
print()
####

first_str = "Teacher Ali"
second_str = "Teacher Al"
second_str += "i"
print(f"{first_str} - {second_str}")
print(first_str is second_str)



