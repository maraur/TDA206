from cvxopt.modeling import op, variable
from numpy import array

x = variable(12)

c1 = (x[0] + x[3] + x[6] + x[9] <= 35)
c2 = (x[1] + x[4] + x[7] + x[10] <= 40)
c3 = (x[2] + x[5] + x[8] + x[11] <= 50)
c4 = (x[0] + x[1] + x[2] == 20)
c5 = (x[3] + x[4] + x[5] == 30)
c6 = (x[6] + x[7] + x[8] == 30)
c7 = (x[9] + x[10] + x[11] == 45)

cx = (x >= 0)

lp = op(6*x[0] + 9*x[1] + 12*x[2] + 9*x[3] + 5*x[4] + 7*x[5] + 10*x[6]
               + 16*x[7] + 13*x[8] + 8*x[9] + 14*x[10] + 9*x[11],
        [c1, c2, c3, c4, c5, c6, c7, cx])
lp.solve()
lp.status

xn = array(x.value)
xr = xn.round(5).T

print([xr[0][0], xr[0][3], xr[0][6], xr[0][9]])
print([xr[0][1], xr[0][4], xr[0][7], xr[0][10]])
print([xr[0][2], xr[0][5], xr[0][8], xr[0][11]])
print("Optimal Solution is:")
print(round(lp.objective.value()[0], 4))
print("Rounded Solution is:")
print(6*xr[0][0] + 9*xr[0][1] + 12*xr[0][2] + 9*xr[0][3] + 5*xr[0][4] + 7*xr[0][5] + 10*xr[0][6]
                 + 16*xr[0][7] + 13*xr[0][8] + 8*xr[0][9] + 14*xr[0][10] + 9*xr[0][11])
