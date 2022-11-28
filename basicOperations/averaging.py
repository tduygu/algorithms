class Average:
    def arithmeticMean(self, list1):
        total = 0
        for a in list1:
            total += a

        avg = total / len(list1)
        return avg

    def geometricMean(self, list1):
        pass


lst = []
n = int(input("Enter number of elements for calculating arithmetic mean : "))

for i in range(0, n):
    element = float(input())
    lst.append(element)

print(lst)

art = Average()
mean_arithmetic = art.arithmeticMean(lst)
print(f"Arithmetic mean of the given list is {mean_arithmetic}")
