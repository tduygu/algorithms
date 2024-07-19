import random
# Which code snippet do you need to insert to get the following output:
# [5, 6, 8, 2, 4, 3, 10, 7, 9, 3]
x = [random.randint(1, 10) for i in range(10)]
print(x)

y = [random.randrange(1, 10) for i in range(10)]
print(y)

z = [int(random.random()*10) for i in range(10)]
print(z)

t =random.sample([i for i in range(1,11)], 10)
print(t)

# Explanation:
# All answers use a list comprehension and a function from the random module.
#Let's review each suggested answers:

#--> x=[random.randint(1, 10) for i in range(10)]  :
# Function randint(1, 10) will produce a random integer which falls in the range [1,10] (with 10 included). So, this code could produce the output shown in the question.

#--> x=[random.randrange(1, 10) for i in range(10)] :
# Function randrange(1, 10)  will produce a random integer taken from the range : range(1,10)  - that means 10 is excluded - So, this code cannot produce the output shown in the question (since 10 is one of the number in the expected output)

#--> x=sample([i for i in range(1,11)],10) :
# this will produce a list of ten integers taken from the range range(1,11) - but each integer is only selected once (that's what the function sample() does).  So, this code cannot produce the output shown in the question since 3 is repeated twice in the expected output.

#--> x=[int(random.random()*10) for i in range(10)] :
# Function random()  generates a float number between 0.0 and 1.0 (excluded). int(random.random()*10)  will return an integer (thanks to the int() function) between 0 and 10 (excluded) - So, this code cannot produce the output shown in the question (since 10 is one of the number in the expected output).


