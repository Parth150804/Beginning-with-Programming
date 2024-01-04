def checkEmpty2(lst):
    if lst == []:
        return True
    else:
        return False

def lenL(lst):
    if lst == []:
        return 0
    else:
        hd, tl = lst[0], lst[1:]
        return 1 + lenL(tl)

#print(lenL([1,2,3,4,"a", True]))

def appendL(lst, a):
    if lst == []:
        return [a]
    else:
        tl = lst[1:]
        return [lst[0]] + appendL(tl, a)

l = [1,1,3]
#print(l.append("a"))
#print (l.append("a") == appendL(l, "a"))


## reverse of a list:
def reverseL1(lst):
    lst.reverse()
    return lst

#print(reverseL1(l))

def revL2(lst):
    if lst == []:
        return []
    else:
        hd, tl = lst[0], lst[1:]
        return revL2(tl) + [hd]

#print (revL2([2,4,6,8,10]))

def revL3(lst):
    def revTL(L, M):
        if(L == []):
            return M
        else:
            hd, tl = L[0], L[1:]
            return revTL((tl), [hd]+M)
    return revTL(lst, [])
"""
- at step i, Length(L) = n-i and 
the length(M) = i
- revL2(M) + L = lst 
"""

# Maps, filter and reduce 

# Map function: is a function F that
# is appplied to every element  of the
# storage structure
# lst = [a, b, c, d]
# map(f, lst) = [f(a), f(b), f(c), f(d)]

# from functools import reduce
# NOTE: function passed into reduce must be a two argument taking function.
# reduce(f, lst) = f(f(f(a, b), c), d)  <---------- in first step, it takes first two values, then their 
#                                                   result and following value and so on.
l = [5, 10, 15]
cubeIt = map(lambda x: x*x*x, l)
#print(list(cubeIt))

def mapL(f, lst):
    if lst ==[]:
        return []
    else:
        hd, tl = lst[0], lst[1:]
        return [f(hd)] + mapL(f, tl)

#print(mapL(lambda x: x*x*x, l))

# Filters
def myPred(x):
    vowel = ['a', 'e', 'i', 'o', 'u']
    if x in vowel:
        return True
    else:
        return False

def filterL(f, lst):
    if lst == []:
        return []
    else:
        hd, tl = lst[0], lst[1:]
        if f(hd) == True:
            return [hd] + filterL(f, tl)
        else:
            return filterL(f, tl)

#print(filterL(myPred, ['a','b','c','d', 'e']))
    
filterIt = filter(myPred, ['a','b','c','d', 'e'])     # whichever element of list when passed into func 'myPred' returns True will be mapped by filter.
#print(list(filterIt))



## READING ASSIGNMENT: read the functionality                                                                       
## of reduce() and implement it recursively                                                                         
## and check your results equivalence with                                                                          
## the python's native reduce()

# QUIZ 1:                                                                                                           

"""                                                                                                                 
Design a recursive function to                                                                                      
find the maximum of a given list.                                                                                   
Show its timing analysis.                                                                                           
"""

def max_lst(lst):
    if len(lst) == 0:
        return None
    elif len(lst) == 1:
        return lst[0]
    else:
        hd, tl = lst[0], lst[1:]
        if hd >= max_lst(tl):
            return hd
        else:
            return max_lst(tl)
'''
T(n) = 1 + T(n-1)
T(1) = T(0) = 1
So, Time complexity will be O(n)
'''

