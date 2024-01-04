def partition(lst, x):
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

    return j

def small(lst, k, index):
    l = len(lst)
    if k <= l and k > 0:
        if index < l:
            ls = lst[0:]
            i = (ls, index)
            if i == k-1:
                print(ls[i])
            else:
                small(lst, k, index + 1)
    else:
        print('Value of k is invalid!')

L = [34, 75, 23, 12, 9, 23, 67, 92, 21, 1, 69]
(small(L, 4, 0))