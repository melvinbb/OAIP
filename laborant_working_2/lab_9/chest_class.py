class CHEST:
    def __init__(self, capacity: int):
        self.capacity = capacity
        self.items = []
        self.is_open = False
        print(f"Сундук создан с вместимостью {capacity}.")

    def open(self):
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

    def add_item(self, item: str):
        if self.is_open:
            if len(self.items) < self.capacity:
                self.items.append(item)
                print(f"В сундук добавлен предмет: {item}.")
            else:
                print(f"Сундук полон (вместимость {self.capacity}), нельзя добавить '{item}'.")
        else:
            print("Сундук закрыт, сначала откройте его.")

    def view_contents(self):
        if self.is_open:
            if self.items:
                print(f"Содержимое сундука: {', '.join(self.items)}.")
            else:
                print("Сундук пуст.")
        else:
            print("Сундук закрыт.")

