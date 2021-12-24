class GetSet(object):

    instance_count = 0
    __mangled_name = 'no privacy'

    def __init__(self, value):
        self._attrval = value

    @property
    def var(self):
        print('getting the "var" attribute')
        return self._attrval

    @var.setter
    def var(self, value):
        print('setting the "var" attribute')
        self._attrval = value

    @var.deleter
    def var(self):
        print('deleting the "var" attribute')
        self._attrval = None

me = GetSet(5)
me.var = 1000
print(me.var)
print(me._attrval)

del me.var
print(me.var)

print(me._GetSet__mangled_name)


