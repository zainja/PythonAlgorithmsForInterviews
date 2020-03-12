import numpy as np

X = ([12, 4, 7],
     [4, 5, 8],
     [7, 8, 9])
Y = ([1, 2, 3],
     [4, 5, 6],
     [7, 8, 9])
res = np.cross(X, Y)
res1 = np.cross(res, res)
x_square = np.cross(X, X)
y_square = np.cross(Y,Y)
res2 = np.cross(x_square, y_square)
print("The value of the first test (AB)^2", res)
print("The value of A^2.B^2 ", res2)