#Lab-1
#Q1.
# a = float(input())
# b = float(input())

# print("Addition: ", a+b)
# print("Subtraction: ", a-b)
# print("Multiplication: ", a*b)
# if b == 0:
#     print("Cannot be divided")
# else:
#     print("Division: ", a/b)
# print("Exponentiation: ", a**b)
# print("L2-norm: ", (a**2 + b**2)**0.5)

#Q2.
# n = float(input())

# print((9*n/5) + 32)

#Q3.
# a = float(input())
# b = float(input())

# n = a**2 + b**2

# if n < 1:
#     print("inside")
# elif n > 1:
#     print("outside")
# else:
#     print("on")

#Q4.
# a = int(input())
# h = a//3600
# m = (a-h*3600)//60
# s = a - (h*3600 + m*60)
# print("Hours: ", h)
# print("Minutes: ", m)
# print("Seconds: ", s)

#Q5.
# m = int(input())

# if 80 <= m <= 100:
#     print("A")
# elif 70 <= m <= 79:
#     print("A-")
# elif 61 <= m <= 69:
#     print("B")
# elif 45 <= m <= 40:
#     print("B-")
# elif 31 <= m <= 44:
#     print("C")
# else:
#     print("F")

#Q6.
# a = float(input())
# b = float(input())
# c = float(input())

# D = b**2 - 4*a*c

# if a != 0:
#     r1 = (-b + (D)**0.5)/(2*a)
#     r2 = (-b - (D)**0.5)/(2*a)
#     if D > 0:
#         if a > 0:
#             print(r2, r1)
#         else:
#             print(r1, r2)      
#     elif D == 0:
#         print(r1, r2)
#     else:
#         print("No real roots")
# else:
#     print("Not a valid quadratic equation")

#Q7.
# u = float(input())
# a = float(input())
# t = float(input())

# print(u + a*t)

#Q8.
# p = float(input())
# r = float(input())
# t = float(input())

# print((p*r*t)/100)


#Lab-2
#Q1.
# x = float(input())
# n = int(input()) 

# res = 1
# for i in range(1, n+1):
#     res = res*x
# print(res)

#Q2.
# n = int(input())     
# assert n >= 0

# for i in range(1, 11):
#     print(n, "x", i, "=", n*i)

#Q3.
# n = int(input())
# s = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
# assert 1 <= n <= 26
# for i in range(1, n+1):
#     for j in range((i*(i-1)//2) + 1, (i*(i+1)//2) + 1):
#         if j <= n:
#             print(s[j-1], end=" ")
#         else:
#             break
#     if j < n:
#         print("")
#     else:
#         break

#Q4.
# x = float(input())
# th = float(input())

# def fac(n):
#     assert n >= 0
#     val = 1
#     for i in range(1, n+1):
#         val = val*i
#     return val

# res = 0
# k = 0
# while x**k/fac(k) >= th:
#     m = k//2
#     res = res + ((-1)**m)*x**k/fac(k)
#     k = k + 2
# print(res)

#Q5.
# n = int(input())

# def t(n):
#     if n == 1:
#         return 0
#     elif n == 2:
#         return 0
#     elif n == 3:
#         return 0
#     elif n == 4:
#         return 1
#     else:
#         return (t(n-1) + t(n-2) + t(n-3) + t(n-4))
    
# for i in range(1, n+1):
#     print(t(i), end=" ")

#Q.6
# n = str(input())
# res = 0
# for i in n:
#     if int(i)%2 != 0:
#         res = res + 1
#     else:
#         pass
# print(res)

#Q.7
# s = str(input())
# spaces = 0
# UC = 0
# LC = 0
# for i in s:
#     if i == " ":
#         spaces = spaces + 1
#     elif i.isupper() == True:
#         UC = UC + 1
#     else:
#         LC = LC + 1

# print("Words: ", spaces + 1)
# print("Spaces: ", spaces)
# print("Uppercase: ", UC)
# print("Lowercase: ", LC)

#Q.8
# s = str(input())
# s1 = s[::-1]

# if s == s1:
#     print("palindrome")
# else:
#     print("not a palindrome")


