import math


class Average:
    def arithmeticMean(self, list1):
        total = 0
        for a in list1:
            total += a

        avg = total / len(list1)
        return avg

    def geometricMean(self, list1):
        multply = 1
        for a in list1:
            multply *= a

        avg = multply ** (1/len(list1))
        return avg

    # def logofgeometricmean(self, list1):
    #     total = 0
    #     for a in list1:
    #         total += math.log(a)
    #
    #     avg = total / len(list1)
    #     return avg


lst = []
n = int(input("Enter number of elements for calculating arithmetic mean : "))

for i in range(0, n):
    element = float(input())
    lst.append(element)

print(lst)

art = Average()
mean_arithmetic = art.arithmeticMean(lst)
mean_geometric = art.geometricMean(lst)
# mean_geometric2 = art.logOfGeometricMean(lst)
print(f"Arithmetic mean of the given list is {mean_arithmetic} \n"
      f"Geometric mean of the given list is {mean_geometric}")

      # f"log of geometric mean is: {mean_geometric2}"
