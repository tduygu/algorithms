class Jedi:
    LightSaber = 1
    def __init__(self):
        self.force=10

class Sith(Jedi):
    def __init__(self):
        self.force=15

class Padawan(Sith):
    force = 5
    def __init__(self):
        super().__init__()

Luke = Padawan()

print(hasattr(Padawan, 'LightSaber'))
print(Luke.force)