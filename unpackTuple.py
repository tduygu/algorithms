fruits = ("apple", "banana", "pear")
print(fruits)
(a, b, c) = fruits
print(a)
print(b)
print(c)
(d, *g) = fruits
print(d)
print(g)

fruits2 = ("apple", "banana", "pear", "cherry")
(s1, *s2, s3) = fruits2
print(s2)
print(s3)