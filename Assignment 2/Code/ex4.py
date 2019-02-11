from cvxopt import glpk, matrix, solvers
import numpy as np

R = np.genfromtxt("graph.txt")

nmbrOfNodes = 100

c = np.ones(nmbrOfNodes)

bs = set(range(nmbrOfNodes))
vs = set(range(nmbrOfNodes))

G = np.empty((0, nmbrOfNodes), int)
ccount = 0

print("Generating constraints from graph...")

for i in range(nmbrOfNodes):
    for j in range(nmbrOfNodes - i): # Matrix is symmetric, hence we only need to look at
        if R[i][j+i] == 1:
            nc = np.zeros(nmbrOfNodes)
            nc[i] = 1
            nc[j+i] = 1
            G = np.vstack([G, nc])
            ccount += 1

print("Number of constraints generated:", ccount)

print("------------------------------------------------------------")
print("Solution to integer linear programming")
print("------------------------------------------------------------")

G = matrix(G * -1)
h = matrix(np.ones(ccount) * -1)

(stat, sol) = glpk.ilp(c, G, h, I=vs, B=bs)
npSum = np.array(sol)
print("Value of integer optimal solution:" ,np.sum(npSum))


print("------------------------------------------------------------")
print("Solution to LP-relaxation")
print("------------------------------------------------------------")

def correct_round(x):
    try:
        y = [actually_correct_round(z) for z in x]
    except:
        y = round(x)
    return y

def actually_correct_round(x):
    if (x % 1 == 0.5):
        return np.ceil(x)
    else:
        return round(x)

for i in range(nmbrOfNodes):
    nc = np.zeros(nmbrOfNodes)
    nc[i] = -1
    nc2 = np.zeros(nmbrOfNodes)
    nc2[i] = 1
    G = np.vstack([G, nc])
    G = np.vstack([G, nc])
    h = np.vstack([h, 0])
    h = np.vstack([h, 1])

GLP = matrix(G)
hlp = matrix(h)

(statlp, x, z) = glpk.lp(c, GLP, hlp)
print(np.sum(x))
print(correct_round(x))
print(np.array(x).T)
print("ROUNDED OPTIMAL SOLUTION GIVES SOLUTION:")
print(np.sum(correct_round(x)))


print("------------------------------------------------------------")
print("Solution by from given algorithm")
print("------------------------------------------------------------")

S = np.zeros(100)

for i in range(nmbrOfNodes):
    for j in range(nmbrOfNodes - i): # Matrix is symmetric, hence we only need to look at
        if R[i][j+i] == 1:
            if S[i] == 0 and S[j+i] == 0:
                if x[i] >= x[j+i]:
                    S[i] = 1
                else:
                    S[j+i] = 1

print("value of solution given by algorithm:" , np.sum(S))
