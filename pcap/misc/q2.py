class A:
    X = 2
    def __init__(self, a, b):
        self.x = a + b
        self.__y = a-b

a = A(3, 2)
a.__z = 0
print(a.__dict__)
print(A.__dict__)