class Chest:
    def __init__(self, capacity: int, password: str = None):
        self.capacity = capacity
        self.items = []
        self.is_open = False
        self.is_locked = False
        self._password = password
        print(f"Сундук создан с вместимостью {capacity}.")
        if self._password:
            self.is_locked = True
            print("Сундук автоматически заперт паролем.")

    def open(self):
        if self.is_locked:
            print("Сундук заперт. Сначала его нужно отпереть.")
            return
        if not self.is_open:
            self.is_open = True
            print("Сундук открыт.")
        else:
            print("Сундук уже открыт.")

    def close(self):
        if self.is_open:
            self.is_open = False
            print("Сундук закрыт.")
        else:
            print("Сундук уже закрыт.")

    def lock(self, entered_password: str):
        if not self._password:
            print("У этого сундука нет пароля для запирания. Установите пароль при создании.")
            return

        if self.is_open:
            print("Нельзя запереть открытый сундук. Сначала закройте его.")
            return

        if self.is_locked:
            print("Сундук уже заперт.")
            return

        if entered_password == self._password:
            self.is_locked = True
            print("Сундук успешно заперт.")
        else:
            print("Неверный пароль. Сундук не заперт.")

    def unlock(self, entered_password: str):
        if not self._password:
            print("У этого сундука нет пароля. Он не может быть заперт.")
            return

        if not self.is_locked:
            print("Сундук не заперт.")
            return

        if entered_password == self._password:
            self.is_locked = False
            print("Сундук успешно отперт.")
        else:
            print("Неверный пароль. Сундук остался заперт.")

    def add_item(self, item: str):
        if self.is_open:
            if len(self.items) < self.capacity:
                self.items.append(item)
                print(f"В сундук добавлен предмет: {item}.")
            else:
                print(f"Сундук полон (вместимость {self.capacity}), нельзя добавить '{item}'.")
        else:
            print("Сундук закрыт, сначала откройте его.")

    def remove_item(self, item: str):
        if self.is_open:
            if item in self.items:
                self.items.remove(item)
                print(f"Из сундука убран предмет: {item}.")
            else:
                print(f"Предмета '{item}' нет в сундуке.")
        else:
            print("Сундук закрыт, сначала откройте его.")

    def view_contents(self):
        print(f"\n--- Сундук (Вместимость: {self.capacity}) ---")
        print(f"Статус: {'Открыт' if self.is_open else 'Закрыт'}, {'Заперт' if self.is_locked else 'Не заперт'}.")
        if self.is_open and self.items:
            print(f"Содержимое: {', '.join(self.items)}.")
        elif self.is_open and not self.items:
            print("Сундук пуст.")
        elif not self.is_open:
            print("Сундук закрыт.")
        print("---------------------------")
