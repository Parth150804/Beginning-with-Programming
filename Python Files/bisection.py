import sys

# Quiz 5: imperative Bisection method
def bisection(f, a, b, tol):
    if f(a)*f(b) > 0:
        sys.exit("No roots in the specified interval")
    else:
        while (b-a) >= tol:
            m = (a+b)/2
            if f(m) == 0:
                break
            elif f(a)*f(m) < 0:
                b = m
            else:
                a = m
            
        print("The root is:", m)

# Assumption: f has no critical point b/w a & b

def bisectionRec(f, a, b, tol):
    if f(a)*f(b) > 0:
        return sys.exit("No roots in the specified interval")
    else:
        m = (a+b)/2
        if f(m) == 0 or (b-a) < tol:
            print("The root is:", m)
        elif f(a)*f(m) < 0:
            bisectionRec(f, a, m, tol)
        else:
            bisectionRec(f, m, b, tol)

def g(x):
    return x*(x-3)

bisection(g, 1, 4, 0.00000000000000000001)



        
