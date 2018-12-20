import numpy
import scipy.linalg
import timeit

A=numpy.random.random((50,50))
k=numpy.arange(50)
def b(k,t):
        return (k/(1+k*t))
start=timeit.default_timer()
for t in numpy.linspace(0,10,100):
    x1=scipy.linalg.solve(A,b(k,t))
    #print x1
stop=timeit.default_timer()-start
print(stop)

start=timeit.default_timer()
LU=scipy.linalg.lu_factor(A)
for t in numpy.linspace(0,10,100):
    x2=scipy.linalg.lu_solve(LU,b(k,t))
    #print x2
stop=timeit.default_timer()-start
print(stop)

start=timeit.default_timer()
Ainv=scipy.linalg.inv(A)
for t in numpy.linspace(0,10,100):
    x3=scipy.linalg.solve(Ainv,b(k,t))
    #print x3
stop=timeit.default_timer()-start
print(stop)
