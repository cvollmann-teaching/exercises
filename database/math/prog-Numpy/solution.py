import numpy as np
import matplotlib.pyplot as plt

""" 4.1. """

""" 4.2."""

m, n = 10, 5

# help(np.arange)
print(np.arange(1, n, 2))
print(np.arange(n))

# help(np.linspace)
print(np.linspace(0, 1, n, endpoint=False))

# help(np.ones)
print(np.ones(n))
print(np.ones((n, n)))

# help(np.zeros)
print(np.zeros(n))
print(np.zeros((n, n)))

# help(np.eye)
print(np.eye(n))
print(np.eye(m, n))
print(np.eye(m, n, 3))

# help(np.diag)
print(np.diag(np.ones(n)))
print(np.diag(np.ones(n), 3))


# help(np.tile)
print(np.tile(np.arange(3), 2))
print(np.tile(np.arange(3), (2, 3)))
print(np.tile(np.ones((2, 2)), 3))

# help(np.repeat)
# Repeat elements of an array
print(np.repeat(np.arange(3), 2))
# print(np.repeat(np.arange(3), (2, 3)))
print(np.repeat(np.ones((2, 2)), 3))
print(np.repeat(np.ones((2, 2)), 3, axis=1))

# help(np.reshape)
x = np.eye(3)
print(x)
print(np.reshape(x, 9))

""" 4.3."""
# a) identity matrix

# b) zero matrix

# c) diagonal matrix
d = np.arange(n)
A = np.diag(d)
print(np.diag(d))
print(len(A), np.shape(A), A.ndim)
plt.figure()
plt.imshow(A)
plt.show()

# d)
A = np.ones((4, 4))
A[3, 1] = 6
A[2, 3] = 2
print(A)
print(len(A), np.shape(A), A.ndim)
plt.figure()
plt.imshow(A)
plt.show()

# e)
A = np.diag(np.arange(2, 7, 1), -1)
print(A)
print(len(A), np.shape(A), A.ndim)
plt.figure()
plt.imshow(A)
plt.show()

# f)
x = np.arange(4, 0, -1).reshape(2, 2)
A = np.tile(x, (2, 3))
print(A)
print(len(A), np.shape(A), A.ndim)
plt.figure()
plt.imshow(A)
plt.show()

# g)
x = np.arange(1, 16)
A = np.reshape(x, (5, 3), order='F')
print(A)
print(len(A), np.shape(A), A.ndim)
plt.figure()
plt.imshow(A)
plt.show()
