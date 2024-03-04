import sys

user_name = input("What is your name? ")
if user_name == '':
    print("Empty name! I'm closing the program.")
    sys.exit()
print(f"Hello {user_name}")

