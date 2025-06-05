from pet import Pet


def main():
    my_pet = Pet("Васька")

    while True:
        print("\nЧто вы хотите сделать?")
        print("1. Покормить")
        print("2. Поиграть")
        print("3. Уложить спать")
        print("4. Проверить статус")
        print("5. Выйти")

        choice = input("> ")

        if choice == "1":
            quality = int(input("Качество еды (1-10): "))
            my_pet.feed(quality)
        elif choice == "2":
            time = int(input("Как долго играем (1-10): "))
            my_pet.play(time)
        elif choice == "4":
            if not my_pet.check_status():
                break
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный ввод.")


if __name__ == "__main__":
    main()
