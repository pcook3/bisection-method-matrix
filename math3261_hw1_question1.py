import numpy as np
import sys

def bisect1(func,xl,xu,maxit=20):
   
    if func(xl)*func(xu)>0:
        sys.exit('initial estimates do not bracket solution, re-run program\n')
    for i in range(maxit):
        xm = (xl+xu)/2
        if func(xm)*func(xl)>0:
            xl = xm
        else:
            xu = xm
    return xm

x=1


# Upon solving the matrix for it's determinant...
# Can be re-written as A = x^4 - 202x^2 + 1404x - 2475 = 5000 ...or set equal to zero (so we can find the roots): A = x^4 - 202x^2 + 1404x - 7475

#Function representing the determinant 
def A(x):
    determinant = (x ** 4) - (202 * (x ** 2)) + (1404 * x) - (7475)
    return determinant

#Gathering input for brackets
xl = int(input("\nLower Bound: "))
xu = int(input("Upper Bound: "))
answer = round(bisect1(A, xl, xu), 6)

#Displaying results
print(answer)

print("\n- - - - -\n")

#testing that answer
mtrix = np.array([
    [1, 2, 3, answer],
    [4, 5, answer, 6],
    [7, answer, 8, 9],
    [answer, 10, 11, 12]
    ])
det = round(np.linalg.det(mtrix), 6)
print(det)
print("\nYour answer was ", (abs(5000-det)),"off from 5000\n")
