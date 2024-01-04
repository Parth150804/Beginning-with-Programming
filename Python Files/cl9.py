# Recursive version
def lin_Search(lst, x, index):
    if lst == []:
        return None, False
    else:
        hd, tl = lst[0], lst[1:]
        if hd == x:
            return index, True
        else:
            return lin_Search(tl, x, index+1)

#print(lin_Search([1,2,'a',True,4,6], 2, 0))
#Time complexity is O(n)
#where n is the size of list

#Binary Search Tree (lst must be sorted)
def bin_Search (lst, x, l, u):     # l & u are lower and upper bound indices
    if l > u:
        return None, False
    else: 
        mid = (l+u)//2
        if lst[mid] == x:
            return (mid, True)
        elif lst[mid] > x:
            return bin_Search(lst, x, l, mid-1)
        else:
            return bin_Search(lst, x, mid+1, u)
    
# Timing analysis: T(n) = 1 + T(n/2)
# T(1) = 1

# Note these recursive bin and lin search return index, boolean
"""
Proof of correctnes: 
Proof stmt: binSearch is true for inputs where u - l = n
I.H> stmt is true for a range 0 to n 
I.S> 
x = lst [mid] 
x < lst[mid] ==> x < lst [k] for all k > mid . this means 
that the search has to be made on l, mid-1, ===> invoke your IH.
       1
  2          3

4           5    6

1--> 2  3
Depth First Search 
Breadth First Search 
"""

# collection of key:value pairs is called a dictionary  
graph = {
  'root': ['n2', 'n3'],
  'n2': ['n4', 'n5'],
  'n3': ['n6'],
  'n4': [],
  'n5': ['n6'],
  'n6': []
}

# hold all the visited states so far
visited = set()

"""
Note on loops: Program structures that 
execute a sequence of statements repeatedly 
until a termination condition is met
It comes in two forms: for loops and while loops
"""


def DepthFirstSearch(G, node, visited):
    if node not in visited:
        print(node)
        visited.add(node)
        for child in G[node]:
            DepthFirstSearch(G, child, visited)

print("The DFS of a graph from the root node is:")
DepthFirstSearch(graph, 'root', visited)


visited = []   # List for visited nodes.
queue = []     # Initialize a queue

def BreadthFirstSearch(G, node, visited): #function for BFS
  visited.append(node)
  queue.append(node)

  while queue:          # Creating loop to visit each node
    m = queue.pop(0)
    print(m)

    for neighbour in graph[m]:
        if neighbour not in visited:
            visited.append(neighbour)
            queue.append(neighbour)

# Driver Code
print("Following is the Breadth-First Search")
BreadthFirstSearch(graph, 'root', visited)

