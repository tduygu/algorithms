class Snake:
    count = 0
    def __init__(self, val):
        self.__count = val
        count = 2

class Python(Snake):
    def __init__(self,val):
        super().__init__(val)


my_snake = Python(1)
print(my_snake.__dict__)

#private prperty'e class dışından erişmek
print(my_snake._Snake__count)