# import sys, math
#
# for name in dir(sys):
#     print(name, end='\n')
#
# def exit():
#     print("I wanna exit")
#
# exit()
# sys.exit()

##################################################

from sys import exit

# def exit():
#     print("I wanna exit")

exit()

#####################################################
#from sys import *
# bu tehlikeli çünkü sys'deki birçok fonksiyoon senin aynı isimle yazdıkların tarafından ezilmiş olacak.
# bunun yerine
# import sys
# daha uygun, bu sys. namespace'i ile kullanmayı mecbur kılacak.

# import sys as s
#
# s.exit()

#######################################################

from sys import exit as bye_bye

bye_bye()