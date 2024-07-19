import string_utils

def halve_strings(string_list):
    lst = [string_utils.halve_string(item) for item in string_list]
    return lst

# print(halve_strings(['Mark', 'Lydia']))