import numpy as np

twoDArray = np.array(([[5,6,8,3], [19,22,13,11], [15,14,18,16],[99,89,65,75]]))
print(twoDArray)

# O(n*m) - time complexity of creation of two dimensional array
# O(n*m) - space  complexity of creation of two dimensional array

# newTwoDArray = np.insert(twoDArray,0,[[1,2,3,4]], axis=1)
#newTwoDArray = np.insert(twoDArray,0,[[1,2,3,4]], axis=0)
#newTwoDArray = np.insert(twoDArray,2,[[1,2,3,4]], axis=0)
newTwoDArray = np.append(twoDArray,[[1,2,3,4]], axis=0)
print(newTwoDArray)

def accessElement(arr, rowInd, colInd):
    if rowInd >= len(arr) or colInd >= len(arr[0]):
        print("No element at this index")
    else:
        print(arr[rowInd][colInd])

accessElement(twoDArray, 5, 3)
accessElement(twoDArray, 2, 1)

def traverse2Darray(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j])

traverse2Darray((newTwoDArray))

# deletion
print(twoDArray)
twoDArr3 = np.delete(twoDArray, 0, axis = 0)
print(twoDArr3)
twoDArr4 = np.delete(twoDArray, 1, axis= 1)
print(twoDArr4)

# numpy modülde deletion ve insertionda işlemi yeni bir array oluşturarak yapıyor
# o yüzden space complexityleri de O(mn)