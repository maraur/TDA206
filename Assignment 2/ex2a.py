import numpy as np
from cvxopt import glpk
import cvxopt

# minimize w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5 + w6*x6

w = [4, 2, 3, 2, 1, 4]

c = cvxopt.matrix([4.0, 2.0, 3.0, 2.0, 1.0, 4.0])
ct = cvxopt.matrix([1.0, 1.0, 1.0, 1.0, 1.0, 1.0])
A = cvxopt.matrix([0.0, 0.0, 0.0, 0.0, 0.0, 0.0])
b = cvxopt.matrix([0.0])
G = cvxopt.matrix([[-1.0, -1.0, 0.0, 0.0, 0.0, 0.0], [-1.0, 0.0, -1.0, 0.0, 0.0, 0.0],
                   [-1.0, 0.0, 0.0, -1.0, 0.0, 0.0], [0.0, -1.0, 0.0, -1.0, 0.0, 0.0],
                   [0.0, 0.0, -1.0, -1.0, 0.0, 0.0], [0.0, 0.0, -1.0, 0.0, -1.0, 0.0],
                   [0.0, 0.0, 0.0, -1.0, 0.0, -1.0]])
h = cvxopt.matrix([-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0])

(stat, sol) = glpk.ilp(ct, G.T, h, A.T, b, set([0, 1]), set())

print(sol)
print()