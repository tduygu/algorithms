# roots of quadratic equation
import math


class EquationOperations:
    def findRootsOfQuadraticEquation(self, a, b, c):
        delta = b * b - 4 * a * c
        # print(delta)
        if delta > 0:
            root1 = -b - math.sqrt(delta) / (2*a)
            root2 = -b + math.sqrt(delta) / (2*a)
            return root1, root2
        elif delta == 0:
            rootn = -b / (2 * a)
            return rootn, rootn
        else:
            return None, None


eq = EquationOperations()
A = int(input("Enter the first coefficient"))
B = int(input("Enter the second coefficient"))
C = int(input("Enter the third coefficient"))
print(f"Coefficients of the equation are a={A}, b={B}, c={C}")
(x1, x2) = eq.findRootsOfQuadraticEquation(A, B, C)
if (x1 is None):
    print("Roots are complex")
else:
    print(f"Roots of the equation are {x1} and {x2}")

