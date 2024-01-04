# Lab Question Solution
def printStarTriangle(n):
    for i in range(1,n+1):
        for j in range(1, n+1-i):
            print(" ", end="")
        for k in range(0, 2*i-1):
            print("*", end="")
        print("")

#printStarTriangle(4)
        

# CLARIFICATION

lst = []

def appendToLst(l1):
    for e in l1:
        lst.append(e)
    return lst

#print(appendToLst(["sub", "svs"]))


# SORTING

## INSERTION SORT

"""
Timing Analysis: 
T(n) = T(n-1) + n 
T(n) \in O(n^2)  <----

I.S: in the else part --> 
hd is the smallest element 
insert(a, tl) via I.H. is indeed sorted
[hd] + sorted list  ---> a  sorted list

"""

def insert(a, lst):      #Assuming list is sorted in ascending order,
    if lst == []:        #this func will insert 'a' at its appropriate position
        return [a]
    else:
        hd, tl = lst[0], lst[1:]
        if a < hd:
            return [a] + lst
        else:
            return [hd] + insert(a, tl)       #Time complexity of this insert func is O(n)

# Recursive Insort (T(n) = O(n^2))

def inSort(lst):           #inductively applying insert at every
    if lst == []:          #element of the list and simultaneously
        return []           #insort at remaining list
    else: 
        hd, tl = lst[0], lst[1:]
        return insert(hd, inSort(tl))   #observe this return, it also gives us general expression of timing analysis


lst1 = [1, 7, 5, 6, 9, 3]
#print(inSort(lst1))

# Insort's Imperative version (Very important and good logic)

def inSortv2(lst):
    n = len(lst)
    
    for j in range(1, n):
        value = lst[j]
        i = j - 1
        # INV2: lst [i ... j] is sorted
        while i >= 0 and lst[i] > value:
            lst[i + 1] = lst[i]
            i = i - 1
        # INV2: for all k  \in [i,j]
            #   s.t. lst[k] >= value
        lst[i + 1] = value
    # INV1: lst[0 .... j-1] is sorted
    return lst

print(inSortv2(lst1))

def in_sort(lst):
    for i in range(1, len(lst)):
        j = 0
        while j < i:            # INV: lst[j:i] is sorted
            if lst[j] > lst[i]:
                lst[j], lst[i] = lst[i], lst[j]
                j = j + 1
            else:
                j = j + 1
    return lst

print(in_sort(lst1))