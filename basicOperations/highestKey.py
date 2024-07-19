
# Key with the Highest Value
#Define a function which takes a dictionary as a parameter and returns the key with the highest value in a dictionary.

#Example:

my_dict = {'a': 5, 'b': 9, 'c': 2}
#max_value_key(my_dict))
#Output:
#b

def max_value_key(dict):
    list1 = [val for val in my_dict.values()]
    list1.sort(reverse=True)

    for key, value in dict.items():
        if value == list1[0]:
            return key

def max_value_key2(my_dict):
    return max(my_dict, key=my_dict.get)

print(max_value_key(my_dict))