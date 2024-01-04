from functools import reduce
class Queue:
    def __init__(self):
        self.arg = []

    def Enqueue(self, x):
        self.arg.append(x)

    def Dequeue(self):
        if len(self.arg) == 0:
            return "Queue is already Empty"
        else:
            res = reduce(lambda x, y: min(x, y[1]), self.arg, float("inf"))
            ind = [y[1] for y in self.arg].index(res)
            self.arg.pop(ind)
            return print(self.arg)

    def seek(self):
        res = reduce(lambda x, y: min(x, y[1]), self.arg, float("inf"))
        ind = [y[1] for y in self.arg].index(res)
        print("index of element with highest priority: ",  ind)

    def __repr__(self):
        return repr(self.arg)


myQ = Queue()
myQ.Enqueue(("A", 3))
myQ.Enqueue(("B", 5))
myQ.Enqueue(("C", 2))
myQ.Enqueue(("D", 1))
myQ.Enqueue(("E", 6))
#print(myQ)

#myQ.seek()
#myQ.Dequeue()


#Singly Linked List

class Node:
    """
    An object for storing a single node in a linked list

    Attributes:
        data: Data stored in node
        next_node: Reference to next node in linked list
    """

    def __init__(self, data, next_node = None):
        self.data = data
        self.next_node = next_node

    def __repr__(self):
        return "<Node data: %s>" % self.data

class SinglyLinkedList:
    """
    Linear data structure that stores values in nodes. The list maintains a reference to the first node, also called head.
    Each node points to the next node in the list

    Attributes:
        head: The head node of the list
    """

    def __init__(self):
        self.head = None
        # Maintaining a count attribute allows for len() to be implemented in
        # constant time
        self.__count = 0

    def is_empty(self):
        """
        Determines if the linked list is empty
        Takes O(1) time
        """

        return self.head is None

    def __len__(self):
        """
        Returns the length of the linked list
        Takesn O(1) time
        """

        return self.__count


#Doubly Linked List

class Node:
    def __init__(self, data, prev_node=None, next_node=None):
        self.data = data
        self.prev_node = prev_node
        self.next_node = next_node

    def __repr__(self):
        return "<Node data: %s>" % self.data

class DoublyLinkedList:
    def __init__(self):
        self.head = None
        self.__count = 0

    def is_empty(self):
        return self.head is None

    def __len__(self):
        return self.__count

def sort(lst):
    if len(lst) == 0 or len(lst) == 1:
        return lst
    else:
        hd = max(lst)
        lst.remove(hd)
        tl = lst
        return [hd] + sort(tl)

print(sort([6, 1, 2, 4, 5, 3]))