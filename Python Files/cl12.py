"""
Quiz 2
compare(oper, x, y):
use the above function as an argument to the
filter function on a given list with oper = lt

import operator as op

filter(compare(op.lt, ....))
"""

# Merge Sort   (Avg. T(n) = O(n log n) and Space Complexity = O(n))

"""
Two sorted sublists L1, L2 and return a sorted L1+L2 
"""
lst = [6, 5, 2, 4, 1, 3]

#Recursive version

def merge(l1, l2):                   #It takes two 'sorted lists' and concatenates them
    if l1 == []:                     #such that we get an overall sorted list.
        return l2
    elif l2 == []:
        return l1
    else:
        hd1, tl1 = l1[0], l1[1:]
        hd2, tl2 = l2[0], l2[1:]
        if hd1 <= hd2:
            return [hd1] + merge(tl1, l2)
        else:
            return [hd2] + merge(l1, tl2)

#print(merge([1, 3, 5], [2, 4, 6]))
"""
preconditions: C1 ---> is a relation on 
the input vars of f
f(x,y, ...)
postcondition: C2 -- > a relation 
on the output of f
I.S: 
 PMI v3:
"""

## Output of split---> a pair of sublists
"""
lst = [6,5,2,4,1,3]
hd = 6, nxt = 5, tl = [2,4,1,3]
(p1, p2) = split ([2,4,1,3])
          --> hd = 2, nxt = 4, tl = [1,3]
              (p1, p2) = split([1,3])
                    ---> hd = 1, nxt = 3, tl = []
                         split([])  <---- ([], [])
                         <--- ([1], [3])
               <---- ([2,1],[4,3])
<----([6,2,1], [5,4,3])
"""
def split(lst):             # returns two sublists
    if lst == []:
        return [], []
    elif len(lst) == 1:
        return lst, []
    else:
        hd, nxt, tl = lst[0], lst[1], lst[2:]
        p1, p2 = split(tl)
        return [hd] + p1, [nxt] + p2
# split(tl) will give another two lists which are named as p1 and p2 above
#print(split([1, 5, 4, 3, 2, 6, 7]))

def mSort(lst):          # Two functions are used: split and merge
    if lst == []:       # and then mSort is used recursively
        return []
    elif len(lst) == 1:
        return lst
    else:
        l1, l2 = split(lst)
        return merge(mSort(l1), mSort(l2))  # Ultimately this merge will get two singleton lists
                                            # (which are always sorted) so its precondition also gets fulfilled.
"""
Quicksort: works  by identifying a "pivot", say x,  and          
partitioning lst into two sublists such 
that 
    [all x' < x, x, all x' > x]
partition function (lst, x): (p1, p2)
"""

print(mSort([1, 5, 4, 3, 2, 6, 7]))