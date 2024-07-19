list_1 = [2**x for x in range(5)]
print(list_1)

list_2 = list(map(lambda x: x//2, list_1))
print(list_2)

list_3 = list(filter(lambda x: x%2, list_1))
print(list_3)

list_4 = list(map(lambda x: x/2, list_1))
print(list_4)

list_5 = list(filter(lambda x: x//2, list_1))
print(list_5)

my_list1 =list('Skywalker')
my_list2 = list('Vader')
my_list3 = list(filter(lambda x: x not in my_list2,my_list1))
print(my_list3)