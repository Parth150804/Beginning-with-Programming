class BinaryT:
    def __init__(self):
        self.tree = EmptyNode()           #As soon as we initialise the BinaryT, an empty node will be created 
                                          #                                         (whose representation is *)
    def __repr__(self):
        return repr(self.tree)           # repr of BinaryT is repr of self.tree, which is basically equal
                                         # to class Emptynode() whose repr is '*'.
    def lookup(self, value):
        return self.tree.lookup(value)     # returns lookup function of self.tree (which is basically EmptyNode())
                                           # with value as its argument
    def insert(self, value):
        self.tree = self.tree.insert(value)

class EmptyNode:
    def __repr__(self):
        return '*'

    def lookup(self, value):       # Lookup after an empty node is False
        return False

    def insert(self, value):
        return BinaryNode(self, value, self)    #After insertion of a value at a node, two empty child
                                                # nodes will be automatically created
class BinaryNode:                                 
    def __init__(self, left, value, right):
        self.data = value
        self.leftT = left                # See, here self.leftT = left
        self.rightT = right              # and self.rightT = right

    def lookup(self, value):            # This is basically to find a value in Btree
        if self.data == value:
            return True
        elif self.data > value:
            return self.leftT.lookup(value)
        else:
            return self.rightT.lookup(value)

    def insert(self, value):
        if self.data > value:
            self.leftT = self.leftT.insert(value)
        elif self.data < value:
            self.rightT = self.rightT.insert(value)

        return self

    def __repr__(self): 
        #return ('(%s %s %s)' %(repr(self.leftT), repr(self.data), repr(self.rightT)))               # %s is used to join strings, E.g = "Hey, %s" % Parth -> Hey, Parth
        return "(" + repr(self.leftT) + " " + repr(self.data) + " " + repr(self.rightT) + ")"  # <--  (This is same as above return statement)                               
    
x = BinaryT()          # Here 'x' is an empty node, so '*' will be printed                                      
print(x)
for i in [3, 1, 9, 2, 7, 6, 5]:
    x.insert(i)
    print(x)


""" Queue data structure: FIFO(First in First out)
Used in Printers to schedule the jobs,
schedulers, all applications that perform services in online
marketplaces like Amazon etc. in CPUs.  Queues are very useful when
implementing algorithms in computer science such as the Breadth-First
Search algorithm used in flight reservation systems.

"""

class myQ:
    def __init__(self):
        self.__items = []

    def enq(self, item):
        self.__items.append(item)
        # what if the queue had a given size?

    def deq(self):
        return self.__items.pop(0)  # pop returns the popped element
                                    # Since Queue is FIFO kind of data st.
                                    # in this case it will pop out first added element
    def peek(self):
        return self.__items[0]

    def isEmpty(self):
        return len(self.__items) == 0           # will return True if len is 0 otherwise False

    def size(self):
        return len(self.__items)

    def __repr__(self):
        return repr(self.__items)

q = myQ()

#print(q)   #will print list or queue
q.enq("a")
q.enq(1)     #All these elements are appended in queue
q.enq((True, 5))
#print(q.deq())
#print(q)
    
