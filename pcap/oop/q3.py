class Gamma:
    s = 5
    def __init__(self, val):
        self.g = val

class Kappa(Gamma):
    K = 0
    pass

k1 = Kappa(1)
k2 = Kappa(2)
k3 = k1
k3.g += 1

print(isinstance(k2,Gamma))
print(k1.g)
print(hasattr(k1,'s'))