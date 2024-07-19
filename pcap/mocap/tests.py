# 40
# class Server:
#     def __init__(self, colour):
#         self.colour = 'brown'
#         self.name = 'Atari'
#
# myserv = Server('black')
# myserv.attr = 'extra'
# print(myserv.__dict__)

##########################################

# 38
# class Sampl:
#     def __init__(self, vala, valb=0):
#         pass
#
# obj3 = Sampl(None)

##########################################
# 37
# def a():
#     hey = 5
#
#     def b():
#         print(hey)
#     return b
#
# x = a()
# print(x())
##########################################
# 35
# class A:
#     x = 'x'
#
#     def alarm(self):
#         print('a' + self.x)
#
#
# class B(A):
#     def alarm(self):
#         super().alarm()
#
#
# class C(B):
#     x = 'y'
#
#
# C().alarm()
##########################################

# 30
# class Art():
#     masterpiece = 'John'
#     def __init__(self):
#         self.name = 'One'
#
# print(len(Art().__dict__))
# print(Art().__dict__)

##########################################
# 29
# try:
#     raise Exception(0,1,[0,1])
# except Exception as e:
#     print(len(e.args))

##########################################
# 26
# class Dog:
#     def __init__(self, breed='none'):
#         self.breed = breed
#
#     def set(self, breed='labrador'):
#         self.breed = breed
#         return self.breed
#
#
# puppy = Dog()
# friend = puppy
# friend.set()
# print(puppy.breed)

##########################################
# 24
# print(__name__)
##########################################
# 23
# print(int(bytearray(10)[0]))
##########################################
# 22
# class Hamster():
#     def __init__(self, teeth_length):
#         self.__teeth_length = teeth_length
#
#
# ham = Hamster(5)
# print(ham.__teeth_length)

# 19
# class A:
#     b = 'b'
#
# def __init__(self):
#     self.c = 'c'
#     d = self.c
#
#
# a = A()
#print(a.d)
##########################################
# 28
# a = float('1,0')

##########################################
# 32
# try:
#     raise Exception
# except:
#     print('a')
# except BaseException:
#     print('b')
# except Exception:
#     print('c')

##########################################
# 10
# class X:
#     Y = 1
#     def __init__(self):
#         self.z = 0
#
# print(hasattr(X,'z'))
# print(hasattr(X(),'z'))
# print(hasattr(X,'Y'))
##########################################
# a = 2
# b = 3
# c = 2
# print(a**b**c)
##########################################
# class Class1():
#     def __init__(self, val):
#         self.value = val
#
# class Class2(Class1):
#     pass
#
# class Class3(Class1):
#     def __init__(self, val):
#         Class1.__init__(self, val)
#
# class Class4(Class1):
#     def __init__(self, val):
#         super().__init__(val)
#
#
# my_object1 = Class1(3)
# print(my_object1.value)
#
# my_object2 = Class2(3)
# print(my_object2.value)
#
# my_object3 = Class3(3)
# print(my_object3.value)
#
# my_object4 = Class4(3)
# print(my_object4.value)

##########################################
# __dict__ is predefined object variable which is a dictionary
# containing the names and values of all the properties (variables) the object is currently carrying.
#
# However, the force property has been defined privately
# (note the two underscores in front of force).
# In that case, Python uses "name mangling" when accessing the property from outside the class :
#     it puts the class name before the property name and puts an additional underscore at the beginning -->
#     that's the second element of the dictionary : '_Jedi__force': 10.
# class Jedi:
#     count_class = 0
#     def __init__(self, name):
#         self.name = name
#         count_local = 5
#
#     def set_force(self, val):
#         self.__force = val
#
#
# Luke = Jedi('Luke')
# Luke.set_force(10)
# Luke.lightsaber = True
#
# print(Luke.__dict__)
# print(Luke._Jedi__force)
# print(Jedi.count_class)
# jj = Jedi('jj')
# jj.count_class += 5
# jj.set_force(3)
# print(Jedi.__dict__)
# print(jj.__dict__)

#############################################################################
#It is very important to understand the difference between class variable, instance variable and local variable.

#############################################################################
# __dict__ is a predefined property of all Python objects :
# this variable is a dictionary and contains the names and values of all the variables the object is currently carrying.
# A few things to remember about __dict__ for an object :
# - class variable will not appear in the __dict__ variable of an object.
# - private instance variable defined inside the class will appear in the dictionary using "name mangling", i.e. : _
# className__variable where className is the name of the class where that private instance variable is defined.
# - private instance variable defined outside the class will appear in the dictionary as __variable
#############################################################################
# class Jedi:
#     def __init__(self):
#         self.force = 10
#
#
# class Sith:
#     def __init__(self):
#         self.force = 15
#         self.bases = 1
#
#
# class Padawan(Sith, Jedi):
#     def __init__(self):
#         super().__init__()


# Luke = Padawan()
# print(Padawan.__bases__)  # (<class '__main__.Sith'>, <class '__main__.Jedi'>)
# print(Luke.bases)  # 1
# print(Luke.__bases__)  # AttributeError: 'Padawan' object has no attribute '__bases__'


# __bases__  is a predefined property of a class. It is a tuple and contains the classes (not the class names)
# which are direct superclasses of the class.
########################################################################################################################

# The function issubclass() is able to determine if Class_1 is a subclass of Class_2 :
# issubclass(Class_1, Class_2)  will return True if Class_1 is a subclass of Class_2 and False otherwise.
# The function isinstance() checks if an object comes from an indicated class:
# isinstance(Object, Class) will return True if Object comes from class  Class and False otherwise.

# print(issubclass(Padawan, Sith))
# print(issubclass(Padawan, Jedi))
# print(issubclass(Jedi,Padawan))

########################################################################################################################
# import math
# print(math.__dict__)
# def traverseDict(dict):
#     for key in dict:
#         # print(key, dict[key])
#         print(f"{key} : {dict[key]}")
#
# traverseDict(math.__dict__)
#
# print(dir(math))

###########################################################
print()