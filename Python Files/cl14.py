def simpleSum(n):
    res = 0
    # assert: n > 0
    # INV: at step i: res holds the sum of first i integers
    for i in range(1, n+1):
        res = res + i
    #print("sum:", res)

#n = int(input("Enter the number: "))
#simpleSum(n)

def fact(n):
    # assert: n > 0
    res = 1
    #INV: at step i, res holds i!
    for i in range(2, n+1):
        res = res*i


# compute sin(x) = x - x^3/3! + x^5/5! ...         
"""
x^3/3! = x^2/3.2 . x/1!
x^5/5! = x^2/5.4 . x^3/3!

;;;
ith term = x^2/i*(i-1). <previous-term>
"""

def sinFun(x, tol):
    term = x
    tsin = x
    i = 1
    x2 = x*x
    #INV: after jth iteration:
    # i = 2j+1 /\
    # term = -1^j.x^i/i! /\
    # tsin is the sum of first j + 1 terms
    while abs(term) > tol:
        i = i + 2
        term = -(term*x2)/(i*(i-1))
        tsin = tsin + term

    print("sin(", x,"):", tsin)

#sinFun(1.57, 0.000001)


#OR
#Difference is in the expression of nth term
#ith term = -x^2/((2*i-1)(2*i-2))

""""
def sinFun(x, tol):
    term  = x
    tsin = x
    i = 1
    x2 = x*x
    #INV: after jth iteration:
    # i = j+1 /\
    # term = -1^(j+2).x^(2*i-1)/i! /\
    # tsin is the sum of first j + 1 terms
    while abs(term) > tol:
        i = i + 1
        term = -(term*x2)/((2*i-1)*(2*i-2))
        tsin = tsin + term

    print("sin(", x,"):", tsin)

sinFun(0.5, 0.000001)
"""

#Fibonacci

def fibo(n):
    a = 0
    b = 1
    if n == 1:
        return 0
    else:
        i = 2
        while i <= n:
            i = i + 1
            temp = a+b         #INV:
            a = b              #After jth iteration, b gives (j+1)th term of the fib series
            b = temp
        return b
#print(fibo(5))

def gcd(a,b):                           # This function uses Euclidean
    assert a, b > 0                     # algorithm to find GCD of two numbers:
    #INV: ?                             # if A = B.Q + R, then GCD(A, B) = GCD(B, R)
    while True:
        r = a%b
        a = b
        b = r
        if r == 0:
            break   #will come out of while loop
        else:
            continue  #pass can also be used
    print("gcd:", a)

#gcd(20, 168)

"""
fastPow(3,4): 
     n = 2
     pseq = 9

     n = 1
     pseq = 81

     prod = 81
     n = 0
     pseq = 81*81 
"""        
def fastPow(x, n):
    # assert: x > 0, n >=0
    prod = 1
    pseq = x
    #INV: prod.pseq^i
    while n > 0:
        if n%2 == 1:
            prod = prod*pseq
            n = n//2
            pseq = pseq*pseq
        else:
            n = n//2
            pseq = pseq*pseq
    #print("fast power:", prod)

#fastPow(3, 4)

