import math
import scipy.optimize
import time
def function(x):
	return math.cos(x)/(1+x**2)
def proizv(x):
	return math.sin(x)*(1+x**2)*(-1)/(1+x**2)**2-2*x*math.cos(x)
print (scipy.optimize.bisect(function,0.1,2.4))
start_time=time.time()
#метод деления отрезка
for i in range (1000):
	scipy.optimize.bisect(function,0.1,2.4)
print ('time',time.time()-start_time)
#метод Ньютона
start_time=time.time()
for i in range (1000):
	scipy.optimize.newton(function,1.57,fprime=proizv)
print ('time',time.time()-start_time)
#метод секущих
start_time=time.time()
for i in range (1000):
	scipy.optimize.newton(function,1.57,fprime=None)
print ('time',time.time()-start_time)
#метод Брента
for i in range (1000):
	scipy.optimize.brentq(function,0.1,2.4)
print ('time',time.time()-start_time)
