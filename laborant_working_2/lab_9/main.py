import time
from chest_class import Chest
from button_class import Button
from pet_class import Pet


def generic_button_action():
    print("-> [СОБЫТИЕ КНОПКИ]: Кнопка была нажата! Выполнено действие. <-\n")


def main():
    my_chest = Chest(capacity=5, password="123")
    my_button = Button(label="Главная Кнопка", action=generic_button_action)
    my_pet = Pet(name="Флаффи")

    while True:
        print("\n--- ГЛАВНОЕ МЕНЮ ---")
        print("1. Управлять Сундуком")
        print("2. Взаимодействовать с Кнопкой")
        print("3. Заботиться о Питомце")
        print("q. Выход из программы")

        choice = input("Выберите действие: ").strip().lower()

        if choice == '1':
            while True:
                print("\n--- МЕНЮ СУНДУКА ---")
                print(f"Сундук: {'открыт' if my_chest.is_open else 'закрыт'}")
                print(f"Содержимое: {', '.join(my_chest.items) if my_chest.items else 'пусто'}")
                print("1. Открыть сундук")
                print("2. Закрыть сундук")
                print("3. Запереть сундук (требуется пароль)")
                print("4. Отпереть сундук (требуется пароль)")
                print("5. Добавить предмет")
                print("6. Убрать предмет")
                print("b. Назад в главное меню")

                chest_choice = input("Что вы хотите сделать с сундуком?: ").strip().lower()

                if chest_choice == '1':
                    my_chest.open()
                elif chest_choice == '2':
                    my_chest.close()
                elif chest_choice == '3':
                    password_input = input("Введите пароль для запирания: ")
                    my_chest.lock(password_input)
                elif chest_choice == '4':
                    password_input = input("Введите пароль для отпирания: ")
                    my_chest.unlock(password_input)
                elif chest_choice == '5':
                    if my_chest.is_open:
                        item_name = input("Введите название предмета для добавления: ")
                        my_chest.add_item(item_name)
                    else:
                        print("Сундук закрыт. Сначала откройте его, чтобы добавить предмет.")
                elif chest_choice == '6':
                    if my_chest.is_open:
                        item_name = input("Введите название предмета для удаления: ")
                        my_chest.remove_item(item_name)
                    else:
                        print("Сундук закрыт. Сначала откройте его, чтобы убрать предмет.")
                elif chest_choice == 'b':
                    break
                else:
                    print("Неверный выбор. Попробуйте еще раз.")

        elif choice == '2':

            while True:
                print(f"\n--- МЕНЮ КНОПКИ: '{my_button.label}' ---")
                print(f"Статус: {'нажата' if my_button.is_pressed else 'отпущена'}.")
                print("1. Нажать кнопку")
                print("2. Изменить надпись кнопки")
                print("3. Отпустить кнопку")
                print("b. Назад в главное меню")

                button_choice = input("Что вы хотите сделать с кнопкой?: ").strip().lower()

                if button_choice == '1':
                    my_button.press()
                elif button_choice == '2':
                    new_label = input("Введите новую надпись для кнопки: ")
                    my_button.set_label(new_label)
                elif button_choice == '3':
                    my_button.release()
                elif button_choice == 'b':
                    break
                else:
                    print("Неверный выбор. Попробуйте еще раз.")

        elif choice == '3':

            while True:
                my_pet.get_status()
                print(f"\n--- МЕНЮ ПИТОМЦА: '{my_pet.name}' ---")
                print("1. Покормить")
                print("2. Поиграть")
                print("3. Уложить спать")
                print("b. Назад в главное меню")

                pet_choice = input(f"Что вы хотите сделать с {my_pet.name}?: ").strip().lower()

                if pet_choice == '1':
                    my_pet.feed()
                elif pet_choice == '2':
                    my_pet.play()
                elif pet_choice == '3':
                    my_pet.sleep()
                elif pet_choice == 'b':
                    break
                else:
                    print("Неверный выбор. Попробуйте еще раз.")
            time.sleep(0.5)

        elif choice == 'q':
            print("Выход из программы. До свидания!")
            break
        else:
            print("Неверный выбор в главном меню. Попробуйте еще раз.")


if __name__ == "__main__":
    main()
