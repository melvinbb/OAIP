class Button:

    def __init__(self, label="Кнопка", action=None, x=0, y=0, width=100, height=50):
        self.label = label
        self.is_pressed = False
        self._action = action
        self.x = x
        self.y = y
        self.width = width
        self.height = height

        print(f"Кнопка '{self.label}' создана. "
              f"Позиция: ({self.x}, {self.y}), "
              f"Размер: {self.width}x{self.height}.")

    def press(self):
        if not self.is_pressed:
            self.is_pressed = True
            print(f"Кнопка '{self.label}' нажата.")
            if self._action:
                self._action()
        else:
            print(f"Кнопка '{self.label}' уже нажата.")

    def release(self):
        if self.is_pressed:
            self.is_pressed = False
            print(f"Кнопка '{self.label}' отпущена.")
        else:
            print(f"Кнопка '{self.label}' уже отпущена.")

    def set_label(self, new_label):
        self.label = new_label
        print(f"Надпись на кнопке изменена на '{self.label}'.")

    def set_position(self, new_x, new_y):
        self.x = new_x
        self.y = new_y
        print(f"Позиция кнопки '{self.label}' изменена на ({self.x}, {self.y}).")

    def set_size(self, new_width, new_height):
        if new_width > 0 and new_height > 0:
            self.width = new_width
            self.height = new_height
            print(f"Размер кнопки '{self.label}' изменен на {self.width}x{self.height}.")
        else:
            print("Ошибка: Ширина и высота должны быть положительными числами.")

    def get_info(self):
        return (f"Кнопка '{self.label}':\n"
                f"  Состояние: {'нажата' if self.is_pressed else 'отпущена'}\n"
                f"  Позиция: ({self.x}, {self.y})\n"
                f"  Размер: {self.width}x{self.height}")
