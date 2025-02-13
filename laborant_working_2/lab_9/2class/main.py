from button import Button


def main():
    my_button = Button(text="Click Me!", width=100, height=30, color="blue", action="Submit form")
    print("Добро пожаловать в эмулятор кнопки!")
    while True:
        print("1. Нажать кнопку")
        print("2. Деактивировать кнопку")
        print("3. Активировать кнопку")
        print("4. Посмотреть информацию о кнопке")
        print("5. Выйти")

        choice = input("> ")

        if choice == "1":
            print(my_button.click())
        elif choice == "2":
            print(my_button.disable())
        elif choice == "3":
            print(my_button.enable())
        elif choice == "4":
            print(my_button.display_info())
        elif choice == "5":
            print("До свидания")
            break

        else:
            print("Неверный ввод. Пожалуйста, выберите один из предложенных вариантов.")


if __name__ == "__main__":
    main()
