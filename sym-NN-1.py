# symmetric NN test 1, linear case

# The matrix M2 is of the form:
#	a b c
#	a b c
#	a b c
# This FAILS the symmetric test

import numpy as np

Row = np.random.rand(3)
M2 = np.vstack((Row, Row, Row))
print("M2 =\n", M2)

β = np.random.rand(1)
M1 = np.hstack((β, β, β))
print("M1 =\n", M1)

γ = np.random.rand(1)
print("γ = ", γ)

print()

x = np.random.rand(3)
print("x  =", x)

# permute x
σx = np.random.permutation(x)
print("σx =", σx)

print()

print("f(x)  =", γ + x.dot(M1) + (x.dot(M2)).dot(x))
print("f(σx) =", γ + σx.dot(M1) + (σx.dot(M2)).dot(σx))

print("M2(x)  =", x.dot(M2))
print("M2(σx) =", σx.dot(M2))

print("g(x)  =", γ + x.dot(M1))
print("g(σx) =", γ + σx.dot(M1))
