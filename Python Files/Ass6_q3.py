def longseq(L):
    n = len(L)
    A  = [1] * n
    for i in range(0, n):
        for j in range(i):
            if L[i] > L[j]:
                A[i] = max(A[i], A[j] + 1)
    return max(A)

lst = [100, 22, 9, 33, 21, 50, 41, 60, 59]
print(longseq(lst))


