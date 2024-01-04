'''

def kth_odd_number(numbers, k):
    if k == 1:
        for num in numbers:
            if num % 2 != 0:
                return num
    else:
        kth_odd = kth_odd_number(numbers, k - 1)
        if kth_odd is None:
            return None
        else:
            index = numbers.index(kth_odd)
            numbers = numbers[index + 1:]
            return kth_odd_number(numbers, k - 1)

print(kth_odd_number([2,9,8,0,6,4], 1))


import sys
class set:
    lst = []
    def __init__(self, l, u):
        self.l = l
        self.u = u
        if l < u:
            set.lst.append(l)
            set.lst.append(u)
        else:
            sys.exit("Invalid input for a set")

    def __repr__(self):
        return set.lst

    def union(self, l1, l2):
        if (l1[0] < l2[0] and l1[1] < l2[1] and l1[1] < l2[0]) or (l2[0] < l1[0] and l2[1] < l1[1] and l2[1] < l1[0]):
            return l1 + "U" + l2
        elif (l1[0] < l2[0] and l1[1] < l2[1] and l1[1] > l2[0]) or (l2[0] < l1[0] and l2[1] < l1[1] and l2[1] > l1[0]):
'''

'''
def revIt(lst):
    if lst == []:
        return []
    else:
        hd, tl = lst[0], lst[1:]
        return revIt(tl) + [hd]

def Add1(lst1, lst2):
    if lst1 == []:
        return lst2
    elif lst2 == []:
        return lst1
    else:
        hd1, tl1 = lst1[0], lst1[1:]
        hd2, tl2 = lst2[0], lst2[1:]
        return [hd1 + hd2] + Add1(tl1, tl2)

'''
'''
class vending_mach:
    def __init__(self, r):
        n = int(input("No. of coins of 5: "))
        p = int(input("No. of coins of 10: "))
        q = int(input("No. of coins of 20: "))
        r = 5*n + 10*p + 20*q
        self.r = r

    def __repr__(self):
        pass

    def after_paying(self):
        while True:
            n = int(input(
                    "Tea - 15"
                    "Coffee - 20"
                    "Biscuit - 50"
                "Press 1 for Tea, 2 for Coffee and 3 for Biscuit"
                "Press the number as many times as the no. of item you want to buy"
                            ))
'''
'''
class Find:
    def __init__(self, l, t):
        self.l = l
        self.t = t

    def f(self):
        for i in range(len(self.l)):
            for j in range(len(self.l)):
                if self.l[i] + self.l[j] == self.t:
                    return i, j
                else:
                    continue

lst = [10, 20, 15, 35, 45]

C = Find(lst, 55)

print(C.f())
'''
'''

'''
'''
def Bin_search(lst, target):
    # assert: lst must be sorted in ascending order
    if len(lst) == 0:
        return False
    else:
        mid = len(lst) // 2
        if lst[mid] == target:
            return True
        else:
            if lst[mid] < target:
                return Bin_search(lst[mid + 1:], target)
            else:
                return Bin_search(lst[:mid], target)


list = [21, 34, 56, 77, 98, 100]
Bin_search(list, 40)
    
'''

'''
class Solution:
    def successfulPairs(self, spells, potions, success):
        pairs = []
        for i in range(len(spells)):
            count = 0
            for j in range(len(potions)):
                if spells[i]*potions[j] >= success:
                    count = count + 1
                else:
                    pass
            pairs.append(count)
        return pairs
'''

class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.right = None
        self.left = None

    def add_child(self, data):
        if self.data == data:
        # Since BinaryTree cannot have duplicate values
            return
        elif data < self.data:
        # add data in the left subtree
            if self.left:
                self.left.add_child(data)
            else:
                self.left = BinarySearchTreeNode(data)
        else:
        # add data in right subtree
            if self.right:
                self.right.add_child(data)
            else:
                self.right = BinarySearchTreeNode(data)

    def in_order_traversal(self):
        elements = []

    # visit left tree
        if self.left:
            elements = self.left.in_order_traversal()

    # visit base node
        elements.append(self.data)

    # visit right tree
        if self.right:
            elements = self.right.in_order_traversal()

        return elements


def build_tree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1, len(elements)):
        root.add_child(elements[i])

    return root

if __name__ == '__main__':
    numbers_tree = build_tree([9, 2, 3, 8, 1, 0])
    print(numbers_tree.in_order_traversal())
'''
        
        
'''
class Solution:
    def longestPalindrome(self, s: str) -> str:
        def rev(string):
            st = ""
            for i in range(1, len(string)+1):
                st = st + string[-i]
            return st

        lst = []
        for i in range(len(s)-1):
            j = len(s) - 1
            while j >= i:
                if s[i:j+1] == rev(s[i:j+1]):
                    lst.append(s[i:j+1])
                    j = j - 1
                else:
                    j = j - 1
        if len(lst) == 0:
            return s[0]
        else:
            return max(lst, key=len)

m = Solution()
print(m.longestPalindrome("abb"))

