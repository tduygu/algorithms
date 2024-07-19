class Animal:
    def __init__(self):
        self.species = "General specie"

    def produce_sound(self):
        print("general animal sound")

    def present(self):
        print("I can produce this sound:")
        self.produce_sound()


class Dog(Animal):
    def __init__(self):
        self.species = "Canis Familia"

    def produce_sound(self):
        print("woov woov")


a = Animal()
print(a.species)
a.produce_sound()
a.present()
print()
d = Dog()
print(d.species)
d.produce_sound()
d.present()