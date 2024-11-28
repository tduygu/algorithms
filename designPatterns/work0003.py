# LSP
class Rectangle:
    def __init__(self, width, height):
        self._height = height
        self._width = width

    @property
    def area(self):
        return  self._width * self._height

    def __str__(self):
        return f"Width: {self.width}, height: {self.height}"

    @property
    def width(self):
        return self._width

    @width.setter
    def width(self, value):
        self._width = value

    @property
    def height(self):
        return self._height

    @height.setter
    def height(self, value):
        self._height = value

# This breaks LSP
class Square(Rectangle):
    def __init__(self, size):
        Rectangle.__init__(self, size,size)

    # These setters directly violate Liskov Substitution Principle
    @Rectangle.width.setter
    def width(self, value):
        self._width = self._height = value

    @Rectangle.height.setter
    def height(self, value):
        self._height = self._width = value

def use_it(rc) :
    w = rc.width
    rc.height = 10
    expected = int(w*10)
    print(f"Expected an area of {expected}, got {rc.area}")

rc= Rectangle(2,3)
use_it(rc)

sq = Square(5)
use_it(sq)
# The kind of high level problem is that we now have this function which uses a rectangle which only
# works on a rectangle and does not work on any derived classes.
# This is a direct violation of the Liskov substitution principle, which states that
# whenever you have an interface taking some sort of base class, you should be able to stick in any of its inheritors.
# Base classtan türetilmiş tüm derived classlar için base classın metotları doğru bir şekilde çalışıyor olmalı.
