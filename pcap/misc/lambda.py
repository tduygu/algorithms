def sum(x, y):
    return x + y

a =lambda x,y : x+ y

print(sum(3, 5))
print(a(3,5))


def apply_func(elements, func):
    for element in elements:
        print(func(element))

b = lambda x: x * x
c = lambda y : 1 / y
d = lambda x : 5

b_list = [5,13, 8, 9,2]
apply_func(b_list,b)
print("************")
apply_func(b_list, c)
print("************")
apply_func(b_list,d)
print("************")


