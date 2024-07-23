x = lambda a: a + 10
print(x(5))

y = lambda a, b: a * b
print(y(2, 5))

z = lambda a, b, c: a + b + c
print(z(5, 9, 8))

def multMe(n):
    return lambda a: a * n
# gelen deger herneyse ona sunu yap

def multMex(n, m):
    return n * m

s = multMe(5)
print(type(s))
print(s)
print(s(4))
