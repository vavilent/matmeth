import numpy as np
n=101
A=np.zeros((n,n))
i,j=np.indices(A.shape)
for k in range (3):
	A[i==j+k]=1
B=np.arange(n)
X=np.linalg.solve(A,B)
print (A)
print (B)
print (X)

