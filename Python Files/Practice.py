"""
import math
def dist(a, b):
    return math.sqrt((a[0] - b[0])**2 - (a[1] - b[1])**2)

def is_point_inside_polygon(polygon, n, z, Q):

    # Assuming polygon is given in terms of its coordinates (as a list of tuples).
    # n --> no. of sides of polygon
    # z --> Given point
    # Q --> point at centre of polygon

    if math.sqrt(3)*dist(Q, polygon[0])/2 < dist(Q, z):
        return "OUTSIDE"
    elif math.sqrt(3)*dist(Q, polygon[0])/2 == dist(Q, z):
        return "ON THE POLYGON"
    else:
        return "INSIDE"

def f():
    l = []
    a = int(input())
    for i in range(a):
        lst = []       
        p = int(input())
        q = str(input())
        for j in range(0, len(q), 2):
            lst.append(q[j])
        sum = 0
        for k in range(len(lst)):
            sum = sum + int(lst[k])
        if sum%int(lst[len(lst) - 1]) == 0:
            l.append(1)
        else:
            l.append(2)
    for m in l:
        print(m)

#f()


def g():
    lst = []
    a = int(input())
    for i in range(a):
        p = int(input())
        lst.append((p-3)//2)
    for m in lst:
        print(m)

#g()
n = int(input("Enter the number of unkowns: "))
print("Enter the Augmented Matrix")
M = []
for i in range(n):
    row = []
    for j in range(n+1):
        ele = float(input("Enter A["+str(i)+"]["+str(j)+"]: "))
        row.append(ele)
    M.append(row)

for i in range(n):
    if M[i][i] != 0:
        for j in range(i+1, n):
            factor = M[j][i]/M[i][i]
            for k in range(n+1):
                M[j][k] -= factor*M[i][k]

class Set:
    def __init__(self):
        self.arg = set()

    def insert(self, x):
        self.arg.add(x)

    def empty(self):
        if len(self.arg) == 0:
            return True
        else:
            return False

    def belongs(self, a):
        if a in self.arg:
            return True
        else:
            return False

    def intersection(self, other_set):
        s = self.arg.intersection(other_set)
        print(s)

    def union(self, other_set):
        s = set()
        for i in str(self.arg):
            s.add(i)
        for j in str(other_set):
            s.add(j)
        print(s)

    def __repr__(self):
        return repr(self.arg)

S1 = Set()
S1.insert(3)
S1.insert(9)
S1.insert(2)
S1.insert(1)

S2 = Set()
S2.insert(1)
S2.insert(2)
S2.insert(6)
S2.insert(7)

print(S1.intersection(S2))

def transpose(A, n):
    for i in range(n):
        j = i + 1
        while j < n:
            A[i][j], A[j][i] = A[j][i], A[i][j]
            j = j + 1
    return A

M = [[1, 2, 3, 4], [5, 6, 7, 8], [9, 10, 11, 12], [13, 14, 15, 16]]

#print(transpose(M, 4))

class PrefixExpressionEvaluator:
    def __init__(self, expression):
        self.expression = expression.split()
        self.stack = []

    def evaluate(self):
        for token in reversed(self.expression):
            if token.isdigit():
                self.stack.append(int(token))
            else:
                operand1 = self.stack.pop()
                operand2 = self.stack.pop()
                if token == '+':
                    result = operand1 + operand2
                elif token == '-':
                    result = operand1 - operand2
                elif token == '*':
                    result = operand1 * operand2
                elif token == '/':
                    result = operand1 / operand2
                else:
                    raise ValueError(f"Invalid operator: {token}")
                self.stack.append(result)
        return self.stack.pop()


expression = "+ * 3 2 / 4 5"
evaluator = PrefixExpressionEvaluator(expression)
result = evaluator.evaluate()
#print(result)
"""

# def maxArea(lst):
#     n = len(lst)
#     l = []
#     for i in range(0, n-1):
#         for j in range(i+1, n):
#             area = (j-i)*min(lst[i], lst[j])
#             l.append(area)
#     return max(l)

# #print(maxArea([1, 8, 6, 2, 5, 4, 8, 3, 7]))
# import sys
# def f(n):
#     if n == "":
#         sys.exit()
#     else:
#         k = int(n[0])
#         print(k, end="")
#         m = n[1:]
#         return f(m)

# f(n)

    
# def f(n):
#     count = 1
#     j = 0
#     r = 0
#     while count <= n:
#         for i in range(r+1, r+1+count):
#             print(i, end=" ")
#         print("")
#         r = r + count 
#         count = count + 1
#         j = j + 1

