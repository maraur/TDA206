from cvxopt import glpk, matrix, solvers
import numpy as np

G = np.genfromtxt("graph.txt")

A = np.zeros((200, 200))
chosenNodes = np.zeros(200)

for i in range(100000):
    if np.sum(G) == 0:
        break
    n = 1/1000
    A = A + G*n
    sums = np.sum(A, axis=1)
    for val in range(sums.size):
        if sums[val] > 1:
            G[val] = np.zeros(200)
            G[:, val] = np.zeros(200)
            chosenNodes[val-1] = 1

print(sum(chosenNodes))