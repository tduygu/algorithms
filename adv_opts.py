class SumList(object):
    def __init__(self, this_list):
        self.myList = this_list

    def __add__(self, other):
        new_list = [x + y for x, y in zip(self.myList, other.myList)]
        return SumList(new_list)

    def __repr__(self):
        return str(self.myList)

cc = SumList([1, 2, 3, 4, 5])
dd = SumList([100, 200, 300, 400, 500])

ff = [1, 2, 3, 4, 5]
gg = [100, 200, 300, 400, 500]

ee = cc + dd
# print(ee.myList)
print(ee)
hh = ff + gg
print(hh)