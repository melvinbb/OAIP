import random


def create_matrix(rows, cols, input_method="random", min_val=-10, max_val=10):
    matrix = []
    if input_method == "keyboard":
        print("Введите элементы матрицы построчно:")
        for i in range(rows):
            while True:
                try:
                    row_input = input(f"Введите {cols} элементов для строки {i + 1}, через пробел:\n>\t")
                    row = list(map(int, row_input.split()))
                    if len(row) != cols:
                        print(f"Ожидается {cols} элементов. Попробуйте снова.")
                        continue
                    matrix.append(row)
                    break
                except ValueError:
                    print("Введены некорректные данные. Попробуйте снова.")
    else:
        matrix = [[random.randint(min_val, max_val) for _ in range(cols)] for _ in range(rows)]
    return matrix


def print_matrix_dimensions(matrix):
    rows = len(matrix)
    cols = len(matrix[0]) if matrix else 0
    print(f"Размерность матрицы: {rows} x {cols}")


def print_matrix(matrix):
    for row in matrix:
        print('  '.join(map(str, row)))


def transpose_matrix(matrix):

    return [list(row) for row in zip(*matrix)]


def scalar_multiply(matrix, scalar):

    return [[element * scalar for element in row] for row in matrix]


def matrix_add(matrix1, matrix2):

    rows1 = len(matrix1)
    cols1 = len(matrix1[0]) if rows1 else 0
    rows2 = len(matrix2)
    cols2 = len(matrix2[0]) if rows2 else 0

    if rows1 != rows2 or cols1 != cols2:
        raise ValueError("Матрицы должны быть одного размера для сложения.")

    return [[matrix1[i][j] + matrix2[i][j] for j in range(cols1)] for i in range(rows1)]


def matrix_subtract(matrix1, matrix2):

    rows1 = len(matrix1)
    cols1 = len(matrix1[0]) if rows1 else 0
    rows2 = len(matrix2)

    cols2 = len(matrix2[0]) if rows2 else 0
    if rows1 != rows2 or cols1 != cols2:
        raise ValueError("Матрицы должны быть одного размера для вычитания.")

    return [[matrix1[i][j] - matrix2[i][j] for j in range(cols1)] for i in range(rows1)]


def matrix_multiply(matrix1, matrix2):
    rows1 = len(matrix1)
    cols1 = len(matrix1[0]) if rows1 else 0
    rows2 = len(matrix2)
    cols2 = len(matrix2[0]) if rows2 else 0

    if cols1 != rows2:
        raise ValueError(
            "Количество столбцов первой матрицы должно быть равно количеству строк второй матрицы для умножения.")

    result_matrix = [[0 for _ in range(cols2)] for _ in range(rows1)]
    for i in range(rows1):
        for j in range(cols2):
            for k in range(cols1):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]
    return result_matrix


matrix_1_data = [
    [7, 7, -2],
    [1, -2, -4],
    [3, -6, 4]
]

matrix_2_data = [
    [-4, 2, 9],
    [-9, 2, -2],
    [-3, -1, 2]
]

matrix_1 = matrix_1_data
matrix_2 = matrix_2_data

print("Матрица 1:")
print_matrix_dimensions(matrix_1)
print_matrix(matrix_1)

print("\nМатрица 2:")
print_matrix_dimensions(matrix_2)
print_matrix(matrix_2)

transposed_matrix_1 = transpose_matrix(matrix_1)
print("\nТранспонированная матрица 1:")
print_matrix(transposed_matrix_1)

multiplied_matrix_2 = scalar_multiply(matrix_2, 3)
print("\nМатрица 2, умноженная на 3:")
print_matrix(multiplied_matrix_2)


try:
    added_matrix = matrix_add(matrix_1, matrix_2)
    print("\nРезультат сложения матриц 1 и 2:")
    print_matrix(added_matrix)
except ValueError as e:
    print(f"\nОшибка сложения матриц: {e}")


try:
    subtracted_matrix = matrix_subtract(matrix_1, matrix_2)
    print("\nРезультат вычитания матриц 1 и 2:")
    print_matrix(subtracted_matrix)
except ValueError as e:
    print(f"\nОшибка вычитания матриц: {e}")


try:
    multiplied_matrix = matrix_multiply(matrix_1, matrix_2)
    print("\nРезультат умножения матриц 1 и 2:")
    print_matrix(multiplied_matrix)
except ValueError as e:
    print(f"\nОшибка умножения матриц: {e}")


print("\nСоздание случайной матрицы:")
random_matrix = create_matrix(3, 4)  # Пример размеров
print_matrix_dimensions(random_matrix)
print_matrix(random_matrix)
