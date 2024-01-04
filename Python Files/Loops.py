#Str = "Hello Parth Gautam"
#print(Str[11:] + " " + Str[6:11] + " " + Str[:5])
#Ques 1
'''
def rev(string):
    i = len(string) - 1
    while 0 <= i <= len(string):
        if string[i] == " ":
            return string[i+1:] + " " + rev(string[:i])    # Here recursion is used
        else:
            i = i - 1

    return string


s = input("Enter a sentence: ")
print(rev(s))
'''
'''
l=[]
word1=''
for i in s:
    if i!=' ':
        word1+=i
    elif i==' ':
        l.append(word1)
        word1=''
l.append(word1)
l.reverse()
statement=' '
for i in l:
    statement=statement+' '+i
print(statement)

#st = str(input("Write a sentence: "))
#print(rev(st))
#INV: ?
'''













