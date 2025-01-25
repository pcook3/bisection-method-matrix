import numpy as np

#Newton's Method Function
def newtraph(f,fp,x0,Ea=1.e-7,maxit=30):
    for i in range(maxit):
        x1 = x0 - f(x0)/fp(x0)
        ea = abs((x1-x0)/x1)
        if ea < Ea:  break
        x0 = x1
    return x1,f(x1),ea,i+1

#Function for f(x)
def f(x):
    return ((np.log(x))**2) - x - 1

#Function for f'(x)
def fp(x):
    return 2*((np.log(x))/(x)) - 1

#Initial x guess
x0 = 0.66

#Displaying Results
(xsoln,fxsoln,ea,n) = newtraph(f,fp,x0,Ea=1.e-5)
print('\n\nSolution = {0:8.5g}'.format(xsoln))
print('Function value at solution = {0:8.5e}'.format(fxsoln))
print('Relative error = {0:8.3e}'.format(ea))
print('Number of iterations = {0:5d}'.format(n))