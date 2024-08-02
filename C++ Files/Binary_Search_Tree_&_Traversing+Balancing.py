# 2) Binary Trees
# a) Simple way to organise the data of users in company (using list)  (Not an efficient way)
class User:
    def __init__(self, username, name, email):
        self.username = username
        self.name = name
        self.email = email

    def __repr__(self):
        return "User(username = '{}', name = '{}', email = '{}')".format(self.username, self.name, self.email)
    
    def __str__(self):
        return self.__repr__()
    
class UserDatabase:
    def __init__(self):
        self.users = []
    
    def insert(self, user):       # Time_complexity = O(n)
        i = 0                       # Start with pointer equal to zero
        while i < len(self.users):               # This will insert a user in such a way that overall tree remains sorted (Alphabetically)
            # Find the first username greater than the new user's username   (here comparison is based on alphabetical order)
            if self.users[i].username > user.username:
                break
            i += 1
        self.users.insert(i, user)
    
    def find(self, username):     # Time_complexity = O(n)
        for user in self.users:
            if user.username == username:
                return user
    
    def update(self, user):       # Time_complexity = O(n)
        target = self.find(user.username)
        target.name, target.email = user.name, user.email
        
    def list_all(self):           # Time_complexity = O(1)
        return self.users

# Space complexity of all these functions = O(1)
aakash = User('aakash', 'Aakash Rai', 'aakash@example.com')
biraj = User('biraj', 'Biraj Das', 'biraj@example.com')
hemanth = User('hemanth', 'Hemanth Jain', 'hemanth@example.com')
jadhesh = User('jadhesh', 'Jadhesh Verma', 'jadhesh@example.com')
siddhant = User('siddhant', 'Siddhant Sinha', 'siddhant@example.com')
sonaksh = User('sonaksh', 'Sonaksh Kumar', 'sonaksh@example.com')
vishal = User('vishal', 'Vishal Goel', 'vishal@example.com')

#users = [aakash, biraj, hemanth, jadhesh, siddhant, sonaksh, vishal]

database = UserDatabase()

database.insert(hemanth)
database.insert(aakash)
database.insert(siddhant)
database.insert(biraj)

database.update(User(username = "siddhant", name = "Siddhant U", email = "siddhantu@example.com"))
# print(database.list_all())

# b) Method of Binary Tree (Efficient method)
# The node to the left of any key node will contain values which are smaller (here lexicographically) than the value in the key node.

class TreeNode:
    def __init__(self, key):
        self.key = key
        self.left = None
        self.right = None

# node0 = TreeNode(1)
# node1 = TreeNode(2)
# node2 = TreeNode(3)
# node3 = TreeNode(4)
# node4 = TreeNode(5)
# node5 = TreeNode(6)
# node6 = TreeNode(7)
# node7 = TreeNode(8)
# node8 = TreeNode(3)


# node1.key                               #              2
# node1.left = node2                      #        3           5
# node2.left = node0                      #      1         3        7
# node1.right = node4                     #                  4    6   8
# node4.right = node6
# node6.right = node7
# node4.left = node8
# node8.right = node3
# node6.left = node5

# Let's define a function which connect the nodes and creates the tree, e.g when we pass a data like this --> ((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8)))

def parse_tuple(data):
    # print(data)
    if isinstance(data, tuple) and len(data) == 3:     # isinstance(data, tuple) will return a bool value that
        node = TreeNode(data[1])                       # whether the data passed is in form of a tuple or not.
        node.left = parse_tuple(data[0])      #Using recursion
        node.right = parse_tuple(data[2])
    elif data is None:
        node = None
    else:
        node = TreeNode(data)
    return node

Tree = parse_tuple(((1, 3, None), 2, ((None, 3, 4), 5, (6, 7, 8))))   ## ------> Tree with key node at "2"
# print(Tree)      


def distanceK(node, k):         # Better problem will be the one in which given node is not a root node
    if node == None:            # So, we should have a val variable which stores the value of parent node (for upward traversal)
        return []
    elif k == 0:
        return [node.key]
    else:
        return distanceK(node.left, k-1) + distanceK(node.right, k-1)

# print(distanceK(Tree, 2))


def tree_to_list(node):
    if node is None:
        return None
    elif node.left == None and node.right == None:
        return node.key
    else:
        return [tree_to_list(node.left)] + [node.key] + [tree_to_list(node.right)]

    
# print(tree_to_list(Tree))
# Function to represent tree (rotated in 90 deg anticlockwise sense)

def display_keys(node, space='\t', level=0):
    # print(node.key if node else None, level)
    
    # If the node is empty
    if node is None:
        print(space*level + '∅')
        return   
    
    # If the node is a leaf 
    if node.left is None and node.right is None:
        print(space*level + str(node.key))
        return
    
    # If the node has children
    display_keys(node.right, space, level+1)
    print(space*level + str(node.key))
    display_keys(node.left,space, level+1)   


# print(display_keys(Tree, '  '))

#   8
#     7
#       6
#   5
#       4
#     3
#       ∅
# 2
#     ∅
#   3
#     1

# b) Traversing a Binary Tree (visiting each node exactly once)
# i) In-order Traversal:

