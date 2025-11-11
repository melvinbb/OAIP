from chest_class import CHEST
from button_class import BUTTON
from pet_class import PET
import time

def main():

    print("=== Запуск===")
    print("\n--- Тестирование класса CHEST (Сундук) ---")
    my_chest = CHEST(capacity=3)
    my_chest.add_item("Золотой слиток")
    my_chest.open()
    my_chest.add_item("Золотой слиток")
    my_chest.add_item("Меч героя")
    my_chest.view_contents()
    my_chest.add_item("Щит доблести")
    my_chest.add_item("Зелье лечения")
    my_chest.close()
    my_chest.view_contents()

    print("\n--- Тестирование класса BUTTON (Кнопка) ---")
    def on_button_click():
        print("-> Выполнено действие при нажатии кнопки!")

    start_button = BUTTON(label="Старт", action=on_button_click)
    start_button.press()
    start_button.set_label("Начать игру")
    start_button.press()

    exit_button = BUTTON(label="Выход")
    exit_button.press()
    print("\n--- Тестирование класса PET (Питомец) ---")
    my_pet = PET(name="Борька", species="Мимик")
    my_pet.get_status()

    my_pet.feed()
    time.sleep(1)
    my_pet.play()
    time.sleep(2)
    my_pet.get_status()

    my_pet.feed()
    my_pet.sleep()
    time.sleep(3)
    my_pet.get_status()
    print("\n=== Завершение демонстрации ===")


if __name__ == "__main__":
    main()
