# symmetric NN test 0

# Purpose of this test is to show that if the matrix form is invariant,
# then we can replace matrix elements with sub-matrices, and the resulting
# bigger matrix would be invariant under permutation of vector blocks

# The matrix M is of the form:
#	A B B
#	B A B
#	B B A
# where A, B are 2⨉2 sub-matrices
# This SUCCEEDS the symmetric test

import numpy as np

A = np.random.rand(2,2)
B = np.random.rand(2,2)

M1 = np.hstack((A,B,B))
M2 = np.hstack((B,A,B))
M3 = np.hstack((B,B,A))
M = np.vstack((M1,M2,M3))
print("M =\n", M)

x = np.random.rand(6)
print("x  =", x)

# permute x
σx = np.array([x[2], x[3], x[0], x[1], x[4], x[5]])
print("σx =", σx)

print("M x  =", x.dot(M))
print("M σx =", σx.dot(M))
