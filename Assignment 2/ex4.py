from cvxopt import glpk, matrix
import numpy as np

R = np.genfromtxt("graph.txt")

c = np.ones(200)

A = matrix(np.zeros(200))
b = matrix([0.0])

bs = set(range(200))
vs = set(range(200))

G = np.empty((0, 200), int)
ccount = 0

print("Generating constraints from graph...")

for i in range(200):
    for j in range(200 - i): #Matrisen är symmetrisk så vi behöver bara kolla på ena halvan
        if R[i][j] == 1:
            nc = np.zeros(200)
            nc[i] = 1
            nc[j] = 1
            G = np.vstack([G, nc])
            ccount = ccount + 1

print("Number of constraints generated:", ccount)

G = matrix(G * -1)
h = matrix(np.ones(ccount) * -1)

(stat, sol) = glpk.ilp(c, G, h, A.T, b, vs, bs)

npSum = np.array(sol)

print(np.sum(npSum))