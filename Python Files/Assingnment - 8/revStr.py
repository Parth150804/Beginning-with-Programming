def rev(string):
    i = len(string) - 1
    while 0 <= i <= len(string):
        if string[i] == " ":
                return string[i+1:] + " " + rev(string[:i])
        else:
            i = i - 1

    return string


s = input("Enter a sentence: ")
print(rev(s))