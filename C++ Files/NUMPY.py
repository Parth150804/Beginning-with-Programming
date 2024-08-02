import numpy as np

## BASICS

a = np.array([1, 2, 3], dtype = "int32")
# print(a)

b = np.array([[9.0, 8.0, 7.0], [6.0, 5.0, 4.0]])
# print(b)

# Get Dimension
# print(a.ndim)

# Get shape
# print(b.shape)          # Output (2, 3) as it is a 2x3 array

# Get Type
# print(a.dtype)

# Get Size
# print(a.itemsize)      # Size of each item in a

# Get total size
# print(a.size)         # Total number of elements        
# print(a.nbytes)       # Space of whole a


## ACCESSING/CHANGING SPECIFIC ELEMENTS, ROWS, COLUMNS, ETC.

a = np.array([[1, 2, 3, 4, 5, 6, 7], [8, 9, 10, 11, 12, 13, 14]])

# Get a specific element [row, col]
# print(a[1, 5])

# Get a specific row
# print(a[0, :])

# Get a specific column
# print(a[:, 2])

# Getting a little more fancy [startindex:endindex;stepsize]
# print(a[0, 1:6:2])

# Chaning value at a particular index
# a[1, 5] = 20
# print(a)

# Change entire column
# a[:, 2] = 5           # will make entire 3nd column as 5
# a[:, 2] = [1, 2]      # 3rd col 1st row as 1 & 3rd col 2nd row as 2

# 3-D example  <------------------
# b = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# print(b)

# Get a sepcific element
# print([0, 1, 1])

# Replace
# b[:, 1, :] = [[9, 9], [8, 8]]


## INITIALIZING DIFFERENT TYPES OF ARRAYS

# All zeros matrix
np.zeros(5)
np.zeros((2, 3))

# All ones matrix
np.ones((4, 2, 2), dtype = "int32")

# Any other Number
np.full((2, 2), 99)

# Any other Number (full_like)
np.full_like(a, 4)          # Shape as a but all values 4

# Random decimal Numbers
np.random.rand(4, 2)         # 4x2 matrix will all random decimal values
np.random.random_sample(a.shape)                # container with shape as of a and random decimal values 

# Random Integer Values
np.random.randint(7, size=(3, 3))           # First argument is the integer upto which integers should be taken in randomization

# Identity matrix
np.identity(3)

# Repeat an array
arr = np.array([[1, 2, 3]])
# r1 = np.repeat(arr, 3, axis = 0)
# [[1 2 3]
#  [1 2 3]
#  [1 2 3]]

r1 = np.repeat(arr, 3, axis = 1)
# [[1 1 1 2 2 2 3 3 3]]

# EXERCISE: Make this matrix using above concepts
# [[1 1 1 1 1]
#  [1 0 0 0 1]
#  [1 0 9 0 1]
#  [1 0 0 0 1]
#  [1 1 1 1 1]]

# SOLUTION:
# output = np.ones((5, 5))
# print(output)

# z = np.zeros((3, 3))
# z[1, 1] = 9
# print(z)

# output[1:4, 1:4] = z
# print(output)

# Copying Array
a = np.array([1, 2, 3])
b = a.copy()        # If we have used b = a, then b[0] = 100 have changed too!!
b[0] = 100


# MATHEMATICS

a = np.array([1, 2, 3, 4])
b = np.array([5, 6, 7, 8])
# All operations can be used directly like variables

# Take sine
np.sin(a)

# Take cosine
np.cos(a)

# Linear Algebra
c = np.ones((2, 3))

d = np.full((3, 2), 2)

e = np.identity(4)
np.matmul(c, d)         # <------ Matrix Multiplication

np.linalg.det(e)        # <------ Calculating determinant

# For more, use internet (like trace, inverse, eigenvalues, etc.)

# Statistics

stats = np.array([[1, 2, 3,], [4, 5, 6]])
# we can use axis aslo
np.min(stats)       # 1

np.max(stats, axis = 1)     # array([3, 6])

np.sum(stats, axis = 0)     # array([5, 7, 9])


## REORGANIZING ARRAYS

before = np.array([[1, 2, 3, 4], [5, 6, 7, 8]])

after = before.reshape((2, 2, 2))
# [[1, 2]
#  [3, 4]
#  [5, 6]]

v1 = np.array([1, 2, 3, 4])
v2 = np.array([5, 6, 7, 8])

np.vstack([v1, v2])         # Vertical Stack

h1 = np.ones((2, 4))
h2 = np.zeros((2, 2))

np.hstack((h1, h2))         # Horizontal Stack


# MISCELLANEOUS

# take out elements at a particular index
a = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9])
a[[1, 3, 7]]

# elements specifying a particular confition
a[a > 4]


# EXAMPLE
#        1  2  3  4  5
#        6  7  8  9  10
#        11 12 13 14 15
#        16 17 18 19 20
#        21 22 23 24 25
#        26 27 28 29 30

        
# indexing 11, 12, 16, 17 - a[2:4, 0:2]
# indexing 2, 8, 14, 20 - a[[0, 1, 2, 3], [1, 2, 3, 4]]
# indexing 4, 5, 24, 25, 29, 30 - a[[0, 4, 5], 3:]













