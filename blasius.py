##This Python code is for calculating Blasius profile
##Zhenyang Yuan, 28th, May, 2020
import numpy as np


##for current time step
def OdeSolve(f1, f2, f3, f1_t, f2_t, f3_t, d_eta, n):
    Update(f1, f2, f3, f1_t, f2_t, f3_t, n)
    for i in range(1, n):     #forward finit element discretization
        f1[i] = f1[i-1] + f2[i-1]*d_eta;  #f1' = f2*eta
        f2[i] = f2[i-1] + f3[i-1]*d_eta;  #f2' = f3*eta
        f3[i] = f3[i-1] - 0.5*f1[i-1]*f3[i-1]*d_eta;  #f3' = -0.5*f1*f3*eta


##for time interation advance
def TimeIntegral(f1, f2, f3, f1_t, f2_t, f3_t, d_eta, n):
    er = 1
    while er > 10e-5:
        #new gauss of f3[0] is obtained from this equation
        f3[0] = f3[0] - (f2[n-1] - 1)*(f3[1] - f3_t[1])/(f2[n-1] - f2_t[n-1])
        #update spatial values
        OdeSolve(f1, f2, f3, f1_t, f2_t, f3_t, d_eta, n)
        #final goal is to satisfy bc f2[n-1] = 1
        er = abs(f2[n-1] - 1)


##update from the last gauss
def Update(f1, f2, f3, f1_t, f2_t, f3_t, n):
    for i in range(0,n):
        f1_t[i] = f1[i]
        f2_t[i] = f2[i]
        f3_t[i] = f3[i]


##initialization
# f1 is f, f2 is f', f3 is f''
# f*_t stands for corresbonding value in the last time iteration
n = 100
f1 = np.zeros(n)
f2 = np.zeros(n)
f3 = np.zeros(n)
f1_t = np.zeros(n)
f2_t = np.zeros(n)
f3_t = np.zeros(n)
eta = np.linspace(0, 10.0, n) #eta = y/delta, eta-> infinty
d_eta = eta[1] - eta[0]

##BCs
f1[0] = 0
f2[0] = 0
#f2[n-1] = 1 this bc is for determining the end of code

##initial gausses (need two initial gausses for f3, one gauss is done be setting initial conditions)
f3[0] = 1
OdeSolve(f1, f2, f3, f1_t, f2_t, f3_t, d_eta, n)
#Since now, two gausses are obtained, Newton method is used next

##Time advance
TimeIntegral(f1, f2, f3, f1_t, f2_t, f3_t, d_eta, n)


#print(f2)

import matplotlib.pyplot as plt
#plt.plot(eta,f1)

##u = U*f'  in this case, U = 18
plt.plot(eta,18*f2)
plt.xlabel('$\eta = y/\delta_x$')
plt.ylabel('$u$')


##using polynomial to fit this curve
z = np.polyfit(eta, f2, 6)
print(z)
p = np.poly1d(z) #p = ... + p[5]*eta^5+p[4]*eta^4+p[3]*eta^3+p[2]*eta^2+p[1]*eta^1+p[0]

plt.plot(eta,18*p(eta),'-.')
plt.legend(['Blasius profile numerical result','Fitting curve'])

plt.show()
#plt.savefig('books_read.eps')
