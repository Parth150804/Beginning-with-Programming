class Node:
    def __init__(self, item):
        self.key = item
        self.right = self.left = None

    def __repr__(self):
        return "<" + repr(self.left) + "," + repr(self.key) + "," + repr(self.right) + ">"


class BTree:
    def __init__(self, node):
        self.root = node

    def isEmpty(self):
        return self.root == None

    def insert(self, key):
        if self.root == None:
            self.root = Node(key)
        else:
            q = []  
            q.append(self.root)
            while not(q == []):
                n = q[0]
                q.pop(0)

                if n.left == None:
                    n.left = Node(key)
                    break
                elif n.right == None:
                    n.right = Node(key)
                    break
                else:
                    q.append(n.left)
                    q.append(n.right)

    def __repr__(self):
        return repr(self.root)


n10 = Node(10)
n20 = Node(20)        
n30 = Node(30)
n40 = Node(40)
n50 = Node(50)
n60 = Node(60)
n10.left = n20
n10.right = n30
n20.left = n40
n30.left = n50
n30.right = n60
bt = BTree(n10)     # n10 is root node of BTree
print(bt)
bt.insert(70)
print(bt)



############# Graphs
class Node:
    def __init__(self, name):
        self.iden = name
        self.nbors = []

    def addNbor(self, name):
        self.nbors.append(name)

    def getName(self):
        return self.iden
        
class Edge:
    def __init__(self, srcNode, dstNode, edWt):
        self.src = srcNode
        self.dst = dstNode
        self.ew = edWt

class Graph:
    def __init__(self):
        self.nodeMap = []
        self.edLst = []

    def addNode(self, name):
        n = Node(name)
        self.nodeMap.append((name, n))

    def getNode(self, name):
        for i in range(len(self.nodeMap)):
            if self.nodeMap[i][0] == name:
                return self.nodeMap[i][1]
            
        return None

    def addEdge(self, src, dst, wt):
        e = Edge(src, dst, wt)
        self.edLst.append(e)
        src.addNbor(dst.getName())
        dst.addNbor(src.getName())


