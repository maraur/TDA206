
# coding: utf-8

import random, numpy
def genDat(m=5e1,n=5e2,sigma=1e-2,nonZero=5):
    """m is no. of samples, n is dimnesion, so m < n
    nonZero is no. of non-zero elements in beta, sigma is variance """
    
    m = int(m)
    n = int(n)
    lis = list(range(n))
    ind = random.sample(lis,nonZero) #Indices of 5 non zero elements
    b = numpy.zeros((n,1))
    b[ind] = 1
    X = numpy.random.randn(m,n)
    y = numpy.matmul(X,b) + sigma*numpy.random.randn(m,1)
    
    x_test = numpy.random.randn(100,n)
    y_test = numpy.matmul(x_test,b)
    
    return X,y,x_test,y_test,b

