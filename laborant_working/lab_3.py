def main():

#1
    input_lines = []

    while True:
        line = input("Введите строку (или нажмите Enter для завершения): ")
        if line == "":
            break
        input_lines.append(line)

    print("\nДлины введённых строк:")
    for line in input_lines:
        print(f'"{line}" - {len(line)} символов')

#2
    negative_count = 0

    while True:
        try:
            number = float(input("Введите вещественное число (или число > 36.6 для завершения): "))

            if number > 36.6:
                break

            if number < 0:
                negative_count += 1

        except ValueError:
            print("Пожалуйста, введите корректное вещественное число.")


    print(negative_count)

#3
    numbers = []

    while True:
        number_input = input("Введите число (или число, по модулю не меньше 1000 для завершения): ")

        try:
            number = float(number_input)
        except ValueError:
            print("Пожалуйста, введите корректное число.")
            continue


        if abs(number) >= 1000:
            break

        numbers.append(number)

    if len(numbers) < 2:
        print("Недостаточно чисел для определения второго максимума.")
    else:

        unique_numbers = list(set(numbers))
        unique_numbers.sort()

        if len(unique_numbers) < 2:
            print("Недостаточно уникальных чисел для определения второго максимума.")
        else:

            second_max = unique_numbers[-2]
            print(f"Второй максимум: {second_max}")

#4
    user_input = input("Введите числа через пробел: ")

    numbers = [float(num) for num in user_input.split()]

    if not numbers:
        print("Вы не ввели ни одного числа.")
    else:

        smallest = numbers[0]

        for num in numbers[1:]:

            if num < smallest:
                smallest = num

        print(f"Наименьшее число: {smallest}")

#5
    while True:

        number = int(input("Введите число (0 для выхода): "))

        if number == 0:
            break

        if number % 3 == 0 and number % 7 == 0:
            print("Караул!")
            break
        elif number % 3 == 0:
            print("Несчастливое число.")
        elif number % 7 == 0:
            print("Опасное число.")
        else:
            print(number)

#6
    total = 0

    for n in range(2, 10001):
        is_prime = True
        for i in range(2, int(n**0.5) + 1):
            if n % i == 0:
                is_prime = False
                break
        if is_prime:
            total += n

    print("Сумма всех простых чисел от 1 до 10000:", total)

#7
    x, y, z = map(int, input("Введите ширину, длину и высоту большой коробки (x, y, z): ").split())

    total_volume_small_boxes = 0

    while True:

        dimensions = input("Введите ширину, длину и высоту маленькой коробки (или 0 для выхода): ")
        w, l, h = map(int, dimensions.split())

        if w == 0 and l == 0 and h == 0:
            break

        total_volume_small_boxes += w * l * h

    volume_large_box = x * y * z

    if total_volume_small_boxes <= volume_large_box:
        print("Да")
    else:
        print("Нет")

#8
    shortest_word = None

    while True:
        word = input("Введите слово (или 'стоп' для завершения): ")

        if word == "стоп":
            break

        if shortest_word is None or len(word) < len(shortest_word):
            shortest_word = word

    if shortest_word is not None:
        print("Самое короткое слово:", shortest_word)
    else:
        print("Не было введено ни одного слова.")

#9
    result = None

    while True:
        input_value = input("Введите число или операцию (+, -, *, /) (или 'стоп' для завершения): ")

        if input_value.lower() == "стоп":
            break

        try:
            num = float(input_value)

            if result is None:
                result = num
            else:
                print("Текущий результат:", result)
                operation = input("Введите операцию (+, -, *, /): ")

                if operation == "+":
                    result += num
                elif operation == "-":
                    result -= num
                elif operation == "*":
                    result *= num
                elif operation == "/":
                    if num != 0:
                        result /= num
                    else:
                        print("Ошибка: деление на ноль.")
                else:
                    print("Неизвестная операция.")

        except ValueError:
            print("Ошибка: это не число. Попробуйте еще раз.")

    if result is not None:
        print("Конечный результат:", result)
    else:
        print("Не было введено ни одного числа.")

#10
    sentences = []
    current_sentence = []

    while True:
        word = input("Введите слово (или 'стоп' для завершения): ")

        if word.lower() == "стоп":

            break

        current_sentence.append(word)


        if word == "!":

            if current_sentence[:-1]:
                sentences.append(" ".join(current_sentence[:-1]) + "!")
            current_sentence = []

    if current_sentence:
        sentences.append(" ".join(current_sentence))

    for sentence in sentences:
        print(sentence)

if __name__ == "__main__":
    main()