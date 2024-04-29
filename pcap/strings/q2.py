x='Tatooine is a lawless Place ruled by Hutt gangsters.'

print(x.capitalize())
print(x.swapcase())
print(x.title())
print(x.upper())

##############################################################

my_list = ['carrot', 'potato', 'cauliflower', 'radish']
my_list.sort(key = lambda x: x[-2], reverse=True)
print(my_list)

# sort() is a method of the list class. It is similar to sorted() but with a few differences :
# - sorted() returns a new sorted list, while sort() sorts the list in place
# - sorted() can be used with an iterable (like a string for example), while sort() can only be used with lists.
# Both sort() and sorted() can be used with one of these optional keyword arguments:
# - reverse : if set to True, sorting is done in a descending order - if set to False, sorting is done in ascending order.
# - key : this argument is a function which will be used on each value in the list being sorted to determine the resulting order.

#this lambda function will extract the second to last character for each of the strings in my_list .
# For example : the lambda function applied to 'carrot' will return 'o' .
# The sort() method will then perform the sorting operation based on those resulting characters
# (note that the original strings are still returned; they are not actually modified by the function identified by key -
# the function in key is only used to figure out what to sort).

##############################################################

z = '\t\\'*2 + '\t'

print(z)
print(z.split('t'))
print(len(z.split('t')))
print(z.split('\t'))
print(len(z.split('\t')))
print('ok')

##############################################################
# ASCII : American Standard Code for Information Interchange
# ASCII is used for representing 128 English characters in the form of numbers, with each letter being assigned to a specific number in the range 0 to 127.
# Unicode provides a unique way to define every character in every spoken language of the world by assigning it a unique number.
# Unicode represents far more characters than ASCII. For backward compatibility, the first 128 Unicode characters point to ASCII characters.
# So, ASCII is essentially is a subset of Unicode.

##############################################################

m = 'abcdef'
print(m[::-3]*2)

print(m[::3])
print(m[1::2])

print(m[::-2])
print(m[1::-2])
print(m[4::-2])

#stepteki - gidiş yönünü değiştiriyor, start tan başlayıp stopa kadar ters yönde gidiyor.
# startın ya da stopun eksi olması baştan ya da sondan sayarak o indexin belirlenmesi ile ilgili
print(m[4:1:-2])

print(m[-3::-1])
print(m[-3:1:-1])
