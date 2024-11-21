def MatrixSpiral(strArr):
    # Convert strArr to a matrix of integers
    matrix = [list(map(int,row.strip('[]').split(','))) for row in strArr]
    print(f"Matrix is : {matrix}")
    result = []

    while matrix:
        # Move from left to right on the top row
        # print(matrix.pop(0))
        # print(f"Now the matrix is {matrix}")
        result += matrix.pop(0)

        # Move from top to bottom on the right column
        if matrix and matrix[0]:
            for row in matrix:
                result.append(row.pop())

        # Move from right to left on the bottom row
        if matrix:
            result += matrix.pop()[::-1]

        # Move from bottom to top on the left column
        if matrix and matrix[0]:
            for row in reversed(matrix):
                result.append(row.pop(0))

    return ",".join(map(str, result))



strArr = ["[1,2,3]", "[4,5,6]", "[7,8,9]"]
print(strArr)
print(MatrixSpiral(strArr))

strArr2 = ["[4,5,6,5]", "[1,1,2,2]", "[5,4,2,9]"]
print(strArr2)
print(MatrixSpiral(strArr2))

