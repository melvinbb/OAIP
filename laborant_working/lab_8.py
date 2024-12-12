def main():


while True:
    try:
        num1 = int(input("Введите первое число: "))
        num2 = int(input("Введите второе число: "))
        break
    except ValueError:
        print("Ошибка: Введенные данные не являются целыми числами.")


try:
    sum_result = num1 + num2
    print(f"Результат сложения: {sum_result}")
    division_result = num1 / num2
    print(f"Результат деления: {division_result}")
except ZeroDivisionError:
    print("Ошибка: Деление на ноль!")
except Exception as e:
    print(f"Произошла неизвестная ошибка: {e}")


finally:
    print("Выход из программы")

if __name__ == "__main__":
    main()