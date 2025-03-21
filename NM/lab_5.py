import numpy as np


def determinant_3x3(matrix):
    return np.linalg.det(matrix)


A = np.array([[3, -2, 4],
              [3, 4, -2],
              [2, -1, -1]])
det_A = determinant_3x3(A)
print("Определитель матрицы А:", det_A)
