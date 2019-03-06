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

(stat1, primalx, primaly) = glpk.lp(c, G.T, h)
print("Optimal value for Primal:", c.T * primalx * -1)
print("Solution for Primal: \n", primalx)


c1 = matrix([6.0, -1.0, 5.0, 4.0])
G1 = matrix([[-2.0, -2.0, -5.0, -2.0],
            [-2.0, -1.0,  2.0,  2.0],
            [ 4.0,  2.0, -4.0, -5.0],
            [-4.0,  1.0, -4.0, -3.0],
            [-8.0,  3.0, -2.0, -1.0],
            [-1.0,  0.0,  0.0,  0.0],
            [ 0.0,  1.0,  0.0,  0.0],
            [ 0.0,  0.0,  0.0, -1.0]])

h1 = matrix([-4.0, 2.0, -5.0, -6.0, -7.0, 0.0, 0.0, 0.0])

(stat1, dualx, dualy) = glpk.lp(c1, G1.T, h1)
print("Optimal value for Dual:", c1.T * dualx)
print("Solution for Dual: \n", dualx)

print("Complementary Slackness for x")
for i in range(5):
    print((G1[:, i].T * dualx - h1[i]) * primalx[i])


print("Complementary Slackness for y")
for j in range(4):
    print((G[:, j].T * primalx - h[j]) * dualx[j])
