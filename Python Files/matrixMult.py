def matrixMult(a, b):
    if len(a[0]) != len(b):
        return "The number of columns in the first matrix must match the number of rows in the second matrix."
    else:
        result = [[0 for j in range(len(b[0]))] for i in range(len(a))]
        for i in range(len(a)):
            for j in range(len(b[0])):
                for k in range(len(b)):
                    result[i][j] += a[i][k] * b[k][j]
        return result


a = [[1, 2, 3], [4, 5, 6]]
b = [[7, 8], [9, 10], [11, 12]]
print(matrixMult(a, b))
