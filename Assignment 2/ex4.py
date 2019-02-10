from cvxopt import glpk, matrix
import numpy as np

f = open("graph.txt", "r")

if f.mode == 'r' :
    contents = f.read()
    #print(contents)
    G = matrix(np.genfromtxt("graph.txt") * -1)
    print(G)


c = np.ones(200)
h = matrix(np.ones(200) * -1)

A = matrix(np.zeros(200))
b = matrix([0.0])

bs = set(range(200))
vs = set(range(200))

(stat, sol) = glpk.ilp(c, G, h, A.T, b, vs, bs)
