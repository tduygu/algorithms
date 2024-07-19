def halve_string(input_string):
    h = int(len(input_string)/2)
    if len(input_string) % 2:
        h +=1
    return input_string[:h], input_string[h:]

# a= 'ali'
# b=('a')
# print(halve_string(a))
# print(halve_string(b))