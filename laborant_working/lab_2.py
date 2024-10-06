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
    string1 = input("Введите первую строку: ")
    string2 = input("Введите вторую строку: ")
    string3 = input("Введите третью строку: ")

    if (string1 in ["раз", "1"] and
            string2 in ["два", "2"] and
            string3 in ["три", "3"]):
        print("ГОРИ")
    else:
        print("НЕ ГОРИ")
#4
    july_city = input("Введите город в июле: ")
    august_city = input("Введите город в августе: ")

    if (july_city == "Тула" and august_city != "Пенза") or (august_city == "Пенза" and july_city != "Тула"):
        print("ДА")
    else:
        print("НЕТ")
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
        elif price >= 100 and price < 500:
            print("Как насчёт орехов в шоколаде?")
        else:
            print("Попробуйте экзотические фрукты!")
    else:
        print("Загляните в товары для дома!")
#8
    price1 = float(input("Цена первого товара: >>> "))
    price2 = float(input("Цена второго товара: >>> "))
    price3 = float(input("Цена третьего товара: >>> "))

    total_price = price1 + price2 + price3

    if (price1 < price2 < price3) or (price1 > price2 > price3):
        print("Акция!")
    if (price1 < price2 < price3):
        total_price /= 2
    else:
        total_price /= 3

    print("К оплате:", total_price)
#9
    buyers_before_yesterday = int(input("Введите число покупателей за позавчера: >>> "))
    buyers_yesterday = int(input("Введите число покупателей за вчера: >>> "))

    difference = buyers_yesterday - buyers_before_yesterday

    if difference > 0:
         buyers_today = buyers_yesterday + difference
    else:
        buyers_today = buyers_yesterday - difference

    print("Сегодня магазин посетит:", buyers_today, "человек")
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