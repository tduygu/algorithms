fruit_list1 = ['Apple', 'Berry', 'Cherry', 'Papaya']
fruit_list2 = fruit_list1
fruit_list3 = fruit_list1[:]


fruit_list2[0] = 'Guava'
fruit_list3[1] = 'Kiwi'

print(fruit_list1)
print(fruit_list2)
print(fruit_list3)

for ls in (fruit_list1, fruit_list2, fruit_list3):
    print(ls[0])


#fruit_list1[::2]=['Apple', 'Berry', 'Cherry', 'Papaya', 'kkkk']
#print(fruit_list1)
def f(t, values):
    t=1
    values[2]='n'

t=3
f(t, fruit_list1)
print(t, fruit_list1)
#
a= [1,2,3,4,5]
print(a[3:0:-1])
#
for i in range(1, 6):
    print(i)
#
aa = [1,2,3,4,5,6,7,8,9]
print(aa[::2])
#