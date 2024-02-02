class Vehicle:
    def show_power_type(self):
        print("vehicle power")


class ElectricVehicle(Vehicle):
    def show_power_type(self):
        print("electric vehicle power")


class PetrolVehicle(Vehicle):
    def show_power_type(self):
        print("petrol vehicle power")


class HybridCar(ElectricVehicle, PetrolVehicle):
    pass
    # def show_power_type(self):
    #     print("hybrid vehicle power")


h = HybridCar()
h.show_power_type()
# according to MRO order
hasa