# n = int(input("Enter the number: "))
#f(n)

# def g(n):
#     i = n
#     while i > 0:
#         for j in range(i-1):
#             print("", end=" ")
#         for k in range(n):
#             print("*", end=" ")
#         print("")
#         i = i - 1

# n = str(input())
# l = n.split()
# val = int(l[0])*int(l[1])
# print(val//2)

# n = str(input())
# m = str(input())
# r = n.split()
# l = m.split()
# k = int(l[int(r[1])-1])
# i = 0
# count = 0
# while  i < len(l) and int(l[i]) >= k and int(l[i]) > 0:
#     count = count + 1
#     i = i + 1
# print(count)

# n = int(input())
# l = []
# for i in range(n):
#     m = str(input())
#     l.append(m)

# val1 = 0 
# val2 = 0
# for j in l:
#     if j == "++X" or j == "X++":
#         val1 = val1 + 1
#     else:
#         val2 = val2 + 1
# print(val1 - val2)

# l = []
# for i in range(5):
#     n = str(input())
#     m = n.split()
#     l.append(m)
# val = None
# r = None
# for j in l:
#     bool = True in (ele != "0" for ele in j)
#     if bool == True:
#         val = l.index(j)
#         r = j
#     else:
#         pass
# res1 = abs(2-val)
# s = r.index('1')
# res2 = abs(2-s)
# print(res1+res2)

# m = str(input())
# n = str(input())
# m = m.lower()
# n = n.lower()
# val1 = 0
# val2 = 0
# for i, j in zip(m, n):
#     if val1 == val2:
#         val1 = val1 + ord(i) - 96
#         val2 = val2 + ord(j) - 96
#     else:
#         break
# if val1 > val2:
#     print(1)
# elif val1 < val2:
#     print(-1)
# else:
#     print(0)

# n = str(input())
# l = n.split()
# ans = int(l[0])*int(l[1])
# if int(l[0]) == 1 or int(l[1]) == 1:
#     print("Akshat")
# else:
#     if ans%2 == 0:
#         if (int(l[0])%2 == 0 and int(l[1])%2 != 0 and int(l[0])>int(l[1])) or (int(l[1])%2 == 0 and int(l[0])%2 != 0 and int(l[1])>int(l[0])):
#             print("Akshat")
#         else:
#             print("Malvika")
#     else:
#         print("Akshat")

# n = int(input())
# para = []
# list = []

# for i in range(2*n):
#     a = str(input())
#     if i%2 != 0:
#         l1 = a.split()
#         list.append(l1)
#     else:
#         l2 = a.split()
#         para.append(l2)

# def f(p1, p2):
#     count = 0
#     for i in range(len(p2)-1):
#         for j in range(i+1, len(p2)):
#             if int(p2[i]) + int(p2[j]) >= int(p1[1]) and int(p2[i]) + int(p2[j]) <= int(p1[2]):
#                 count = count + 1
#             else:
#                 pass
#     return count

# for k in range(n):
#     print(f(para[k], list[k]))


# n = int(input())
# if n >= 0 or n%10 == n:
#     print(n)
# else:
#     if n%100 == n:
#         a = int(str(n)[:-1])
#         b = str(n)[-1]
#         if a > b:
#             print(a)
#         else:
#             print(b)
#     else:
#         val1 = int(str(n)[:-1])
#         val2 = int(str(n)[:-2] + str(n)[-1])
#         if val1 > val2:
#             print(val1)
#         else:
#             print(val2)

# s = "abcd"
# print(s[:-2]+s[3:])

# n = int(input())
# list = []
# for i in range(n):
#     m = int(input())
#     l = str(input())
#     l1 = l.split()
#     list.append(l1)

# def f(lst):
#     lst = list(map(int, lst))
#     val1 = max(lst)
#     val2 = None
#     for i in range(val1):
#         if i in lst:
#             val2 = i
#             break
#         else:
#             pass

# def reverse(x):
#         x = str(x)[::-1] 
#         if x[len(x)-1] == "-":
#             val = 0
#             for i in range(2, len(x)+1):
#                 val = val + int(x[-i])*(10**(i-2))
#             val = "-" + str(val)
#             return int(val)
#         else:
#             ans = 0
#             for j in range(1, len(x)+1):
#                 ans = ans + int(x[-j])*(10**(j-1))
#             return ans
        
# print(reverse(123))

# n = int(input())
# lst = []
# for i in range(n):
#     m = str(input())
#     lst.append(m)

