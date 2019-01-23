from cvxopt.modeling import op, variable

x1 = variable()
x2 = variable()
x3 = variable()
x4 = variable()
x5 = variable()
x6 = variable()
x7 = variable()
x8 = variable()
x9 = variable()
x10 = variable()
x11 = variable()
x12 = variable()

c1 = (x1 + x4 + x7 + x10 <= 40)
c2 = (x2 + x5 + x8 + x11 <= 45)
c3 = (x3 + x6 + x9 + x12 <= 55)
c4 = (x1 + x2 + x3 == 20)
c5 = (x4 + x5 + x6 == 30)
c6 = (x7 + x8 + x9 == 30)
c7 = (x10 + x11 + x12 == 45)

cx1 = (x1 >= 0)
cx2 = (x2 >= 0)
cx3 = (x3 >= 0)
cx4 = (x4 >= 0)
cx5 = (x5 >= 0)
cx6 = (x6 >= 0)
cx7 = (x7 >= 0)
cx8 = (x8 >= 0)
cx9 = (x9 >= 0)
cx10 = (x10 >= 0)
cx11 = (x11 >= 0)
cx12 = (x12 >= 0)

lp = op(6*x1 + 9*x2 + 12*x3 + 9*x4 + 5*x5 + 7*x6 + 10*x7 + 16*x8 + 13*x9 + 8*x10 + 14*x11 + 9*x12,
        [c1, c2, c3, c4, c5, c6, c7, cx1, cx2, cx3, cx4, cx5, cx6, cx7, cx8, cx9, cx10, cx11, cx12])
lp.solve()
lp.status

A = [[round(x1.value[0], 5), round(x4.value[0], 5), round(x7.value[0], 5), round(x10.value[0], 5)],
     [round(x2.value[0], 5), round(x5.value[0], 5), round(x8.value[0], 5), round(x11.value[0], 5)],
     [round(x3.value[0], 5), round(x6.value[0], 5), round(x9.value[0], 5), round(x12.value[0], 5)]
     ]
print(A[0])
print(A[1])
print(A[2])
print("Optimal Solution is:")
print(round(lp.objective.value()[0], 4))


#Nånting verkar galet....