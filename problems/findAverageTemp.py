from array import *

n = input('How many day''s temperature?')
tempOfDays = array('i')
for i in range(int(n)):
    t = input(f"Day {i+1}'s temp: ")
    tempOfDays.append(int(t))

print(tempOfDays)

avg = round(sum(tempOfDays) / len(tempOfDays),2)
print(f"Average temperature is {avg}")

aboveDays = [1 if d > avg else 0 for d in tempOfDays]
print(f"{sum(aboveDays)} day(s) above average")



