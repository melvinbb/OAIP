import math

def template(a, b, c):
    p = a + b + c
    s = p / 2
    if s > a and s > b and s > c:
        print(f'Периметр = {p}')
        print(f'Площадь = {math.sqrt(s * (s - a) * (s - b) * (s - c))}')
        print(f'Равнобедренный = {"ДА" if a == b or b == c or a == c else "НЕТ"}')
        print(f'Равносторонний = {"ДА" if a == b == c else "НЕТ"}')
    else:
        print(None)
