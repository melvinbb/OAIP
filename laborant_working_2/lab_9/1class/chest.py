class Chest:
    def __init__(self, name, description, is_locked):
        self.name = name
        self.description = description
        self.is_locked = is_locked
        self.items = []

    def unlock_chest(self, key):
        if self.is_locked and key == "magic_key":
            self.is_locked = False
            return "Сундук открыт!"
        elif self.is_locked:
            return "Неверный ключ"
        else:
            return "Сундук уже открыт."

    def open_chest(self):
        if not self.is_locked:
            if not self.items:
                return "Сундук пуст."
            else:
                contents = "В сундуке:\n"
                for item in self.items:
                    contents += f"- {item}\n"
                return contents
        else:
            return "Сундук заперт. Сначала откройте его!"

    def add_item(self, item):
        self.items.append(item)
        return f"{item} добавлен в сундук."

    def take_item(self, item):
        if not self.is_locked:
            if item in self.items:
                self.items.remove(item)
                return f"{item} взят из сундука."
            else:
                return f"Предмет '{item}' не найден в сундуке."
        else:
            return "Сундук заперт. Нельзя взять предмет."

    def display_contents(self):
        print(self.open_chest())
