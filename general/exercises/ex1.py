import random

def generate_random(lbound, ubound):
    r = random.choice(range(lbound, ubound+1))
    return r

while True:
    lbound = int(input("Enter the lower bound: "))
    ubound = int(input("Enter the upper bound: "))
    print(generate_random(lbound, ubound))

