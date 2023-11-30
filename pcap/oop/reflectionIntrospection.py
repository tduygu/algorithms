# create a function that modifies all string properties of any object
# by turning them into empty strings

def empty_strings(user_object):
    for prop_name in user_object.__dict__.keys():
        prop_value = getattr(user_object, prop_name)
        if isinstance(prop_value, str):
            setattr(user_object, prop_name, '')


class Doctor():
    def __init__(self, first_name = 'Zekai', last_name='Tuncay'):
        self.first_name = first_name
        self.last_name = last_name
        self.__format_names()

    def __format_names(self):
        self.first_name = self.first_name.title()
        self.last_name = self.last_name.title()

    def introduce(self):
        print('Hi, I am', self.first_name)


kuli = Doctor('Kemal', 'Kılıç')
kuli.introduce()
empty_strings(kuli)
kuli.introduce()