class MatrixOperations:
    def createMatrix(self, rownum, colnum, dataList):
        C = []
        for x in range(rownum):
            subline = []
            for y in range(colnum):
                subline.append(dataList[x * colnum + y])

            C.append(subline)

        return C

    def addMatrixes(self, M, N):
        l = len(M) if len(M) < len(N) else len(N)
        Total = []
        for x in range(l):
            print(f"line {x}")
            print(M[x])
            print(N[x])
            lsub = len(M[x]) if len(M[x]) < len(N[x]) else len(N[x])
            subline = []
            for y in range(lsub):
                subline.append(M[x][y] + N[x][y])

            Total.append(subline)

        return Total

    def multiplyMatrixes(self, M, N):
        #     # 1. matrisin sütun sayısı ikinci matrisin satır sayısına eşit mi?
        C = []

        # M matrisinin satır sayısı
        i = len(M)
        j = len(N)
        # N
        k = len(N[0])

        if len(M) > 0:
            if len(M[0]) != len(N):
                return -1
            else:
                for ii in range(i):
                    # print(f"i={ii}")
                    subline = []
                    for kk in range(k):
                        subtotal = 0
                        # print(f"k= {kk}")
                        for jj in range(j):
                            # print(f"jj= {jj}")
                            subtotal += M[ii][jj] * N[jj][kk]

                        subline.append(subtotal)
                        # print(subline)
                    C.append(subline)

        return C


a = MatrixOperations()
result = a.addMatrixes([[1, 2, 3, 4, 4, 4], [4, 5, 6], [7, 8, 9], [11, 11, 11]], [[9, 8, 7], [6, 5, 4], [3, 2, 1]])
print("Result:")
for r in result:
    print(r)
#     for c in r:
#         print(c)

data = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'ö', 'p']
newMatrix = a.createMatrix(3, 4, data)
for n in newMatrix:
    print(n)

newMatrix2 = a.createMatrix(2, 6, data)
for n in newMatrix2:
    print(n)

m1 = [[1, 2], [3, 4], [5, 6]]
m2 = [[1, 2, 3], [4, 5, 6]]
multiplied = a.multiplyMatrixes(m1, m2)
for m in multiplied:
    print(m)
