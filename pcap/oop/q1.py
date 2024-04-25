class Lambda():
    L=2
    def __init__(self, x=0):
        self.l = x+1
        self.__m = x

    def set(self, y=2):
        self.k = y+1


class Omega(Lambda):
    M=2
    def __str__(self):
        return str(super().L)

m=Omega()
m.__n=3

print(m.__dict__)
print(m._Lambda__m)
print(m)
print(hasattr(m,'k'))

m.set(5)
print(hasattr(m,'k'))
print(m.__dict__)