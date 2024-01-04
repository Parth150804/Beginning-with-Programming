def partition_1(lst, x, start, end):
    def swap(i, j):
        temp = lst[j]
        lst[j] = lst[i]
        lst[i] = temp
    n = len(lst)
    l = start
    u = end
    while u > l:
        while lst[l] < x:
            l += 1
        while lst[u] > x:
            u -= 1
        swap(l, u)
    return l


def quicksort(lst):
    n = len(lst)
    L = [(0, n-1)]
    m = 1
    while m > 0:
        m = 0
        L1 = []
        for i in L:
            l, u = i
            if u > l:
                x = partition_1(lst, lst[l], l, u)
                L1.append((l, x))
                L1.append((x+1, u))
                m += 1
        L = L1
    print(lst)
#quicksort(([4, 1, 3, 12, 9, 2]))

def partition(lst, x):
    i = 0
    j = len(lst) - 1

    while i < j and lst[i] <= x:
        i = i + 1
    while i < j and lst[j] > x:
        j = j - 1

    while i < j:
        lst[i], lst[j] = lst[j], lst[i]
        i = i+1
        j = j-1
        
        while lst[i] <= x:
            i = i + 1
        while lst[j] > x:
            j = j - 1

    return lst

# print(partition([4, 1, 3, 12, 9, 2], 12))

## Object Oriented Programming

class Complex:
    # class variable -- available to all instances
    domainName = "Number"         # domainName is a class variable
    # real and imag are "instance-specific" variables
    def __init__(self, r, i):        # __init__ tells how our method or function
        self.real = r                # is going to take input and which input value
        self.imag = i                # will be considered real and imag.

    def __repr__(self):
        return 'Complex_Number(' + repr(self.real)+', '+repr(self.imag) + ')'            # How output should be
                                #Observe how above return statement is written           # represented

x = Complex(3, 2.5)
y = Complex(1, -1.5)
z = Complex(0.5, "svs")
print(x)
print(y)
print(z)
