# symmetric-NN
Symmetric (permutation-invariant) neural networks, in Python 3.6

matrix-multiply-test.py
-----------------------
simple test of NumPy functions to multiply 2 matrices

sym-NN-0.py
-----------
Simple test to show that invariance under permutations of vector **blocks** is possible, simply by replacing the invariant matrix's entries with **sub-matrices**.

sym-NN-1.py
-----------
Linear case.  The matrix form:

    a b c
    a b c
    a b c

is NOT invariant.

sym-NN-2.py
-----------
Linear case.  The matrix form:

    a b b
    b a b
    b b a

is invariant.

sym-NN-3.py
-----------
Linear case. The matrix M is of the form:

    a b c
    b a d
    c d a

Test result is that this is NOT equivariant.

sym-NN-4.py
-----------
The matrix A is of size (N ⨉ 2N) and of the form:

    e a a b c d
    a e a b c d
    a a e b c d

Result is that this FAILS the equivariance test.

sym-NN-5.py
-----------
Quadratic version.  First trial, result = FAIL.

sym-NN-6.py
-----------
Quadratic, corrected version.  SUCCESS for n = 3.

sym-NN-7.py
-----------
Quadratic, "algebraic" version.  This is evolved from the `count-colors` code.  SUCCESS for all n.

sym-NN-8.py
-----------
Quadratic, algebraic version 2.0.  SUCCESS for all n.

sym-NN-9.py
-----------
Quadratic, 'Colorful' algebraic version (see my paper).  SUCCESS for all n.

symNN-count-colors-1.py
-----------------------
We want to count the number of colors in the (2D) matrix A.  It has to satisfy the constraints in the (simplest) linear case.

The end result is we get a matrix like this:

    β α α
    α β α
    α α β

with 2 colors.

symNN-count-colors-2.py
-----------------------
The linear, folded-in-half case.  We get this matrix reuslt:

    5 1 1 2 3 4
    1 5 1 2 3 4
    1 1 5 2 3 4

with 5 colors.  Notice that this matrix form fails the equivariance test.  The constraints are not correctly derived for the folded-in-half case.

symNN-count-colors-3.py
-----------------------
Quadratic case.  Equation is of the form

    y = A x² = 〈A x, x〉

The program counts the number of colors in the 3D matrix A.

This code works, and is the pre-cursor for the **algebraic** versions.

poly-algebra-1.py
-----------------
**Symbolic** computer algebra.  Uses Python's operator-overloading to implement polynomial operations, ie, addition and multiplication of polynomials.

This version is able to perform some polynomial tests, and gives the correct result for the expansion of the linear matrix:

    y = A x

Not all polynomial operations are implemented in this version.

poly-algebra-2.py
-----------------
Quadratic case:

    y = 〈A x, x〉

Can perform the polynomial expansion, but does not "collect like terms".

poly-algebra-3.py
-----------------
This version is able to compose 3 quadratic layers!  Highest degree = 2³ = 8.

It takes a few minutes to run.  The coefficients are not printed out, as that would make the output too long.  Only the monomials are printed (in red color).

To-do
=====
1. Work out the back-propagation algorithm
2. Solve the 3-layer or 4-layer quadratic case, hopefully push the number of layers as high as possible