def traverse_in_order(node):           # Returns a list in the order we traversed the Btree
    if node is None: 
        return []
    return(traverse_in_order(node.left) + 
           [node.key] + 
           traverse_in_order(node.right))

# print(traverse_in_order(Tree))

# ii) Pre_order Traversal:

def traverse_pre_order(node):
    if node is None:
        return []
    else:
        return [node.key] + traverse_pre_order(node.left) + traverse_pre_order(node.right)
    
# NOTE : for Post Order Traversal, the node key comes at last in return statement.
    
# print(traverse_pre_order(Tree))

# c) Height of a Tree:

def tree_height(node):
    if node is None:
        return 0
    return 1 + max(tree_height(node.left), tree_height(node.right))

# d) Size of a Tree (No. of elements in it):

def tree_size(node):
    if node is None:
        return 0
    return 1 + tree_size(node.left) + tree_size(node.right)


# a function to check if a binary tree is a binary search tree (BST).

# a function to find the maximum key in a binary tree.

# a function to find the minimum key in a binary tree.

# Here's a function that covers all of the above:

def remove_none(nums):
    return [x for x in nums if x is not None]

def is_bst(node):
    if node is None:
        return True, None, None
    
    is_bst_l, min_l, max_l = is_bst(node.left)
    is_bst_r, min_r, max_r = is_bst(node.right)
    
    is_bst_node = (is_bst_l and is_bst_r and 
              (max_l is None or node.key > max_l) and 
              (min_r is None or node.key < min_r))
    
    min_key = min(remove_none([min_l, node.key, min_r]))
    max_key = max(remove_none([max_l, node.key, max_r]))
    
    # print(node.key, min_key, max_key, is_bst_node)
        
    return is_bst_node, min_key, max_key


# d) Binary Search Trees:   (searching, deleting, inserting an element & calculating height of tree takes time O(log n), where n is no. of nodes)
# I) The left subtree of any node only contains nodes with keys less than the node's key
# II) The right subtree of any node only contains nodes with keys greater than the node's key

# We need to store user objects with each key in our BST. Let's define new class BSTNode to represent the 
# nodes of of our tree. Apart from having properties key, left and right, we'll also store a value and 
# pointer to the parent node (for easier upward traversal).

class BSTNode():            
    def __init__(self, key, value=None):    
        self.key = key
        self.value = value
        self.left = None
        self.right = None
        self.parent = None            
        
    def insert(node, key, value):
        if node is None:
            node = BSTNode(key, value)
        elif key < node.key:
            node.left = BSTNode.insert(node.left, key, value)
            node.left.parent = node
        elif key > node.key:
            node.right = BSTNode.insert(node.right, key, value)
            node.right.parent = node
        return node

    def find(node, key):
        if node is None:
            return None
        if key == node.key:
            return node
        if key < node.key:
            return BSTNode.find(node.left, key)
        if key > node.key:
            return BSTNode.find(node.right, key)
        
    def update(node, key, value):
        target = BSTNode.find(node, key)
        if target is not None:
            target.value = value

    def list_all(node):
        if node is None:
            return []
        return BSTNode.list_all(node.left) + [(node.key, node.value)] + BSTNode.list_all(node.right)
    
# A Binary tree is said to be balanced:
# the left subtree is balanced.
# the right subtree is balanced.
# the difference between heights of left subtree and right subtree is not more than 1.

    def is_balanced(node):
        if node is None:
            return True, 0
        balanced_l, height_l = BSTNode.is_balanced(node.left)
        balanced_r, height_r = BSTNode.is_balanced(node.right)
        balanced = balanced_l and balanced_r and abs(height_l - height_r) <=1
        height = 1 + max(height_l, height_r)
        return balanced, height
    
    def make_balanced_bst(data, lo=0, hi=None, parent=None):
        if hi is None:
            hi = len(data) - 1
        if lo > hi:
            return None
        
        mid = (lo + hi) // 2
        key, value = data[mid]

        root = BSTNode(key, value)
        root.parent = parent
        root.left = BSTNode.make_balanced_bst(data, lo, mid-1, root)
        root.right = BSTNode.make_balanced_bst(data, mid+1, hi, root)
        
        return root
    
    def balance_bst(node):
        return BSTNode.make_balanced_bst(BSTNode.list_all(node))
    
class TreeMap():
    def __init__(self):
        self.root = None
        
    def __setitem__(self, key, value):                # It is a combination of both insert and update
        node = BSTNode.find(self.root, key)
        if not node:                                    # if we do not find node our tree
            self.root = BSTNode.insert(self.root, key, value)
            self.root = BSTNode.balance_bst(self.root)
        else:                                           # if node is found
            BSTNode.update(self.root, key, value)
            
        
    def __getitem__(self, key):
        node = BSTNode.find(self.root, key)
        return node.value if node else None
    
    def __iter__(self):
        return (x for x in BSTNode.list_all(self.root))    # it returns a generator, that means, we can directly use it within a for loop
    
    def __len__(self):
        return tree_size(self.root)
    
    def display(self):
        return display_keys(self.root)
    

    
