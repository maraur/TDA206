
# coding: utf-8

import random, numpy
import cvxpy as cp
import datetime


def genDat(m=5e1, n=5e2, sigma=1e-2, nonZero=5):
    """m is no. of samples, n is dimnesion, so m < n
    nonZero is no. of non-zero elements in beta, sigma is variance """
    
    m = int(m)
    n = int(n)
    lis = list(range(n))
    ind = random.sample(lis, nonZero)  # Indices of 5 non zero elements
    b = numpy.zeros((n, 1))
    b[ind] = 1
    X = numpy.random.randn(m, n)
    y = numpy.matmul(X, b) + sigma*numpy.random.randn(m, 1)
    
    x_test = numpy.random.randn(100, n)
    y_test = numpy.matmul(x_test, b)
    
    return X, y, x_test, y_test, b


def leastSquare(X, y, vSize, integer=False):
    lmbd = 0.001
    if integer:
        beta = cp.Variable((vSize, 1), boolean=True)
    else:
        beta = cp.Variable((vSize, 1))
    prob = cp.Problem(cp.Minimize(cp.norm((X * beta) - y, 2)))
    prob.solve()
    return beta.value


def lasso(X, y, vSize, integer=False):
    lmbd = 0.001
    if integer:
        beta = cp.Variable((vSize, 1), boolean=True)
    else:
        beta = cp.Variable((vSize, 1))
    prob = cp.Problem(cp.Minimize(cp.norm((X * beta) - y, 2) + lmbd * cp.norm1(beta)))
    prob.solve()
    return beta.value


def checkSolution(x_test, y_test, beta):
    n = cp.matmul(x_test, beta) - y_test
    return cp.norm(n, 2)


# --------------------------------------------------------------------------------------
# Running starts from here
# --------------------------------------------------------------------------------------
vals = [5e1, 5e2, 5e3, 5e4]

for i in range(2): #Run range(3) for all the test sets however it crashes for anything but the first one
    X, y, x_test, y_test, b = genDat(vals[i*2], vals[i*2+1])
    print("Running least squares for data set number", i+1)
    a = datetime.datetime.now()
    beta = leastSquare(X, y, int(vals[i*2+1]), False)
    b = datetime.datetime.now()
    print("Running least square took", b-a)
    c = checkSolution(x_test, y_test, beta)
    print("Least square got error:", c.value)
    print("Running LASSO for data set number", i+1)
    a = datetime.datetime.now()
    betaLasso = lasso(X, y, int(vals[i*2+1]), False)
    b = datetime.datetime.now()
    print("Running LASSO took", b-a)
    c = checkSolution(x_test, y_test, betaLasso)
    print("LASSO got error:", c.value)


