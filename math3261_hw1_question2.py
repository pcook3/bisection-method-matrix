import numpy as np

#Fixed Point Iteration Function
def fixpt(g,x0,Ea=1.e-7,maxit=30):
    for i in range(maxit):
        x1 = g(x0)
        ea = abs((x1-x0)/x1)
        if ea < Ea: break
        x0 = x1
    return x1,ea,i+1

#Equation g(x)
def g(x):
    return (x+2)/(x+1)

#Initial x value
x0 = 1

#Displaying Results
xsoln,ea,n = fixpt(g,x0)
print('\n\nSolution = {0:8.5g}'.format(xsoln))
print('Relative error = {0:8.3e}'.format(ea))
print('Number of iterations = {0:5d}'.format(n))
