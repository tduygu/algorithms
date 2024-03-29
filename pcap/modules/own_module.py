print("I'm a module")
if __name__ == '__main__':
    print('File executed directly.')
else:
    print('File executed as a module')
    print(__name__)
