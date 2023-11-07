import random


class PasswordGenerator:
    def __init__(self, pass_length, include_digit, include_special, include_uppercase):
        self.pass_length = pass_length
        self.include_digit = include_digit
        self.include_special = include_special
        self.include_uppercase = include_uppercase

    def __str__(self):
        return f'''You provided password length as {self.pass_length} 
include digit : {self.include_digit}
include special character : {self.include_special}
include uppercase character : {self.include_uppercase}
'''

    def generate_password(self):
        lst_chars = []
        lst_uppers = []
        lst_digits = []
        lst_specials = ['!','@','#','$','%','&','*','^','|','(',')','_','+']

        for i in range(97,123):
            lst_chars.append(chr(i))
            i += 1

        for i in range(65,91):
            lst_uppers.append(chr(i))
            i += 1

        for i in range(48, 58):
            lst_digits.append(chr(i))
            i += 1


        # print(lst_chars)
        # print(lst_uppers)
        # print(lst_specials)
        # print(lst_digits)

        ind = 0
        generated_pass = []
        while ind < self.pass_length:
            if self.include_digit:
                generated_pass.append(random.choice(lst_digits))
                ind += 1
            if ind == self.pass_length:
                break
            if self.include_special:
                generated_pass.append(random.choice(lst_specials))
                ind += 1
            if ind == self.pass_length:
                break
            if self.include_uppercase:
                generated_pass.append(random.choice(lst_uppers))
                ind += 1
            if ind == self.pass_length:
                break
            generated_pass.append(random.choice(lst_chars))
            ind += 1
            if ind == self.pass_length:
                break

        return ''.join(generated_pass)

init_str = '''Choose option:
1: generate password
2: exit the program
'''

ch = input(init_str)
try:
    if ch == '2':
        print('Bye')
    elif ch == '1':
        print("Please provide your preferences: ")
        pl = input("Provide password length:")

        while int(pl) < 4:
            print("Minimum length must be greater then 3")
            pl = input("Provide password length:")
            if int(pl) == 0:
                break

        d = input("Use digits (y/n):")
        u = input("Use uppercase letters? (y/n):")
        s = input("Use special characters? (y/n):")

        pss = PasswordGenerator(int(pl),
                                (True if d=='y' or d=='Y' else False),
                                (True if s == 'y' or s == 'Y' else False),
                                (True if u == 'y' or u == 'Y' else False))
        print(pss)
        print(pss.generate_password())

    else:
        print("Please provide proper value")
        ch = input(init_str)
except:
    print("Please provide proper value")
    ch = input(init_str)

