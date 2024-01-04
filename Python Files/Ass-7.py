# QUES_1
'''
class Interval:
    def __init__(self, l, u):
        self.l = l
        self.u = u

    def __repr__(self):
        return 'The interval is ('+repr(self.l) +', '+repr(self.u) +')'

    def intadd():
            return print('Addition : ('+str(I1.l + I2.l) + ', '+str(I1.u + I2.u) +')')

    def intsub():
        if I1.l - I2.l > I1.u - I2.u:
            return print('Subtraction : (' + str(I1.u - I2.u) + ', ' + str(I1.l - I2.l) + ')')
        else:
            return print('Subtraction : (' + str(I1.l - I2.l) + ', ' + str(I1.u - I2.u) + ')')

    def intmult():
        if I1.l * I2.l > I1.u * I2.u:
            return print('Multiplication : (' + str(I1.u * I2.u) + ', ' + str(I1.l * I2.l) + ')')
        else:
            return print('Multiplication : (' + str(I1.l * I2.l) + ', ' + str(I1.u * I2.u) + ')')
    def intdiv():
        if I1.l / I2.l > I1.u / I2.u:
            return print('Division : (' + str(I1.u / I2.u) + ', ' + str(I1.l / I2.l) + ')')
        else:
            return print('Division : (' + str(I1.l / I2.l) + ', ' + str(I1.u / I2.u) + ')')

I1 = Interval(3, 6)
I2 = Interval(2, 100)

print(I1)
print(I2)
Interval.intadd()
Interval.intsub()
Interval.intmult()
Interval.intdiv()
'''


#QUES_2

import sys

class Stack:
    lst = []

    def __init__(self, *arg):
        self.arg = arg
        if len(arg) == 0:
            pass
        else:
            Stack.lst.append(self.arg)

    def __repr__(self):
        return Stack.lst


    def pop():
        if len(Stack.lst) == 0:
            return "Empty Stack"
        else:
            Stack.lst.pop(len(Stack.lst) - 1)
            return print(Stack.lst)

    def push(x):
        if 0 <= len(Stack.lst) < 5:
            Stack.lst.append(x)
            return Stack.lst
        else:
            return print("Stack is Full")

    def peek():
        return print(Stack.lst[len(Stack.lst) - 1])

    def isEmpty():
        if len(Stack.lst) == 0:
            return print(True)
        else:
            return print(False)

    def isFull():
        if len(Stack.lst) == 5:
            return print(True)
        else:
            return print(False)

Stack()
Stack.push(1)
Stack.push(2)
Stack.push(3)
Stack.push(4)


print(Stack.lst)

Stack.peek()
Stack.isEmpty()
Stack.isFull()
Stack.pop()







