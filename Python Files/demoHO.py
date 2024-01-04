import sys

def add2(x, y):
    return x + y

def add3(x, y, z):
    return x+y+z

def generalAdd(argCnt): 
    if argCnt == 2:
        return add2
    elif argCnt == 3:
        return add3
    else:
        sys.exit("Not supported")
"""
res = generalAdd(3)        
print(res)
print(res(2,3,5))
print(add3)
"""
# Anonymous functions -- Lambda expressions 
def myFnc(n):
    return lambda x: x**n
# myFnc: N ->(N->N)
res1 = myFnc(3)
#print(res1)
#print(" the output of 10^3 is:", res1(10))

"""
Python Closures
allow me to return a function as a value
as well as the environment under which 
it executes.

Uses:
 -- Bind data to a function w/o passing
it as a result even if the enclosing scope
is not alive anymore. 
-- Avoid the use of unnecessary global scopes
"""


# Decorators: redefine the functionality
# of a function w/o changing its code. 
def decorator(fnc):
    def wrapper(x,y):
        print(" I am here before the call")
        fnc(x,y)
        print(" I am here after the call")
    return wrapper

def simpleAdd(x,y):
    print("The sum of", x, "and", y, "is", x +y)

simpleAdd = decorator(simpleAdd)

#simpleAdd(2,3)
"""
####################
Sum of integers(a, b)
= Sigma_{i = a}^{i = b} F(i)
s.t. F(i) = i

Sum of square of integers = Sigma_{i = a}^{i = b} F(i)
s.t. F(i) = i*i
"""

def summationHOFnc(l, u, succ, f):
    if l > u:
        return 0
    else:
        f(l) + summationHOFnc(succ(l), u, succ, f)

