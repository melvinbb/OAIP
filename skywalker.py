def multiply_matrices(matrix1, matrix2):

    n = len(matrix1)

    # Проверка на соответствие размеров матриц
    if len(matrix2) != n or len(matrix1[0]) != n or len(matrix2[0]) != n:
        print("Ошибка: Матрицы должны быть квадратными и иметь одинаковый размер.")
        return None

    # Инициализация результирующей матрицы нулями
    result_matrix = [[0 for _ in range(n)] for _ in range(n)]

    # Основной алгоритм умножения матриц
    # Внешний цикл (i) проходит по строкам первой матрицы (matrix1).
    for i in range(n):
        # Средний цикл (j) проходит по столбцам второй матрицы (matrix2).
        for j in range(n):
            # Внутренний цикл (k) выполняет суммирование произведений элементов i-й строки matrix1 и j-го столбца matrix2.
            for k in range(n):
                result_matrix[i][j] += matrix1[i][k] * matrix2[k][j]

    return result_matrix


# Пример использования
if __name__ == "__main__":
    matrix_a = [
        [1, 2, 3],
        [4, 5, 6],
        [7, 8, 9]
    ]

    matrix_b = [
        [9, 8, 7],
        [6, 5, 4],
        [3, 2, 1]
    ]

    result = multiply_matrices(matrix_a, matrix_b)

    if result:
        print("Матрица A:")
        for row in matrix_a:
            print(row)

        print("\nМатрица B:")
        for row in matrix_b:
            print(row)

        print("\nРезультат умножения A * B:")
        for row in result:
            print(row)


