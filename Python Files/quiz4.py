class Node:
    def __init__(self, val):
        self.value = val
        self.next = None
    def __repr__(self):
        return repr(self.value)

""" 

Use the above to implement the Queue object. Provide functions: enq(x), deq()

"""

class Queue:
    def __init__(self):
        self.front = self.rear = None

    def isEmpty(self):
        if self.front == None:
            return True
        else:
            return False

    def Enq(self, value):
        n = Node(value)
        if self.isEmpty(): 
            self.front = n
            self.rear = n
        else:
            self.rear.next = n
            self.rear = n

    def Deq(self):
        if self.isEmpty():
            return
        else:
            n = self.front
            self.front = n.next
            if self.front == None:
                self.rear = None
            return n

    def __repr__(self):
        n = self.front.next
        show ='<'
        while n:
            show += repr(n)+" "
            n = n.next
        show+= '>'
        return show

q = Queue()
for i in range(0, 50, 10):
    q.Enq(i)
    print(q)
