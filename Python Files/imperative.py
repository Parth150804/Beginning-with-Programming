"""
We now start the imperative computation model!

-- Start with data records
-- tuples (pairs, triples, etc.), lists, dict
Tuples: 
-- are heterogeneous containers
-- Are immutable in nature; i.e. once the data is stored, it cannot be changed
-- Tuples are ordered;
-- Indexes are used to traverse a tuple
-- In many ways they are similar to lists; the only difference is that
they are immutable and are faster to access since the structure is fixed
at programming time.
"""

## Rational Numbers:
#constructor
"""
>>> (1,2)
(1, 2)
>>> a = (1,2)
>>> type(a)
<class 'tuple'>
>>> a = (1, "1")
>>> type(a)
<class 'tuple'>
>>> x,y = (1, a)
>>> x
1
>>> y
(1, '1')
"""

def rational(n,d):
    return (n,d)

#destructors
def numer(x):
    n, d = x
    return n

def denom(x):
    n, d = x
    return d

def gcd(a,b):
    if a == 0 or b == 0 or a == b:
        return a
    elif a > b:
        return gcd(a-b, b)
    else:
        return gcd(a, b-a)

def simplify_rational(x):
    n, d = x
    g = gcd(n, d)
    return (n//g, d//g)

# lists in Python
# a dynamically sized array in python;
# need not be homogeneous
#List items are enclosed in square brackets, like this [item1, item2, item3].
#Lists are ordered – i.e. the items in the list appear in a specific order. This enables us to use an index to access to any item.
#Lists are mutable, which means you can add or remove items after a list's creation.
#List elements do not need to be unique. Item duplication is possible, as each element has its own distinct place and can be accessed separately through the index.
#Elements can be of different data types: you can combine strings, integers, and objects in the same list.

# Checking if a list is empty -- from scratch
def checkEmpty1(lst):
    if not len(lst):
        return True
    else:
        return False

def checkEmpty2(lst):
    if lst == []:
        return True
    else:
        return False

def lenL(lst):
    if (lst == []):
        return 0
    else:
        hd,tl = lst[0], lst[1:]
        return 1 + lenL(tl)
    
#print(lenL([1,2,3,4,5,6]))    
    
def appendL1(lst, a):
    return lst.append(a)
# one could use insert
# find the length: l = len(lst)
# lst.insert(l, <val>)
def appendL2(lst, a):
    if lst == []:
        return [a]
    else:
        tl = lst[1:]
        return [lst[0]] + appendL2(tl, a)

        
#print(appendL2([1,2,3,4,5,6], 'a'))    
def reverseL1(lst):
    return lst.reverse()

def reverseL2(lst):
    if lst == []:
        return []
    else:
        hd, tl = lst[0], lst[1:]
        return reverseL2(tl) + [hd]

#print(reverseL2([1,2,3,4,5,6]))

# tail recursive reverse
""" 
Proof of correctness: 
Use the invariant
at ith step Length(L) = n-i
length of M = i
reverse(M)+L = L_original
"""
def reverseL3(lst):
    def revTL(L,M):
        if (L == []):
            return M
        else:
            hd, tl = L[0], L[1:]
            return revTL(tl, [hd]+M)
    return revTL(lst, [])

#print(reverseL3([1,2,3,4,5,6]))