# def f(x):
#     l = [str(i) for i in str(x)]
#     a = all(ele == x[0] for ele in l)
#     if a == True:
#         return -1
#     else:
#         for k in l:
#             count = 0
#             for j in l:
#                 if j == k:
#                     count = count + 1
#                 else:
#                     pass
#             if count == len(l) - 1:
#                 return len(l) + 2
#             else:
#                 continue
#         return len(l)

# for g in lst:
#     print(f(g))

# n = str(input())
# lst = []
# for i in range(0, len(n), 2):
#     lst.append(n[i])
# lst = list(map(int, lst))
# lst.sort()
# for j in range(len(lst)):
#     if j != len(lst)-1:
#         print(str(lst[j]), end="+")
#     else:
#         print(str(lst[j]))

# n = str(input())

# def f(n):
#     val1 = 0
#     val2 = 0
#     for i in n:
#         if val1 >= 7 or val2 >= 7:
#             return "YES"
#         elif i == "0" and val2 < 7 and val1 < 7:
#             val2 = val2 + 1
#             val1 = 0
#         elif i == "1" and val1 < 7 and val2 < 7:
#             val1 = val1 + 1
#             val2 = 0
#         else:
#             return "YES"
#     if val1 >= 7 or val2 >= 7:
#         return "YES"
#     else:
#         return "NO"

# print(f(n))


# n = str(input())
# l = n.split()

# a = int(l[0])
# b = int(l[1])
# c = int(l[2])

# i = 0
# while i*(c**2) < a*b:
#     i = i + 1
# if i%2 == 0 or i == 1:
#     print(i)
# else:
#     print(i+1)

# lst = []
# for i in range(3):
#     n = str(input())
#     lst.append(n)

# def f(lst):
#     if len(lst[2]) != (len(lst[1]) + len(lst[0])):
#         return "NO"
#     else:
#         l1 = []
#         l2 = []
#         a = lst[0] + lst[1]
#         b = lst[2]
#         for i in a:
#             l1.append(i)
#         for j in b:
#             l2.append(j)
#         l1.sort()
#         l2.sort()
#         for k in range(len(l1)):
#             if l1[k] == l2[k]:
#                 pass
#             else:
#                 return "NO"
#         return "YES"

# print(f(lst))

# n = str(input())
# lst = n.split()
# l2 = []
# l3 = []
# l5 = []
# l6 = []
# for i in range(int(lst[0])):
#     l2.append("2")
# for j in range(int(lst[1])):
#     l3.append("3")
# for k in range(int(lst[2])):
#     l5.append("5")
# for l in range(int(lst[3])):
#     l6.append("6")

# def f(l2, l3, l5, l6):
#     if len(l2) == 0:
#         return 0
#     elif len(l3) == 0:
#         sum = 0
#         if len(l5) == 0 or len(l6) == 0:
#             return 0
#         else:
#             del l2[0]
#             del l5[0]
#             del l6[0]
#             sum = 256 + f(l2, l3, l5, l6)
#             return sum
#     elif len(l5) == 0 or len(l6) == 0:
#         del l2[0]
#         del l3[0]
#         sum = 32 + f(l2, l3, l5, l6)
#         return sum
#     else:
#         del l2[0]
#         del l5[0]
#         del l6[0]
#         sum = 256 + f(l2, l3, l5, l6)
#         return sum

# print(f(l2, l3, l5, l6))

# if len(l2) == 0:
#     print(0)
# elif len(l3) == 0:
#     sum = 0
#     if len(l5) == 0 or len(l6) == 0:
#         print(0)
#     else:
#         val = min(len(l2), len(l5), len(l6))


# n = str(input())    
# count = 0
# for i in n:
#     if i == "4" or i == "7":
#         count = count + 1
#     else:
#         pass

# count = str(count)
# if "4" in count:
#     print("YES")
# elif "7" in count:
#     print("YES")
# else:
#     print("NO")

# m = int(input())
# n = str(input())

# val1 = 0
# val2 = 0
# for i in n:
#     if i == "A":
#         val1 = val1 + 1
#     else:
#         val2 = val2 + 1
# if val1 > val2:
#     print("Anton")
# elif val2 > val1:
#     print("Danik")
# else:
#     print("Friendship")

# m = int(input())
# l = []
# for i in range(m):
#     n = str(input())
#     l1 = n.split()
#     l.append(l1)
# count = 0
# for i in range(len(l)):
#     if int(l[i][1]) - int(l[i][0]) >= 2:
#         count = count + 1
#     else:
#         pass
# print(count)

