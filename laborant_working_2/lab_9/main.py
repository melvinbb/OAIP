from chest_class import CHEST
from button_class import BUTTON
from pet_class import PET
import time


def main():

    print("=== Запуск интерактивной лабораторной работы №9: ООП: Абстракция ===")


    my_chest = CHEST(capacity=5, password="123")


    def generic_button_action():
        print("-> [СОБЫТИЕ КНОПКИ]: Кнопка была нажата! <-\n")

    my_button = BUTTON(label="Главная Кнопка", action=generic_button_action)
    my_pet = PET(name="Флаффи")

    while True:
        print("\n--- ГЛАВНОЕ МЕНЮ ---")
        print("1. Управлять Сундуком")
        print("2. Взаимодействовать с Кнопкой")
        print("3. Заботиться о Питомце")
        print("q. Выход из программы")

        choice = input("Выберите действие: ").strip().lower()

        if choice == '1':

            while True:
                my_chest.view_contents()
                print("\n--- МЕНЮ СУНДУКА ---")
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
                print("b. Назад в главное меню")

                button_choice = input("Что вы хотите сделать с кнопкой?: ").strip().lower()

                if button_choice == '1':
                    my_button.press()
                elif button_choice == '2':
                    new_label = input("Введите новую надпись для кнопки: ")
                    my_button.set_label(new_label)
                elif button_choice == 'b':
                    break
                else:
                    print("Неверный выбор. Попробуйте еще раз.")

        elif choice == '3':

            while True:
                my_pet.get_status()  #
                print("\n--- МЕНЮ ПИТОМЦА ---")
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
