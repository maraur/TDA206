from cvxopt.modeling import op, variable

x1 = variable()
x2 = variable()
x3 = variable()
x4 = variable()
x5 = variable()

c1 = (2*x1 + 2*x2 - 4*x3 + 4*x4 + 8*x5 <= 6)
c2 = (2*x1 + 1*x2 - 2*x3 - 1*x4 - 3*x5 >= -1)
c3 = (5*x1 - 2*x2 + 4*x3 + 4*x4 + 2*x5 == 5)
c4 = (2*x1 - 2*x2 + 5*x3 + 3*x4 + 1*x5 <= 4)
c5 = (x1 >= 0)
c6 = (x2 >= 0)
c7 = (x3 >= 0)
c8 = (x4 >= 0)
c9 = (x5 >= 0)
lp = op(-(4*x1 - 2*x2 + 5*x3 + 6*x4 + 7*x5), [c1, c2, c3, c4, c5, c6, c7, c8, c9])
lp.solve()
lp.status
print(lp.objective.value()*(-1))
