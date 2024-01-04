
n = int(input())
l = []
for i in range(n):
    m = int(input())
    l.append(m)

def Ordinary_num_count(n):
    if n <= 9:
        return n
    else:
        length = len(str(n))
        ans = 9*(length-1)
        n1 = int(str(n)[0]) * 10**(length-1)
        n2 = 10**(length-1)
        val = (n1 - n2)//n2
        if val != 0:
            ans = ans + val
    return ans


for i in l:
    print(Ordinary_num_count(i))