#Lab-3
#Q1.
# Newton Raphson Method:
# Let x0 be the approximate root of f(x) = 0 and let
# x1 = x0 + h be the correct root. Then f(x1) = 0 => f(x0 + h) = 0
# By Expanding the above equation using Taylor's Theorem, we get:
# f(x0) + hf'(x0) + ......... = 0 or h = -f(x0)/f'(x0)
# Therefore, x1 = x0 - f(x0)/f'(x0)
# Now, x1 is the better approximation than x0
# Generalising it, we get:
# x     =    x   -  f(x ) / f'(x )
#  n+1        n        n        n

# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# e = int(input())
# th = float(input())
# root = int(input())


# def Root_determiner(a, b, c, d, e, root, th):
#     p = lambda a, b, c, d, e, x: a*(x**4) + b*(x**3) + c*(x**2) + d*x + e
#     p1 = lambda a, b, c, d, x : 4*a*(x**3) + 3*b*(x**2) + 2*c*x + d
#     x = root
#     r = p(a, b, c, d, e, root)/p1(a, b, c, d, root)
#     while abs(r) >= th:
#         r = p(a, b, c, d, e, x)/p1(a, b, c, d, x)
#         x = x - r
        
#     return x

# print(Root_determiner(a, b, c, d, e, root, th))


#Q2.
# s1 = str(input())
# s2 = str(input())

# for i in s1:
#     val = 0
#     for j in s2:
#         if i != j:
#             val += 1
#         else:
#             pass
#     if val == len(s2):
#         print(i,end="")
#     else:
#         pass


# for i in s2:
#     val = 0
#     for j in s1:
#         if i != j:
#             val += 1
#         else:
#             pass
#     if val == len(s1):
#         print(i,end="")
#     else:
#         pass

#Q3.
# n = str(input())

# m = 0
# for i in n:
#     m = m + int(i)**len(n)

# if m == int(n):
#     print("Armstrong")
# else:
#     print("Not Armstrong")

#Q4.
# n = int(input())
# m = int(input())

# if n%m == 0:
#     print(m)
# else:
#     r = n%m
#     while r != 0:
#         n = m
#         m = r
#         r = n%m
#     print(m)

#Q5.

# n = int(input())
# m = int(input())

# def gcd(n, m):
#     if n%m == 0:
#         return m
#     else:
#         r = n%m
#         while r != 0:
#             n = m
#             m = r
#             r = n%m
#         return m

# c = gcd(n, m)

# val1 = n//c
# val2 = m//c

# d = val1*val2

# print(d*c)


#Q6.
# n = int(input())

# l = []

# i = 1
# while i < n:
#     if n%i == 0:
#         l.append(i)
#         i = i + 1
#     else:
#         i = i + 1
# sum = 0
# for i in range(len(l)):
#     sum = sum + l[i]

# if sum == n:
#     print("Perfect")
# else:
#     print("Not Perfect")


#Q7.
# s = str(input())
# # "val = len(s) - 2"
# def f(s, val):
#     if len(s) == 2:
#         return int(s[1])
#     else:
#         res = int(s[1]) * (10**(val))
#         s1 = s[:1] + s[2:]
#         return res + f(s1, val-1)
    
# if s[0] == "+":
#     ans = f(s, len(s) - 2)
# else:
#     ans = -f(s, len(s) - 2)
    
# print(ans)
   
#Q8.

# n = int(input())

# def odd_digit_count(n, ind = 0, count = 0):
#     if ind == len(str(n)) - 1:
#         return count
#     elif int((str(n)[ind]))%2 != 0:
#         count = count + 1
#         ind = ind + 1
#         return odd_digit_count(n, ind, count)
#     else:
#         ind = ind + 1
#         return odd_digit_count(n, ind, count)
    

# print(odd_digit_count(n))

#Q9.
# a = int(input())
# b = int(input())
# c = int(input())
# d = int(input())
# delta = float(input())
# x1 = float(input())
# x2 = float(input())


# def f(a, b, c, d, x):
#     return a**(x**b) + c*(1 + x**d)**(1/d)

# x = x1
# area = 0
# while x <= x2:
#     area = area + f(a, b, c, d, x) * delta
#     x = x + delta

# print(area)











        

