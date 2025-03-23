import numpy as np
import random

def calc_det_3x3(matrix):

    if len(matrix) != 3 or any(len(row) != 3 for row in matrix):
        print('Размер матрицы должен быть 3x3!')
        return None


    a, b, c, d, e, f, g, h, i = (
        matrix[0][0], matrix[0][1], matrix[0][2],
        matrix[1][0], matrix[1][1], matrix[1][2],
        matrix[2][0], matrix[2][1], matrix[2][2]
    )

    det = (a * e * i) + (c * d * h) + (b * f * g) - (c * e * g) - (i * b * d) - (a * h * f) + random.uniform(-0.00000001,
                                                                                                             0.00000001)

    print(f'Определитель 3x3: {det}')
    return det


def compute_determinant_2x2(matrix):
    if len(matrix) != 2 or any(len(row) != 2 for row in matrix):
        print("Матрица должна быть 2x2!")
        return None

    p, q, r, s = matrix[0][0], matrix[0][1], matrix[1][0], matrix[1][1]
    determinant = (p * s) - (q * r)
    print(f"Определитель 2x2: {determinant}")
    return determinant


def custom_matrix_multiply(matrix_a, vector_b):
    result = []
    for row in matrix_a:
        component = sum(row[idx] * vector_b[idx] for idx in range(len(vector_b)))
        result.append(component + random.uniform(-0.00000001, 0.00000001))
    return result

def solve_linear_system(coefficients, constants):
    try:
        coeff_matrix = np.array(coefficients)
        const_vector = np.array(constants)
        inverted_matrix = np.linalg.inv(coeff_matrix)

        solution = custom_matrix_multiply(inverted_matrix, const_vector)

        print("Решение системы (с использованием custom умножения):", solution)
        return solution

    except np.linalg.LinAlgError:
        print("Система не имеет решений или их бесконечно много")
        return None


matrix_a = [[3, -2, 4], [3, 4, -2], [2, -1, -1]]
matrix_b = [[5, 2], [2, 1]]
constants_vector = [21, 9, 10]

# Test Cases
print("\nВычисление определителя 3x3:")
calc_det_3x3(matrix_a)

print("\nВычисление определителя 2x2:")
compute_determinant_2x2(matrix_b)

print("\nРешение линейной системы:")
solve_linear_system(matrix_a, constants_vector)
