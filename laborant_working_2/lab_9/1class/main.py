from chest import Chest


def main():
    treasure_chest = Chest("Старинный дубовый сундук", "Покрыт резьбой и темным лаком.", True)

    print(f"Вы видите {treasure_chest.name}.{treasure_chest.description}")

    while True:
        print("\nЧто вы хотите сделать?")
        print("1. Попытаться открыть сундук")
        print("2. Посмотреть содержимое сундука")
        print("3. Добавить предмет в сундук")
        print("4. Взять предмет из сундука")
        print("5. Выйти")

        choice = input("> ")

        if choice == "1":
            key = input("Введите ключ: ")
            print(treasure_chest.unlock_chest(key))
        elif choice == "2":
            print(treasure_chest.open_chest())
        elif choice == "3":
            item = input("Введите название предмета: ")
            print(treasure_chest.add_item(item))
        elif choice == "4":
            item = input("Какой предмет вы хотите взять? ")
            print(treasure_chest.take_item(item))
        elif choice == "5":
            print("До свидания!")
            break
        else:
            print("Неверный ввод. Пожалуйста, выберите один из предложенных вариантов.")


if __name__ == "__main__":
    main()
