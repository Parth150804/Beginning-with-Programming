def revIt(lst):
    if lst == []:
        return []
    else:
        l = 0
        u = len(lst)-1
        while l < u:
            temp = lst[l]
            lst[l] = lst[u]
            lst[u] = temp
            l = l+1
            u = u-1
    return lst

    #INV: lst[l:u] are unchanged /\ lst[0:l], lst[u, n] have swapped

#print(revIt([1,2,3,4,5,6]))
# Prob 6 in the exam is O( nlog log n)

def primes(n):
    lst = []
    for j in range(2, n+1):
        lst.append(True)

    i = 2
    while i*i <= n:
        k = i*i
        while k <= n:
            if k%i == 0:
                lst[k] = False
            k = k + i
        i = i + 1
    # INV: ?
    # Time complexity:?

def mergeIT(l1, l2):        # It is basically iterative version of merge (takes two sorted lists and
    if l1 == []:            # concatenates them such that output is an overall sorted list).
        return l2
    elif l2 == []:
        return l1
    else:
        res = []
        i = j = 0
        while True:
            if l1[i] < l2[j]:
                res.append(l1[i])
                i = i+1
            else:
                res.append(l2[j])
                j = j+1

            if i == len(l1) and j < len(l2):
                res = res + l2[j:]
                break
            if j == len(l2) and i < len(l1):
                res = res + l1[i:]
                break
    return res
        # INV: At every iteration, res will be a sorted list having all
        # elements of both l1[:i] and l2[:j]

## Quicksort   (Avg. T(n) = O(n log n) and Space complexity = O(1))

def partition(pivot, lst):     # this fnc returns two sublists one of which has elements
    if lst == []:              # less than pivot and other one has elements greater than or
        return ([], [])        # equal to pivot
    else:
        hd, tl = lst[0], lst[1:]
        (p1, p2) = partition(pivot, tl)
        if hd < pivot:
            return ([hd]+p1, p2)
        else:
            return (p1, [hd]+p2)

#print(partition(3, [4, 3, 2, 10, 12, 1]))

# Recursive Quick sort

def qSort(lst):
    if lst == []:
        return []
    elif len(lst) == 1:
        return lst
    else:
        hd, tl = lst[0], lst[1:]
        (p1, p2) = partition(hd, tl)
        return qSort(p1) + [hd] + qSort(p2)


# Implement an iterative qSort; average case time complexity: O(n log n)

def partition1(lst, x):
    i = 0
    j = len(lst) - 1

    while i < j and lst[i] <= x:
        i = i + 1
    while i < j and lst[j] > x:
        j = j - 1

    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i = i + 1
        j = j - 1

        while lst[i] <= x:
            i = i + 1
        while lst[j] > x:
            j = j - 1


def iter_qSort(lst):
    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        c = []
        for j in lst:
            c.append(j)
        i = 0
        while i < len(lst):
            partition1(lst, c[i])
            i = i + 1
        return lst

# Avg. case time complexity will be O(n log n)

print(iter_qSort([6, 1, 3, 4, 8, 0]))

