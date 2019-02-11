from cvxopt import glpk, matrix
import numpy as np

# minimize w1*x1 + w2*x2 + w3*x3 + w4*x4 + w5*x5 + w6*x6

w = [4, 2, 3, 2, 1, 4]

c = matrix([4.0, 2.0, 3.0, 2.0, 1.0, 4.0])
G = matrix([[-1.0, -1.0, 0.0, 0.0, 0.0, 0.0], [-1.0, 0.0, -1.0, 0.0, 0.0, 0.0],
            [-1.0, 0.0, 0.0, -1.0, 0.0, 0.0], [0.0, -1.0, 0.0, -1.0, 0.0, 0.0],
            [0.0, 0.0, -1.0, -1.0, 0.0, 0.0], [0.0, 0.0, -1.0, 0.0, -1.0, 0.0],
            [0.0, 0.0, 0.0, -1.0, 0.0, -1.0]])
h = matrix([-1.0, -1.0, -1.0, -1.0, -1.0, -1.0, -1.0])

(stat, sol) = glpk.ilp(c, G.T, h, I={0, 1, 2, 3, 4, 5}, B={0, 1, 2, 3, 4, 5})

print(sol)

print("------------------------------------------------------------")
print("Solution to LP-relaxation")
print("------------------------------------------------------------")

GLP = G.T
for i in range(6):
    nc = np.zeros(6)
    nc[i] = -1
    nc2 = np.zeros(6)
    nc2[i] = 1
    GLP = np.vstack([GLP, nc])
    GLP = np.vstack([GLP, nc])
    h = np.vstack([h, 0])
    h = np.vstack([h, 1])

hlp = matrix(h, tc='d')
GLP = matrix(GLP, tc='d')

(stat1, x, z) = glpk.lp(c, GLP, hlp)

print(x)

