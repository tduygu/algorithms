#Fundamental Data Types

# int
# float
# bool
# str
# list
# tuple
# set
# dict

#Classes -> custom types

#Specialized Data Types - modules

# None

print(type(4+4))
print(type(2-4))
print(type(2/4))
print(type(8.8+1.3))
a = 2 ** 3
b = 5 // 4
c = 5 % 3
print(f"a = {a} Type of a: {type(a)}")
print(f"b = {b} Type of b: {type(b)}")
print(f"c = {c} Type of c: {type(c)}")

n = -37
print(bin(n))
print(n.bit_length())
print("------------------------------------------")
# Setting the data type
x = "Windy"
print(f"x = {x} Type of x: {type(x)}")
n = str("feeling")

x = 9
print(f"x = {x} Type of x: {type(x)}")
n = int(9)

x = 20.5
print(f"x = {x} Type of x: {type(x)}")
n = float(20.5)

y = 2 + 1j
print(f"y = {y} Type of y: {type(y)}")
n = complex(2 + 1j)

x = ["apple", "banana", "cherry"]
print(f"x = {x} Type of x: {type(x)}")
n = list(("apple", "banana", "cherry"))

x = ("apple", "banana", "cherry")
print(f"x = {x} Type of x: {type(x)}")
n = tuple(("apple", "banana", "cherry"))

x = range(6)
print(f"x = {x} Type of x: {type(x)}")
for a in range(6):
    print(a)

x = {"name": "John", "age": 45}
print(f"x = {x} Type of x: {type(x)}")
print(x["name"])
print(x["age"])
n = dict(name="John", age=45)

x = {"apple", "banana", "cherry", "cherry"}
print(f"x = {x} Type of x: {type(x)}")
n = set(("apple", "banana", "cherry"))

x = frozenset({"apple", "banana", "cherry"})
print(f"x = {x} Type of x: {type(x)}")

x = True
print(f"x = {x} Type of x: {type(x)}")
n = bool(5)

x = b"Hello"
print(f"x = {x} Type of x: {type(x)}")
for bb in x:
    print(bb)
n = bytes(5)
print(f"bytes(5) = {n}")

x = bytearray(5)
print(f"x = {x} Type of x: {type(x)}")

x = memoryview(bytes(5))
print(f"x = {x} Type of x: {type(x)}")

x = None
print(f"x = {x} Type of x: {type(x)}")




