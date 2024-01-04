#functions as return values

def add2(x, y): 
    return x + y
def add3(x, y, z):
    return x + y + z

def general_add(argCnt):
    if argCnt == 3:
        return add3
    elif argCnt == 2:
        return add2
    else:
        pass

res = general_add(3)
print(res)
print(res(2, 5, 3))

#Lambda expressions: Anonymous functions

def myfnc(n):
    return lambda x: x**n    # return value of myfnc is a function which raises power n
                            # on the number which is given as an input to it.
myexp = myfnc(3)
print("10^3 is: ", myexp(10))
    
#Python closures
def addc (y):
    def add(x):
        return x + y
    return add

z = addc(3)

# Functions passed as arguments
def say_hello(name):
    return "Hello " + name

def ask_question():
    return "Do you know how to shuffle?"

def converse_with_subodh(f):
    return f("subodh") + ". "+ ask_question()

print(converse_with_subodh(say_hello))

"""
Through a closure, i have returned
a function along with its environment
Environment how? Note that while 
function add is returned, the variable
y is also alive with a value 3.

Use of closures: 
-- Binding data to a function w/o passing it
as a results even if the enclosing scope or fuction
is not alive, a closure function object remembers
those values. Classic example of data hiding.
-- Avoid the use of unnecessary global scopes. 
Sometimes you might have variables in the global 
scope that are not used by more than one function. 
"""
def add5():
    f = 5
    def add(x): 
        return x + f
    return add

#print(add5()(3))

# Decorators:

def decorator(fnc):
    def wrapper(x, y):
        print("I am just before the func call")
        fnc(x, y)
        print("I am just after the func call")
    return wrapper

def simpleAdd(x, y):
    print("The sum of ", x, "and", y, "is", x+y)

#simpleAdd = decorator(simpleAdd)

#simpleAdd(3,2)

################################################

## Motivation for Higher order
def sumInt(a,b):
    if a > b:
        return 0
    else:
        return a + sumInt(a+1, b)

def sumCubes(a,b):
    if a > b:
        return 0
    else:
        a*a*a + sumCubes(a+1, b)

# Sequence: 1/(1*3) + 1/(5*7) + 1/(9*11) ...
# Converges to Pi/8
# Inductive definition: 1/(i*(i+2)) + next term starts at (i+4)
def sumSeq(a,b):
    if a > b:
        return 0
    else:
        return 1.0/(a*(a+2)) + sumSeq(a+4, b)
    
"""
Observations: 
1. The first term in the IH is a function of lower bound: f(a). 
2. In the second term of our IH, the lower bound gets incremented 
by yet another function, say, g(a) or succ(a). 
3. There is a "+" operator whose identity is playing the role in the
termination argument
"""
        

# Higher order sum
# Sigma_{i = l} ^{u} f(i)

def sumho(l, u, f, succ):
    if l > u:
        return 0 # 0 is the identity for the + operator
    else:
        return f(l) + sumho(succ(l), u, f, succ)

def sum(a,b):
    return sumho(a,b, lambda x: x, lambda y: y+1)

print(sum(1,10))

def sum_squares(a,b):
    return sumho(a,b, lambda x: x*x, lambda y: y+1)

print(sum_squares(1,10))

def sumSeq2(a,b):
    return sumho(a,b, lambda x:  1/(x*(x+2)), lambda y:y+4)

#print(sumSeq(3,10)== sumSeq2(3,10))

"""
Let us now generalize the higherOrder function even more!
Look the series \Pi_{a,b} f(i) are no different except the
operator + is replaced by a *

Thus, we can generalize our sumho to a general accumulator
"""


import operator as oper

def Accumulator(l,u,f,succ, op, iden):
    if l > u:
        return iden
    else:
        return op(f(l), Accumulator(succ(l), u, f, succ, op, iden))

def sumSeq3(a,b):
    return Accumulator(a,b,lambda x: 1/(x*(x+2)), lambda y:y+4, oper.add, 0)
    
print(sumSeq(3,10)== sumSeq3(3,10))

def fact1(n):
    if n <=1:
        return 1
    else:
        return n*fact1(n-1)


def factho (n):
    return Accumulator(1,n,lambda x: x, lambda y:y+1, oper.mul, 1)

print(fact1(100) == factho(100))

"""

Note that Accumulator as defined above is general for any operator
X so long as the following properties hold for X: 
1. Associative: a X (b X c) = (a X b) X c
2. has Identity element: a X e = a = e X a

Some examples of operators X are: 
- +, 0 on integers and reals
- concatenation and the empty string on strings 
- and, true on booleans
- or, false on booleans
- +, 0 on vectors and matrices
- ∗, 1 on vectors and matrices

"""

    
