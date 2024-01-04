def print_pascals_triangle(n):
    for i in range(n):
        for j in range(i + 1):
            print(combination(i, j), end=' ')
        print()

def combination(n, k):
    return int(factorial(n) / (factorial(k) * factorial(n - k)))

def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n-1)

print_pascals_triangle(4)
