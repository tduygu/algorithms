import random

# print(random.random())
# print(random.random())
# print(random.random())

#################################

# random.seed(0)
# print(random.random())
# print(random.random())
# print(random.random())

#################################

# numbers = [1, 2, 3, 6, 8, 15, 22, 23, 24]
# names = ['Ali', 'Ahmet', 'Rüzgar', 'Duygu', 'Özgür', 'Sezgin']
# şüpheliler = ['Ümit Akçakaya', 'Ayşegül veya Ankaradakiler', 'kuzenler', 'Bilge teyzem', 'bilmediğim biri', 'kadın', 'Selçuk Büyüktanır']
# yapilabilecekler = ['işlerine devam et', 'meditasyon', 'yoga', 'max konsantre olduğun bir iş', 'resim', 'gizliliği arttır']
#
# print(random.choice(numbers))
# print(random.choice(names))
# print(random.choice(şüpheliler))
# print(random.choice(yapilabilecekler))
#
# print(random.choice('BanaOnunBaşHarfiniVer'))

###################################################################################################

# numbers = [1, 2, 3, 6, 8, 15, 22, 23, 24, 32]
# for i in range(3):
#     print(random.choice(numbers))

###################################################################################################

# names = ['Ali', 'Ahmet', 'Rüzgar', 'Duygu', 'Özgür', 'Sezgin']
# print(random.sample(names, 3))

###################################################################################################
# import random
#
# def generate_tickets(ticket_count, max_number):
#     lst1 = []
#     for y in range(max_number):
#         lst1.append(y)
#
#     ticket_list = random.sample(lst1, ticket_count)
#     return ticket_list, random.choice(ticket_list)
#
#
# generate_tickets(5, 100)

###################################################################################################
import random


def generate_tickets(ticket_count, max_number):
    list_to_return = random.sample(range(0, max_number), ticket_count)
    return (list_to_return, random.sample(list_to_return, 1)[0])


generate_tickets(5, 100)
