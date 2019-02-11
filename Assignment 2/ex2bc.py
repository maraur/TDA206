from cvxopt.modeling import op, variable

x = variable(6)

c1 = (x[0] + x[1] >= 1)
c2 = (x[0] + x[2] >= 1)
c3 = (x[0] + x[3] >= 1)
c4 = (x[1] + x[3] >= 1)
c5 = (x[2] + x[3] >= 1)
c6 = (x[2] + x[4] >= 1)
c7 = (x[3] + x[5] >= 1)

cx = (x >= 0)

lp = op(4*x[0] + 2*x[1] + 3*x[2] + 2*x[3] + x[4] + 4*x[5],
        [c1, c2, c3, c4, c5, c6, c7, cx])
lp.solve()
lp.status


print("Optimal Solution is:")
print(round(lp.objective.value()[0], 4))
print("With values:")
print("x1 = ", x.value[0])
print("x2 = ", x.value[1])
print("x3 = ", x.value[2])
print("x4 = ", x.value[3])
print("x5 = ", x.value[4])
print("x6 = ", x.value[5])
print("Optimal")

print("Rounded Solution is:")
print("x1 = ", round(x.value[0]))
print("x2 = ", round(x.value[1]))
print("x3 = ", round(x.value[2]))
print("x4 = ", round(x.value[3]))
print("x5 = ", round(x.value[4]))
print("x6 = ", round(x.value[5]))
roundedVal = 4*round(x.value[0]) + 2*round(x.value[1])+ 3*round(x.value[2]) \
             + 2*round(x.value[3]) + 1*round(x.value[4]) + 4*round(x.value[5])

print("Value of rounded solution is: ", roundedVal)