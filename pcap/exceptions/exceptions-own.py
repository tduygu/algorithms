class AnimalValueError(ValueError):
    pass

def produce_animal_sound(animal_type):
    if animal_type == 'DOG':
        print("Woof woof!")
    elif animal_type == 'CAT':
        print("Meow!")
    else:
        raise AnimalValueError("Incorrect animal type!")

produce_animal_sound('CAT')

#produce_animal_sound('GGG')


class UserActionException(Exception):
    def __init__(self, message='', user_id=''):
        Exception.__init__(self)
        self.user_id = user_id
        self.message = message

    def __str__(self):
        return type(self).__name__ + ' occured. Error message: ' + self.message + ', user_id: ' + self.user_id

# def say_hello(name, userid):
#     if name == '':
#         raise UserActionException('empty name !', userid)
#     print("Hello ", name)


# try:
#     say_hello('Duygu', 'dtuncay')
#     say_hello('', 'abc')
# except Exception as e:
#     print(e)


class EmptyNameUserException(UserActionException):
    def __init__(self, user_id=''):
        super().__init__("An empty name was provided.", user_id)

def say_hello2(name, user_id):
    if name == '':
        raise EmptyNameUserException(user_id)
    print('Hello', name)


say_hello2('', 'duygu')



