# You are given an n x n 2D matrix representing an image, rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.
def rotate(matrix):
    num_sutun = len(matrix[0])
    t = [[0] * num_sutun for i in range(len(matrix))]
    for j in range(num_sutun):
        for i in range(len(matrix)):
            #print(matrix[len(matrix) - 1 - i][j])
            t[j][i] = matrix[len(matrix) - 1 - i][j]
    return t

def rotateSelf(matrix):
    n = len(matrix)
    for i in range(n):
        for j in range(i, n):
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    for row in matrix:
        row.reverse()

matrix1 = [[1,2,3], [4,5,6], [7,8,9]]

#print(matrix1[0][2])
#tt = rotate(matrix2)
#print(tt)
rotateSelf(matrix1)
print(matrix1)

