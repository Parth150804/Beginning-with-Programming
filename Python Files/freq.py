def freq(n):
    s = str(n)
    c0 = 0
    c1 = 0
    c2 = 0
    c3 = 0
    c4 = 0
    c5 = 0
    c6 = 0
    c7 = 0
    c8 = 0
    c9 = 0
    for i in range(len(s)):
        if int(s[i]) == 0:
            c0 += 1
        elif int(s[i]) == 1:
            c1 += 1
        elif int(s[i]) == 2:
            c2 += 1
        elif int(s[i]) == 3:
            c3 += 1
        elif int(s[i]) == 4:
            c4 += 1
        elif int(s[i]) == 5:
            c5 += 1
        elif int(s[i]) == 6:
            c6 += 1
        elif int(s[i]) == 7:
            c7 += 1
        elif int(s[i]) == 8:
            c8 += 1
        elif int(s[i]) == 9:
            c9 += 1
    return [(0,c0),(1,c1),(2,c2),(3,c3),(4,c4),(5,c5),(6,c6),(7,c7),(8,c8),(9,c9)]

print(freq(12345260))