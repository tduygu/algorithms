#SOLID - OCP - Open Close Principle
from enum import Enum


class Color(Enum):
    RED = 1
    GREEN = 2
    BLUE = 3

class Size(Enum):
    SMALL = 1
    MEDIUM = 2
    LARGE = 3

class Product:
    def __init__(self, name, color, size):
        self.name = name
        self.color = color
        self.size = size


#  OCP = open for extension, closed for modification
# After you write and modify a class you should not modify it instead you should extend it.

# breaking OCP
class ProductFilter:
    def filter_by_color(self, products, color):
        for p in products:
            if p.color == color : yield p

    def filter_by_size(self, products, size):
        for p in products:
            if p.size == size : yield p

    def filter_by_size_and_color(self, products, size, color):
        for p in products:
            if p.color == color and p.size == size:
                yield p

    