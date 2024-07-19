print('hi there'[1:])
print('hi there'[3:6])
print('I\'m Adrian')

print(ord('a'))
print(ord('A'))
print(chr(97))

multiple_line_string = '''line 1
line 2'''
print(multiple_line_string)
print(len(multiple_line_string))

print('aaa'+'bbb')
print(2*'c')
print(2+5)
print('This is operator overloading.\nIf the order doesn\'t matter, it\'s called commutative')
# if the order doesn't matter we say that it's commutative 5+3 - 3+5
# if the order matters it's not commutative 'bbb'+'aaa' = 'bbbaaa'

for k in 'hey there':
    print(k, end='-')

txt = 'you can\'t delete from this text'
# del txt[0]

print()
print(min('ilovetravellingaroundtheworld'))
print(min('ilove travellingaroundtheworld'))
print(max('ilovetravellingaroundtheworld'))