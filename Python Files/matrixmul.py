import sys
import numpy as np

A = [[1, 0], [-2, -2]]
B = [[1, -3], [0, 1]]
(n, m) = (len(A), len(A[0]))    # n = rows & m = columns
(p, q) = (len(B), len(B[0]))

if m != p:
    sys.exit('Dimension mismatch')

C = []
for i in range(n):
    row = []
    for j in range(q):
        row.append(0.0)
    C.append(row)

# alternatively C = np.zeros((p,q))
    
for i in range(n):
    for j in range(q):
        sumV = 0.0
        for k in range(m):
            sumV += A[i][k]*B[k][j] 
        C[i][j] = sumV

# print(C)

# Another method
import sys

def Mat_mul(m1, m2):                          ## Cubic time complexity
    n, m = len(m1), len(m1[0])
    p, q = len(m2), len(m2[0])
    if m != p:
        return sys.exit("Multiplication not possible")
    else:
        C2 = []
        for i in range(n):
            C1 = []
            for j in range(q):
                sum = 0
                k = 0
                while k < p:
                    ele = m1[i][k] * m2[k][j]
                    sum = sum + ele
                    k = k + 1
                C1.append(sum)
            C2.append(C1)
        return C2


A = [[1, 2, 3], [2, 5, 3], [1, 0, 8]]
B = [[-40, 16, 9], [13, -5, -3], [5, -2, -1]]
print(Mat_mul(A, B))

