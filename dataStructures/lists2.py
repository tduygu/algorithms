prev_list = [1, 2, 3, 4]
new_list =[item*2 for item in prev_list]
new_list2 = [i for i in prev_list if i%2==0]
print(new_list)
print(new_list2)

#########################

language = "Python"
lang_list = [letter for letter in language]
print(lang_list)

#########################

# list comprehension can be used for list, range, string and tuple

#########################
sentence = 'My name is Duygu'

def is_consonant(letter):
    vowels = 'aeiıöouü'
    return letter.isalpha() and letter.lower() not in vowels

consonents = [i for i in sentence if is_consonant(i)]
print(consonents)

c1 = [l.isalpha() for l in sentence]
print(c1)
c2 = [l.isalpha() and l.lower() for l in sentence]
print(c2)

#########################

k1 = [-100, 102, 75, -3, 80, 82]
k2 = [i if i>0 else 0 for i in k1]
print(k2)

