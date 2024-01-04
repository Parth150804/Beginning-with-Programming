import sys

def isqrt(n):
    if n < 0:
        sys.exit("No isqrt is possible since n < 0")
    elif n == 0:
        return 0
    else:
        return shrink(n, 0,n)

def shrink(n,l,u):
    if l == u :
        return l
    elif (l < u and (l+1)**2 <= n):
        return shrink (n, l+1, u)
    elif ((l+1)**2 > n):
        return l
    elif (l < u and u**2 > n):
        return shrink (n, l, u-1)
    elif (l < u and (u-1)**2 <= n):
        return u-1
    else: # l > u
        sys.exit("Interval specification error ")

n = int(input("Enter a number: "))
print("isqrt of ", n, " is", isqrt(n))

'''
shrinkV2.0(n,l,u) =
   if (l ==u) or u == l+1 then return l
   if l < u and m**2 <=n then shrinkV2.0(n, m, u)
   if l < u and m**2 > n then shrinkV2.0(n,l,m)
where m = (l+u) //2
'''
