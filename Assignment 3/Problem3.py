import numpy as np

G = np.genfromtxt("graph.txt")

A = np.zeros((200, 200))
chosenNodes = np.zeros(200)
emptyVec = np.zeros(200)

while np.sum(G):
    n = 1/1000
    A = A + G*n
    sums = np.sum(A, axis=1)
    for val in range(sums.size):
        if sums[val] >= 1:
            if np.sum(G[val]) != 0:
                G[val] = emptyVec
            if np.sum(G[:, val]) != 0:
                G[:, val] = emptyVec
            chosenNodes[val] = 1

print("The algorithm chose", np.sum(chosenNodes), "nodes")

var = input("Do you want to print the chosen nodes? (y/n)  ")
if var == 'y':
    idx = np.where(chosenNodes == 1)
    idx = [x + 1 for x in idx]
    print("The chosen nodes are: \n", np.concatenate(idx).tolist())
