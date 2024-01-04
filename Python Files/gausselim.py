import numpy as np
import sys
# can use arrays too using numpy

n = int(input('Enter the number of unknowns: '))
a = []
print('Enter the augmented matrix')
for i in range(n):
    row = []
    for j in range(n+1):
        elem = float(input('enter A['+str(i)+']['+str(j)+']: '))
        row.append(elem)
    a.append(row)


# Gauss Elimination

for i in range(n):
    if a[i][i] != 0:
        for j in range(i+1, n):
            factor = a[j][i]/a[i][i]
            for k in range(n+1):
                a[j][k] -= factor*a[i][k]

sol = np.zeros(n)
## x_0, x_1, ....., x_{n-1}
sol[n-1] = a[n-1][n]/a[n-1][n-1]

for i in range(n-2, -1, -1):
    sol[i] = a[i][n]
    for j in range(i+1, n):
        sol[i] = sol[i] - a[i][j]*sol[j]

    sol[i] = sol[i]/a[i][i]


# print solution
for i in range(n):
    print('x%d = %0.2f' %(i, sol[i]), end='\t')
