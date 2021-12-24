class MyDict(dict):
    def __setitem__(self, k, v):
        print("setting a key and a value")
        dict.__setitem__(self, k, v)


dd = MyDict()
dd['a'] = 5
dd['b'] = 10

ff = dict()
ff['a'] = 5
ff['b'] = 10

gg = {"a": 5, "b": 10}

for key in dd.keys():
    print('{0} = {1}'.format(key, dd[key]))

print("dict ff:")
for key in ff.keys():
    print(f"{key} = {ff[key]}")

print("dict gg:")
print(gg)


class MyList(list):
    def __getitem__(self, index):
        if index == 0:
            raise IndexError
        if index > 0:
            index = index -1
        return list.__getitem__(self, index)

    def __setitem__(self, index, value):
        if index == 0:
            raise IndexError
        if index > 0:
            index = index -1
            list.__setitem__(self, index, value)

print("List subclassing examples")
x = [1, 2, 3, 4]
y = list([1, 2, 3, 4])
z = MyList([1, 2, 3, 4])

x.append("spam")
z.append("spam")

print(x)
print(y)
print(z)

print(x[0])
print(z[1])
print(z[4])
