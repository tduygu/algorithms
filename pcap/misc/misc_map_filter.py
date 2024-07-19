lambda_func = lambda i:i*2
initial_list =[1,5,7,11]

map_result = map(lambda_func,initial_list)
print(next(map_result))
# print(next(map_result))
# print(next(map_result))
# print(next(map_result))

for i in map_result:
    print(i, end=',')

print(list(map_result))
print("************")

print(list(map(lambda x:x*3,[1,2,3,4,5])))

print(list(filter(lambda x:x%2 == 0,[1,2,3,4,5,6,7,8,9,10])))

emails = ['abc@google.com',
          'baris@yuyu.com.tr',
          'aliveli',
          'sampleme@pythonanywhere.com',
          'puhutv']

print(list(filter(lambda a : '@' in a, emails)))

