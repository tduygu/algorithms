class MyClass(object):
    def __enter__(self):
        print('we have entered "with"')
        return self

    def __exit__(self, type, value, traceback):
        print('we are leaving "with"')
        print('error type: {0}'.format(type))
        print('error value: {0}'.format(value))
        print('error traceback: {0}'.format(traceback))

    def sayhi(self):
        print('hi, instance %s' % (id(self)))


with MyClass() as cc:
    cc.sayhi()
    5/0

print('after the "with" block')

