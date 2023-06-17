my_dict = dict()
print(my_dict)

my_dict2 = {}
print(my_dict2)

eng_tr = dict(one='bir', apple='elma', mor='purple')
print(eng_tr)

eng_tr2 = {'two':'iki', 'happy':'mutlu', 'blue':'mavi'}
print(eng_tr2)

# list of tuples to dict
eng_tr3_list = [('two','iki'), ('happy','mutlu'), ('blue','mavi')]
eng_tr3 = dict(eng_tr3_list)

pers = {'name': 'Duygu', 'age':30 }
pers['age'] = 35
pers['surname'] = 'Tuncay'
pers['education'] = 'master'

print(pers)

def traverseDict(dict):
    for key in dict:
        print(key, dict[key])

traverseDict(pers)

def searchDict(dict, value):
    for key in dict:
        if dict[key] == value:
            return key, value
    return 'The value does not exist'

print(searchDict(pers, 28))
print(searchDict(pers, 'Duygu'))

### delete
# 1
# del pers['age']

# 2
#removed_element = pers.pop('age')
#print(removed_element)

# 3
#removed_element = pers.pop('address', None)
#print(removed_element)

# 4 removes the last one after python 3.8
#removed_element = pers.popitem()
#print(removed_element)

# 5
#pers.clear()

#print(pers)

### copy
pers2 = pers.copy()

print(pers)
print(pers2)

pers2['age'] = 45
print('Age is changed in the coppied one.')
print(pers)
print(pers2)

### fromkeys
pers3 = {}.fromkeys([1, 2, 3], 0)
print(pers3)

pers4 = {}.fromkeys(['ad', 'soyad', 'meslek'])
print(pers4)

### get
print(pers.get('education', 'high school'))
print(pers.get('education', 'master'))
print(pers.get('age'))

# items() - gives list of tuple pairs
print(pers.items())

# keys
print(pers.keys())

# popitem
print(pers.popitem())
print(pers)

# setdefault
print(pers.setdefault('name', 'Ali'))

pers.setdefault('entertainment')
pers.setdefault('yoyo', 'aha')
print(pers)

# pop
pers.pop('yoyo')
pers.pop('yaya', 'not')
print(pers)

# values()
print(pers.values())

# update() - one dict to another dict
pers5 = {'a':1, 'b':2, 'c':3}
pers.update(pers5)
print(pers)