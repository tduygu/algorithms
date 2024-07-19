numbers = [i for i in range(1, 101) if i % 3 != 0]
print(numbers)

numbers2 = [i for i in range(1, 101) if i % 2 ==0]
print(numbers2)

numbers3 = [0 if i % 2 ==0 else 1 for i in    range(100)]
print(numbers3)

table1 = [[i for i in range(1,6)] for j in range(5)]
print(table1)

