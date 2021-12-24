
class MyInteger(object):
    def set_val(self, val):
        try:
            val = int(val)
        except ValueError:
            return
        self.val = val

    def get_val(self):
        return self.val

    def incremenet_val(self):
        self.val = self.val + 1


i = MyInteger()
i.set_val(9)
i.incremenet_val()
print(i.get_val())
# i.set_val('hi')
i.val = 'hi'
i.incremenet_val()
print(i.get_val())