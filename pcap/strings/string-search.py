print('ilovetravellingtheworld'.index('a'))

my_text = 'This is my sample text'
print(my_text.index('is'))
print(my_text.find('is'))

my_text = 'This is my sample text'
# print(my_text.index('are')) # gives error
print(my_text.find('are'))
#

print(my_text.find('ex',10))
print(my_text.find('ex',10,15))

print(my_text.rfind('ex'))

print()
mtext = 'work work work'
print(mtext.find('work'))
print(mtext.rfind('work'))
print(mtext.find('work',2))
print(mtext.rfind('work',2))
print(mtext.find('work',2,5))
print(mtext.rfind('work',2,5))
print(mtext.find('work',2,9))
print(mtext.rfind('work',2,9))

######################################################################
print('Duygu'.isalnum())
print('Duygu 13'.isalnum())
print('Duygu13'.isalnum())
print('Duygu_aa'.isalnum())

print('Duygu'.isdigit())
print('Duygu aa'.islower())
print('Duygu AA'.isupper())
print('DUYGU AA'.isupper())
print('   '.islower())
print('   '.isspace())
print('\n\n\n'.isspace())





