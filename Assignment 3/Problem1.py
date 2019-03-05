from cvxopt import glpk, matrix, solvers
import numpy as np

c = matrix([-4.0, 2.0, -5.0, -6.0, -7.0])
G = matrix([[ 2.0,  2.0, -4.0,  4.0,  8.0],
            [-2.0, -1.0,  2.0,  1.0,  3.0],
            [ 5.0, -2.0,  4.0,  4.0,  2.0],
            [-5.0,  2.0, -4.0, -4.0, -2.0],
            [ 2.0, -2.0,  5.0,  3.0,  1.0],
            [-1.0,  0.0,  0.0,  0.0,  0.0],
            [ 0.0, -1.0,  0.0,  0.0,  0.0],
            [ 0.0,  0.0, -1.0,  0.0,  0.0],
            [ 0.0,  0.0,  0.0, -1.0,  0.0],
            [ 0.0,  0.0,  0.0,  0.0, -1.0]])

h = matrix([6.0, 1.0, 5.0, -5.0, 4.0, 0.0, 0.0, 0.0, 0.0, 0.0])

(stat1, solx, soly) = glpk.lp(c, G.T, h)
print("Optimal value for Primal:", c.T * solx * -1)
print("Solution for Primal: \n", solx)


c = matrix([6.0, -1.0, 5.0, 4.0])
G = matrix([[-2.0, -2.0, -5.0, -2.0],
            [-2.0, -1.0,  2.0,  2.0],
            [4.0,   2.0, -4.0, -5.0],
            [-4.0,  1.0, -4.0, -3.0],
            [-8.0,  3.0, -2.0, -1.0],
            [-1.0,  0.0,  0.0,  0.0],
            [0.0,   1.0,  0.0,  0.0],
            [0.0,   0.0,  0.0, -1.0]])

h = matrix([-4.0, 2.0, -5.0, -6.0, -7.0, 0.0, 0.0, 0.0])

(stat1, solx, soly) = glpk.lp(c, G.T, h)
print("Optimal value for Dual:", c.T * solx)
print("Solution for Dual: \n", solx)