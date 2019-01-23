from cvxopt import matrix, solvers
#c = matrix([4.0, -2.0, 5.0, 6.0, 7.0])
c = matrix([-4.0, 2.0, -5.0, -6.0, -7.0])

# I need to switch around signs to get the correct inequalities
# Also need to add the for the bonds on x->
H = matrix([[1, 0, 0, 1, 0, 0, 1, 0, 0, 1, 0, 0],
            [-2, -1, 2, 1, 3],
            [5, -2, 4, 4, 2],
            [-5, 2, -4, -4, -2],
            [2, -1, 5, 3, 1],
            [-1.0, 0.0, 0.0, 0.0, 0.0],
            [0.0, -1.0, 0.0, 0.0, 0.0],
            [0.0, 0.0, -1.0, 0.0, 0.0],
            [0.0, 0.0, 0.0, -1.0, 0.0],
            [0.0, 0.0, 0.0, 0.0, -1.0]])

h = matrix([35, 40, 50, 20, 30, 30, 45, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0, 0])
sol = solvers.lp(c, H.T, h)
print(sol['x'])
optSol = sol['x']
optVal = c.T * optSol
print("Objective solution:")
print(optVal)