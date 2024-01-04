def swap(lst, i, j):
    temp = lst[i]
    lst[i] = lst[j]
    lst[j] = temp

import pdb

def partition(lst, x):
    i = 0
    j = len(lst) - 1
    #pdb.set_trace()
    while i < j and lst[i] < x:
        i = i + 1
    while i < j and lst[j] > x:
        j = j - 1
    #INV: i >=j \/ (i < j /\ lst[i] >=x /\ lst[j] <= x)
    while i < j:
        #INV: (i < j /\ lst[i] >=x /\ lst[j] <= x)
        swap(lst, i, j)
        #INV: (i < j /\ lst[i] < x /\ lst[j] >= x)
        i = i +1
        #j = j-1
        while lst[i] < x:
            i = i+1
        while lst[j] > x:
            j = j - 1
    return j

lst = [2,5,3,4,6,1]
print("The pivot index:", partition(lst,4))
print("Lst after partitioning", lst)

    
