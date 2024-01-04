import numpy as np
import sys

class Matrix:
    def __init__(self, row, col):
        self.r = row
        self.c = col
        self.mat = np.zeros((row, col))

    def getMat(self):
        for i in range(self.r):
            for j in range(self.c):
                self.mat[i][j] = float(input('enter A['+str(i)+']['+ str(j)+']:'))
        
                
    def matMul(self, m1, m2):
        sdfsdfsfs


C = Matrix(n, q)
A = Matrix(n, m)
B = Matrix(m, q)

C.matMul(A, B)
