def main():

#1
    input_string = input("Введите строку: ")
    if input_string == "Python":
        print("ДА")
    else:
        print("НЕТ")
#2
    string1 = input("Введите первую строку: ")
    string2 = input("Введите вторую строку: ")

    valid_strings = ["да", "нет"]

    if (string1 in valid_strings) and (string2 in valid_strings):
        print("ВЕРНО")
    else:
        print("НЕВЕРНО")
#3
    one = input()
    two = input()
    three = input()

    if one in ('1', 'раз') and two in ('2', 'два') and three in ('3', 'три'):
        print('ГОРИ')
    else:
        print('НЕ ГОРИ')

#4
    city_1 = input()
    city_2 = input()
    if (((city_1 == 'Тула' and city_2 != 'Пенза' or city_1 != 'Тула' and city_2 == 'Пенза'
        or(city_2 == 'Пенза' or city_1 == 'Пенза') or (city_2 == 'Тула' or city_1 == 'Тула')
            and city_1 != city_2))):
        print('ДА')
    else:
        print('НЕТ')
#5
    n = int(input("Введите количество километров в марафоне (n): "))
    m = int(input("Введите расстояние, которое спортсмен пробегает за день (m): "))

    if n % m == 0:
        days = n // m
    else:
        days = (n // m) + 1

    print("Спортсмен добежит до финиша на день:", days)
#6
    number = int(input())

    first_digit = number // 100
    third_digit = number % 10
    middle_digit = (number // 10) % 10

    sum_of_digits = first_digit + third_digit

    if sum_of_digits % 8 != 0 and middle_digit == 3:
        print("Подходит")
    else:
        print(sum_of_digits, middle_digit)
#7
    category = input("Категория: ")

    if category.lower() == "продукты":
        price = float(input("Цена: "))
        if price < 100:
            print("Попробуйте нашу выпечку!")
        elif 100 <= price < 500:
            print("Как насчёт орехов в шоколаде?")
        else:
            print("Попробуйте экзотические фрукты!")
    else:
        print("Загляните в товары для дома!")
#8

    prices_str = input("Введите цены через пробел: ").split()
    prices = [float(p) for p in prices_str]

    if prices == sorted(prices):
      total = sum(prices) / 2
      print("Акция!\nК оплате:", f"{total:.2f}")
    elif prices == sorted(prices, reverse=True):
      total = sum(prices) / 3
      print("Акция!\nК оплате:", f"{total:.2f}")
    else:
      total = sum(prices)
      print("К оплате:", f"{total:.2f}")

#9
    n1 = int(input("Введите количество посетителей вчера: "))
    n2 = int(input("Введите количество посетителей позавчера: "))

    visitors = n2 + abs(n1 - n2)

    print(f'Сегодня магазин посетит: {visitors} человек')


#10
    year = int(input("Введите год: "))

    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        print(year, "високосный")
    else:
        print(year, "не високосный")
#11
    number = int(input("Введите целое число: "))

    if number % 2 == 0:
        print(number, " - четное число")
    else:
        print(number, " - нечетное число")

if __name__ == "__main__":
    main()