# s1 = str(input())
# s2 = str(input())

# s3 = s1[::-1]

# if s3 == s2:
#     print("YES")
# else:
#     print("NO")

# n = int(input())
# m = str(input())
# l = m.split()
# lst = list(map(int, l))
# lst.sort()

# def f(lst):
#     if len(lst) == 1:
#         return 1
#     else:
#         i = len(lst) - 1
#         j = len(lst) - 1
#         while i >= 0:
#             if sum(lst[i:j+1]) > sum(lst[0:i]):
#                 return j - i + 1
#             else:
#                 i = i - 1

# print(f(lst))
   

# n = int(input())
# m = str(input())

# l = m.split()
# lst = list(map(int, l))

# h = min([i for i, v in enumerate(lst) if v == max(lst)])
# s = max([i for i, v in enumerate(lst) if v == min(lst)])

# if h < s:
#     print(h + len(lst) - 1 - s)

# n = int(input())
# l = []
# for i in range(n):
#     m = str(input())
#     lst = m.split()
#     l.append(lst)

# def f(l):
#     l1 = []
#     val1 = 0
#     val2 = 0
#     for j in l:
#         val1 = val2
#         val2 = val2 + int(j[1]) - int(j[0])
#         if val2 < val1:
#             l1.append(val1)
#         else:
#             pass
#     l1.append(val2)
#     return max(l1)

# print(f(l))

# n = str(input())
# s = set()
# for i in n:
#     s.add(i)
# res = len(s)
# if res%2 == 0:
#     print("CHAT WITH HER!")
# else:
#     print("IGNORE HIM!")

# n = int(input())
# lst = []
# for i in range(n):
#     m = str(input())
#     lst.append(m)
# res = 1
# val1 = 0
# val2 = 0
# for j in lst:
#     if j == "10" and val1 == 0:
#         val1 = val1 + 1
#     elif j == "01" and val2 == 0:
#         val2 = val2 + 1
#     elif j == "10" and val1 != 0:
#         res = res + 1
#         val1 = 0
#     elif j == "01" and val2 != 0:
#         res = res + 1
#         val2 = 0
#     else:
#         pass

# print(res)

# n = int(input())
# m = str(input())
# s = set()

# m = m.lower()
# for i in m:
#     s.add(i)
    
# l = len(s)

# if l < 26:
#     print("NO")
# else:
#     print("YES")

# n = str(input())
# s = set()
# for i in range(1, len(n)-1, 3):
#     s.add(n[i])

# print(len(s))


# n = str(input())
# l = n.split()

# if int(l[0])%2 == 0:
#     if int(l[1]) > int(l[0])//2:
#         val1 = int(l[1]) - int(l[0])//2
#         print(2*val1)
#     else:
#         val2 = int(l[1])
#         print(2*val2 - 1)
# else:
#     if int(l[1]) > (int(l[0])+1)//2:
#         val3 = int(l[1]) - (int(l[0])+1)//2
#         print(2*val3)
#     else:
#         val4 = int(l[1])
#         print(2*val4 - 1)

# n = int(input())
# lst = []
# for i in range(n):
#     m = str(input())
#     l = m.split()
#     lst.append(l)

# def f(l1):
#     if l1[0] == l[1]:
#         return l1[0]
#     else:
#         val = int(l[1]) - int(l[0])
#         if val > 9:
#             val = val - 9
            
# n = int(input())
# lst = []
# for i in range(n):
#     m = int(input())
#     k = str(input())
#     l = list(map(int, k.split()))
#     lst.append(l)

# def f(l1):
#     l1.sort()
#     for i in l1:
#         if l1[i] == i+1:
#             return "YES"
#         else:
#             pass
#     return "NO"

# for j in lst:
#     print(f(j))

# n = int(input())
# l = []
# for i in range(n):
#     m = str(input())
#     l.append(list(map(int, m.split())))


# def f(lst):
#     a = lst[0]
#     b = lst[1]
#     if a == b:
#         return (a+b)//4
#     elif a > b:
#         res1 = (a+b)//4
#         res2 = b
#         if res1 > res2:
#             return res2
#         else:
#             return res1
#     else:
#         res1 = (a+b)//4
#         res2 = a
#         if res1 > res2:
#             return res2
#         else:
#             return res1

# for i in l:
#     print(f(i))

