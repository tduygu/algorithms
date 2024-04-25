# import sys
#
# user_name = input("What is your name? ")
# if user_name == '':
#     print("Empty name! I'm closing the program.")
#     sys.exit()
# print(f"Hello {user_name}")

###########################################333333
def func(x,y):
    return x/y

try:
    func(3,0)
except BaseException:
    print("Error 3")
except ZeroDivisionError:
    print("Error 2")
# except BaseException:
#     print("Error 3")
except:
    print("Error 1")



