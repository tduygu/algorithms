import math
#
# for name in dir(math):
#     print(name, end='\n')

########################################3

# print(math.ceil(3.6))
# print(math.floor(3.6))
# print(math.trunc(3.6))

# nearest integer not less than 3.0

# nearest integer not less than these numbers
print(math.ceil(3.1))
print(math.ceil(3.505))
print(math.ceil(3.945))
print(math.ceil(3.0))

# lowest number not less than the number itself
print(math.ceil(-5.4))
print(math.ceil(-5.9))

# ceil() ile hep büyüğü seçiliyor yani. -5 > -5.4

# floor() - nearest integer not greater than these numbers
print(math.floor(3.1))
print(math.floor(3.505))
print(math.floor(3.945))
print(math.floor(3.0))
print(math.floor(-5.4))
print(math.floor(-5.9))

# trunc()  simply removes the decimal part and returns the integer part, no rounding
print(math.trunc(3.1))
print(math.trunc(3.505))
print(math.trunc(3.945))
print(math.trunc(3.0))
print(math.trunc(-5.4))
print(math.trunc(-5.9))

# factorial()
print(math.factorial(4))

from math import sqrt as karekok
print(karekok(9))

#hypat()

print(math.hypot(3, 4))

x = round(5.76543, 2)
y = round(5.76543, 3)
print(x)
print(y)