# n = int(input())
# l = []
# for i in range(n):
#     lst = []
#     i1 = str(input())
#     i2 = str(input())
#     H = int(i1.split()[1])
#     l1 = list(map(int, i2.split()))
#     l1.sort()
#     l.append(H)
#     l.append(l1)

# def f(x,y):
#     a = y[len(y)-1]
#     H = x
#     if H <= a:
#         return 1
#     else:
#         k = H-a
#         if k <= y[0]:
#             return 2
#         else:
#             ans = 1
#             while H > 0:
#                 a1 = y[len(y)-1]
#                 a2 = y[len(y)-2]
#                 H = H-a1
#                 ans = ans + 1
#                 a1, a2 = a2, a1
#             return ans
        
# for i in range(0, 2*n, 2):
#     print(f(l[i], l[i+1]))


# n = int(input())
# lst = []
# for i in range(n):
#     q = int(input())
#     x = str(input())
#     l = list(map(int, x.split()))
#     lst.append(l)

# def beautiful_checker(l1):
#     l2 = sorted(l1)
#     if len(l1) == 0 or len(l1) == 1 or len(l1) == 2 or l1 == l2:
#         return True
#     else:
#         for j in range(len(l1)-1):
#             l3 = l1[j+1:] + l1[0:j+1]
#             if l3 == l2:
#                 return True
#             else:
#                 pass
#         return False

# def g(lst):
#     l1 = []
#     s = ""
#     for i in lst:
#         l1 = l1 + [i]
#         if beautiful_checker(l1) == True:
#             s = s + "1"
#         else:
#             del l1[len(l1)-1]
#             s = s + "0"
#     return s

# for i in lst:
#     print(g(i))

# n = int(input()) 
# l = [] 
# for i in range(n):
#     m = int(input())
#     s = input(str())
#     l.append(s)

# def min_cost_of_arrays(s):
#     i = 0
#     j = len(s)-1
#     ans = 1
#     while i <= j:
#         if s[i] == s[j]:
#             if i != j:
#                 ans = ans + 1
#             else:
#                 ans = ans + 2
#             i = i + 1
#             j = j - 1
#         else:
#             ans = ans + 1
#     return ans + 1


# for j in l:
#     print(min_cost_of_arrays(j))

#n = int(input())
# l = []
# for i in range(n):
#     m = int(input())
#     l.append(m)

# for j in l:
#     if j == 4 or j == 2 or j == 3:
#         print("Bob")
#     else:
#         print("Alice")

# n = int(input())
# l = []
# for i in range(n):
#     m = int(input())
#     s = str(input())
#     l.append(s)

# def decrypter(s):
#     s1 = ""
#     n = len(s)
#     i = 0
#     j = 1
#     while i < n-1:
#         while j < n:
#             if s[i] == s[j]:
#                 s1 = s1 + s[i]
#                 i = j + 1
#                 j = j + 2
#             else:
#                 j = j + 1
#     return s1

# for k in l:
#     print(decrypter(k))

# nums = [5,7,7,8,8,10]
# nums.reverse()
# print(len(nums) - nums.index(8) - 1)
# def searchRange(nums, target):
#     l = []
#     if target in nums:
#         val1 = nums.index(target)
#         nums.reverse()
#         val2 = len(nums) - nums.index(target) - 1
#         l.append(val1)
#         l.append(val2)
#         return l
#     else:
#         l.append(-1)
#         l.append(-1)
#         return l

# n = int(input())
# s = str(input())
# ans = 0
# len = len(s)
# for i in range(n-1):
#     if s[i] == s[i + 1]:
#         ans = ans + 1
#     else:
#         pass

# print(ans)
            

# s = str(input())
# l = s.split()
# L = int(l[0])
# B = int(l[1])
# ans = 0

# while L <= B:
#     L = 3*L
#     B = 2*B
#     ans = ans + 1
# print(ans)

# def int_sqrt(n):            # T(n) = O(n)
#     l = 1
#     while l**2 <= n:
#         if (l + 1)**2 > n:
#             return l
#         else:
#             l += 1

# def integer_sqrt(n):        # T(n) = O(log n)
#     l = 1
#     while True:
#         if (l + 1)**2 > n and l**2 <= n:
#             return l
#         elif l**2 < n:
#             l = 2*l
#         else:
#             l = l//2 + 1

# def tail_rec_fac(n, p = 1):
#     if n == 0:
#         return 1
#     elif n == 1:
#         return p
#     else:
#         return tail_rec_fac(n - 1, p*n)

# arr = ["bl", "w", "bl", "br", "w"]

