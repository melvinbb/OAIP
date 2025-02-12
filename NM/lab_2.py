import math


def perimeter(n):
    if n == 2:
        return 2 * math.sqrt(2)
    else:
        p_prev = perimeter(n // 2)
        return 2 ** (n // 2 - 1) * math.sqrt(2 * (1 - math.sqrt(1 - (p_prev / 2 ** (n // 2 - 1)) ** 2)))


def perimeter_stable(n):
    if n == 2:
        return 2 * math.sqrt(2)
    else:
        p_prev = perimeter_stable(n // 2)
        return 2 ** (n // 2 - 1) * (p_prev / 2 ** (n // 2 - 1)) / math.sqrt(
            0.5 * (1 + math.sqrt(1 - (p_prev / 2 ** (n // 2 - 1)) ** 2)))


def calculate_pi_error(n, perimeter_func):
    calculated_perimeter = perimeter_func(2 ** n)
    pi_approximation = calculated_perimeter / 2 ** (n - 1)
    error = abs(math.pi - pi_approximation) / math.pi
    return pi_approximation, error


def print_results(start, end, perimeter_func, func_name):
    print(f"Результаты для {func_name}:")
    print("n\tПриближение pi\tОтносительная погрешность")
    for n in range(start, end + 1):
        pi_approx, error = calculate_pi_error(n, perimeter_func)
        print(f"{n}\t{pi_approx:.15f}\t{error:.15f}")
def perimeter_stable(n):
    if n == 2:
        return 2 * math.sqrt(2)
    else:
        p_prev = perimeter_stable(n//2)
        sides = 2**(n//2)

