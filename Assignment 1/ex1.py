from cvxopt.modeling import op, variable

x = variable(5)

c1 = (2*x[0] + 2*x[1] - 4*x[2] + 4*x[3] + 8*x[4] <= 6)
c2 = (2*x[0] + 1*x[1] - 2*x[2] - 1*x[3] - 3*x[4] >= -1)
c3 = (5*x[0] - 2*x[1] + 4*x[2] + 4*x[3] + 2*x[4] == 5)
c4 = (2*x[0] - 2*x[1] + 5*x[2] + 3*x[3] + 1*x[4] <= 4)
cx = (x >= 0)

lp = op(-(4*x[0] - 2*x[1] + 5*x[2] + 6*x[3] + 7*x[4]), [c1, c2, c3, c4, cx])
lp.solve()
lp.status

print(lp.objective.value()[0]*(-1))
