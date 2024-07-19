class Robot:
    def t(self):
        print('Robot')

class Droid:
    def t(self):
        print('Droid')

class ProtoDroid(Droid, Robot):
    def f(self):
        self.t()

R2D2 = ProtoDroid()
R2D2.f()
