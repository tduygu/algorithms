import random

class Animal(object):
    def __init__(self, name):
        self.name = name

    def eat(self, food):
        print('{0} eat {1}'.format(self.name, food))

class Dog(Animal):
    def __init__(self, name):
        super(Dog, self).__init__(name)
        self.breed = random.choice(['Shih Tzu', 'Beagle', 'Mutt'])

    def fetch(self, thing):
        print('{0} goes after the {1}!'.format(self.name, thing))

d = Dog('Badi')
print(d.name)
print(d.breed)
