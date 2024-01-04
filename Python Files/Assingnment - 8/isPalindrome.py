def isPalindrome(w):
    p = len(w)
    for i in range(p):
        if (p%2 == 0):
            if i == (p)/2 :
                return True
                break
            elif w[i] == w[(p-1)-i]:
                continue
            else:
                return False
                break
        else:
            if i == (p//2 ):
                return True
                break
            elif w[i] == w[(p-1)-i]:
                continue
            else:
                return False
                break
print(isPalindrome(''))