def main():
    # 1
    abc = input("Введите строку: ")
    while abc:
        print(f"Длина строки: {len(abc)}")
        abc = input("Введите строку: ")

    # 2
    negative_numbers = 0
    number = float(input())
    while number < 36.6:
        if number < 0:
            negative_numbers += 1
        number = float(input())
    print(negative_numbers)

    # 3
    num1_max = num2_max = float('-inf')
    number = float(input("Введите число: "))
    while number < 1000:
        if number > num1_max:
            num2_max = num1_max
            num1_max = number
        elif number > num2_max:
            num2_max = number
        number = float(input("Введите число: "))
    print(f"Второй максимум = {num2_max}")

    # 4
    numbers = list(map(float, input("Введите числа через пробел: ").split()))
    min_number = min(numbers)
    print(f"Наименьшее число = {min_number}")

    # 5
    number = int(input("Введите число: "))
    while number:
        if number % 21 == 0:
            print("Караул!")
            break
        elif number % 3 == 0:
            print("Несчастливое")
        elif number % 7 == 0:
            print("Опасное")
        else:
            print(number)
        number = int(input("Введите число: "))

    # 6
    summa = sum(num for num in range(2, 10001) if all(num % i for i in range(2, int(num ** 0.5) + 1)))
    print(f"Сумма простых чисел: {summa}")

    # 7
    x, y, z = map(int, (input() for _ in range(3)))
    b_box = x * y * z
    s_boxes = sum(
        a * b * c for _ in range(int(input())) for a, b, c in ([int(input()) for _ in range(3)] for _ in range(1)))
    print("Да" if s_boxes <= b_box else "Нет")

    # 8
    min_word = input("Введите первое слово: ")
    word = input("Введите следующее слово (или 'стоп' для завершения): ")
    while word != "стоп":
        min_word = word if len(word) < len(min_word) else min_word
        word = input("Введите следующее слово (или 'стоп' для завершения): ")
    print(f"Самое короткое слово: {min_word}")

    # 9
    result = float(input("Введите число: "))
    operation = input("Введите операцию (+, -, *, /) или 'стоп' для завершения: ")
    while operation != "стоп":
        next_number = float(input("Введите следующее число: "))
        if operation == "+":
            result += next_number
        elif operation == "-":
            result -= next_number
        elif operation == "*":
            result *= next_number
        elif operation == "/":
            result /= next_number
        operation = input("Введите операцию (+, -, *, /) или 'стоп' для завершения: ")
    print("Результат работы: ", result)

    # Задание 10
    sentence = ""
    word = input()
    while word != "стоп":
        if sentence:
            sentence += " "
        sentence += word
        word = input()
    print(sentence) if sentence else None


if __name__ == "__main__":
    main()