# def helper(ele, lst):
#     if lst == []:
#         return [ele]
#     else:
#         hd, tl = lst[0], lst[1:]
#         if ele == "w":
#             return [ele] + lst
#         elif ele == "bl":
#             if hd == "w":
#                 return [hd] + helper(ele, lst)
#             else:
#                 return [ele] + lst
#         else:
#             return [hd] + helper(ele, lst)

# def arrange(arr):
#     if arr == []:
#         return []
#     else:
#         hd, tl = arr[0], arr[1:]
#         return helper(hd, arrange(tl))   
      
# print(arrange(arr))

# class Stack:
#     def __init__(self):
#         self.stack = []
    
#     def push(self, a):
#         self.stack.append(a)

#     def pop(self):
#         self.stack.pop()

#     def __isEmpty__(self):
#         return True if len(self.stack) == 0 else False
    
#     def __len__(self):
#         return len(self.stack)
    
#     def top(self):
#         return self.stack[-1]
    
#     def __repr__(self):
#         return repr(self.stack)

    

# myStack = Stack()

# lst = [2, 3, 1, 7, 32, 0]

# for i in lst:
#     myStack.push(i)

# myStack.pop()
# myStack.pop()
# print(len(myStack))


# def lastocc(arr, n, target, ans = -1, p = 0):
#     if p == n - 1 and arr[p] != target:
#         return ans 
#     elif p == n - 1 and arr[p] == target:
#         return p
#     else:
#         if arr[p] == target:
#             return lastocc(arr, n, target, p, p + 1)
#         else:
#             return lastocc(arr, n, target, ans, p + 1)
        
# print(lastocc([1, 2, 3, 4, 2, 2], 6, 2))

# def towerofHanoi(no_of_disks, src, helper, dest):
#     if no_of_disks == 1:
#         print("Move from", src, "to", dest)
#     else:
#         towerofHanoi(no_of_disks - 1, src, dest, helper)

#         print("Move from", src, "to", dest)

#         towerofHanoi(no_of_disks - 1, helper, src, dest)


# towerofHanoi(3, "S", "H", "D")

## Proof of correctness:

## Basis: for n = 1, it is true as we can simply move the disk directly from src to dest tower.

## Induction Hypothesis: Assume it is true for some n >= 1.

## Induction step: So, if we have n+1 disks on src tower, we can move starting n disks from
## src to helper tower using dest tower as the algo. is true for 'n'. Now using basis step, we can
## simply move the remaining one disk from src to dest. Hence, the problem reduces to solving
## with helper as src tower with 'n' disks & src tower as helper tower to dest tower (here, dest tower will behave 
## normally as any disk can be placed over the largest disk). Using induction hypothesis it is true for every n+1.


# def removeDup(s):
#     if len(s) == 0:
#         return ""
#     else:
#         ch = s[0]
#         ros = removeDup(s[1:])
#         if ch in ros:
#             return ros
#         else:
#             return ch + ros
        
# print(removeDup("abbcddde"))

# def partily_sort(arr, n):
#     low = 0
#     high = n-1

#     while(low < n):
#         if (high < 0 or low > high):
#             low += 1
#             high = n-1
#         else:
#             if (arr[low]%2 == 0):
#                 if (arr[high]%2 == 0):
#                     if (arr[low] > arr[high]):
#                         arr[high], arr[low] = arr[low], arr[high]
#                         low += 1
#                         high = n-1
#                     else:
#                         high -= 1
#                 else:
#                     high -= 1
#             else:
#                 if (arr[high]%2 != 0):
#                     if (arr[low] > arr[high]):
#                         arr[high], arr[low] = arr[low], arr[high]
#                         high = n-1
#                     else:
#                         high -= 1
#                 else:
#                     high -= 1
#     return arr

# a = [11, 3, 4, 2, 12, 32, 0]
# print(partily_sort(a, 7))
        
class Employee:
    def __init__(self, val):
        self.id = val
        self.__password = 1234567

    def work(self):
        print("I am Employee ", self.id, " and I am working")

    def Login(self, number):
        if number == self.password:
            print("Login Successful")
        else:
            print("Unsuccessful")

class Developer(Employee):
    pass

class Manager(Employee):
    manager_id = 73254329

    def work(self):
        print("I am manager", self.manager_id, "and I am working")


    def Login(self, number):
        if number == self.__password:
            print("Login Successful")
        else:
            print("Unsuccessful")

    def change_password(self, old_password, new_password):
        self.__password = new_password
    
a = Manager(5)
a.Login(1234567)


    