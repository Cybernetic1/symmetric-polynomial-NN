# symmetric NN, test 2, linear case

# The matrix M2 is of the form:
#	a b b
#	b a b
#	b b a
# symmetric test SUCCEEDS,
# but this is just 1 layer, what we will need is equivariance rather than invariance (symmetric)

import numpy as np

a = np.random.rand(1)
b = np.random.rand(1)

R1 = np.hstack((a, b, b))
R2 = np.hstack((b, a, b))
R3 = np.hstack((b, b, a))
M2 = np.vstack((R1, R2, R3))
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
