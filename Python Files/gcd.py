def gcd(x, y):
    if x > 0 and y > 0:
        p = min(x, y)
        q = max(x, y)
        i = p
        while i > 1:
            if p % i == 0 and q % i == 0:
                return i
            else:
                i -= 1
        return 1
    else:
        return "Invalid Input"

print(gcd(2,10))
print(gcd(230,64350))
print(gcd(4,8))
print(gcd(-2,-5))