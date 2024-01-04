'''
 Perfect(n) = n == Sum_{k = 1}^{n-1} k s.t. k is a divisor of n
'''

def perfect(n):
    if (n <= 0):
        sys.exit("NonPositive")
    else:
        def  sumDivisors(l, u):
            if (l > u):
	        return 0
            else:
                return ifdivisor(l) + sumDivisors(l+1, u)

        def ifdivisor(l):
	    if (n%l == 0):
		return l
	    else:
             	return 0

        return (n == sumDivisors(1, n-1))

