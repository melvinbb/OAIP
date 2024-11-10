def main():
    # 1.
    movie = input("Введите название фильма: ")
    cinema = input("Введите название кинотеатра: ")
    time = input("Введите время сеанса: ")
    print(f'Билет на "{movie}" в "{cinema}" на {time} забронирован.')

    # 2.
    salary = int(input("Зарплата за месяц: \n>>> "))
    opening_hours = int(input("Количество отработанных в выходные часов: \n>>> "))
    prize = salary * 0.01 * opening_hours
    print(f"Размер премии: {prize}")

    # 3.
    n = int(input('Введите сумму:\n>>> '))
    thousands = n // 1000
    hundreds = (n % 1000) // 100
    tens = (n % 100) // 10
    ones = (n % 10) // 1
    print(ones, '- по 1р')
    print(tens, '- по 10р')
    print(hundreds, '- по 100р')
    print(thousands, '- по 1000р')

    # 4.
    review = input("Оцените развлекательный комплекс: \n>>> ")
    keywords = ["весело", "увлекательно", "развлечения"]
    result = [review.find(keyword) for keyword in keywords]
    print("Результат анализа:", *result, sep=' ')

    # 5.
    text = input('Введите слово: ')
    middle_index = len(text) // 2
    if len(text) % 2 == 0:
        print(f'Средние буквы: {text[middle_index - 1]}')
    else:
        print(f'Средняя буква: {text[middle_index]}')

    # 6.
    feedback = 'Алиса и Вася, большое спасибо за теплый приём!'
    name1 = feedback[:5]
    name2 = feedback[8:12]
    print(f'Назначить премию: {name1}/{name2}')

    # 7.
    alphabet = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
    number = int(input("Введите номер буквы английского алфавита: "))
    if 1 <= number <= len(alphabet):
        letter_index = number - 1
        print(alphabet[letter_index:letter_index + 4])
    else:
        print("Введите номер от 1 до 26.")

    # 8.
    my_list = []
    print("Созданный список:", my_list)
    my_list.append(1)
    my_list.append(2)
    print("Список после добавления элементов:", my_list)
    my_list.remove(1)
    print("Список после удаления элемента:", my_list)
    sliced_list = my_list[0:2]
    print("Срез списка:", sliced_list)
    my_list.reverse()
    print("Перевернутый список (метод reverse):", my_list)
    reversed_list = my_list[::-1]
    print("Перевернутый список (срез):", reversed_list)
    two_dimensional_list = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    print("Двумерный список:", two_dimensional_list)
    element = two_dimensional_list[1][2]
    print("Элемент на позиции [1] [2] :", element)
    my_list.clear()
    print("Список после очистки:", my_list)

    # 9.
    empty_tuple = ()
    print("Пустой кортеж:", empty_tuple)
    filled_tuple = (1, 2, 3, 'a', 'b', 'c')
    print("Заполненный кортеж:", filled_tuple)

    # 10.
    empty_set = set()
    print("Пустое множество:", empty_set)
    filled_set = {1, 2, 3, 'a', 'b', 'c'}
    print("Множество с элементами:", filled_set)
    empty_set.add(1)
    empty_set.add(2)
    empty_set.add('a')
    print("Множество после добавления элементов:", empty_set)
    set_a = {1, 2, 3}
    set_b = {3, 4, 5}
    union_set = set_a | set_b
    print("Объединение:", union_set)
    intersection_set = set_a & set_b
    print("Пересечение:", intersection_set)
    difference_set = set_a - set_b
    print("Разность (set_a - set_b):", difference_set)
    symmetric_difference_set = set_a ^ set_b
    print("Симметричная разность:", symmetric_difference_set)

    # 11.
    empty_dict = {}
    print("Пустой словарь:", empty_dict)
    filled_dict = {
        'name': 'Alice',
        'age': 25,
        'city': 'Moscow'
    }
    print("Словарь с элементами:", filled_dict)
    filled_dict['country'] = 'Russia'
    print("Словарь после добавления значения:", filled_dict)
    del filled_dict['age']
    print("Словарь после удаления значения:", filled_dict)
    filled_dict['city'] = 'Saint Petersburg'
    print("Словарь после изменения значения:", filled_dict)


if __name__ == "__main__":
    main()