class MatrixOperations:
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
                subline.append(M[x][y]+N[x][y])

            Total.append(subline)

        return Total

a = MatrixOperations()
result = a.addMatrixes([[1,2,3,4,4,4], [4,5,6], [7,8,9], [11,11,11]], [[9,8,7], [6,5,4], [3,2,1]])
print("Result:")
for r in result:
    print(r)
#     for c in r:
#         print(c)



