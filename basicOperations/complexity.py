class BigO:
    def multiplyMe(self, n):
        return n * n

    def printMe(self, n):
        for i in range(n):
            print(i)

    def printMeTwc(self, n):
        for i in range(n):
            print(i)

        for j in range(n):
            print(j)

    def printItems(self, n):
        for i in range(n):
            for j in range(n):
                print(f"{i} {j}")

    def printCubicItems(self, n):
        for i in range(n):
            for j in range(n):
                for k in range(n):
                    print(i, j, k)


b1 = BigO()

# O(1) - constant time complexity
# number of operations doesn't change according to the input
print(b1.multiplyMe(89))
print(b1.multiplyMe(45))

# O(n) linear complexity
# print operation takes place as many as the input
# finding the desired card from the deck of cards - in the worst case, operation is done number of cards time
# as the number of elements increases number of operations increases
b1.printMe(30)

# O(2N) complexity, constant can be dropped
b1.printMeTwc(3)

# O(n * n) = O(n^2)
b1.printItems(5)

# O(n * n * n) = O(n^3) => we say O(n^2)
b1.printCubicItems(4)




