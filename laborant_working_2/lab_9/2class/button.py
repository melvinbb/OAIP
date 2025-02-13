class Button:
    def __init__(self, text, width, height, color, action=""):
        self.text = text
        self.width = width
        self.height = height
        self.color = color
        self.action = action
        self.is_enabled = True

    def click(self):
        if self.is_enabled:
            return f"Кнопка '{self.text}' нажата. Выполняется действие: {self.action}"
        else:
            return f"Кнопка '{self.text}' неактивна. Нажатие невозможно."

    def disable(self):
        if not self.is_enabled:
            self.is_enabled = False
            return f"Кнопка '{self.text}' деактивирована."
        else:
            return f"Кнопка '{self.text}' уже неактивна."

    def enable(self):
        if not self.is_enabled:
            self.is_enabled = True
            return f"Кнопка '{self.text}' активирована."
        else:
            return f"Кнопка '{self.text}' уже активна."

    def display_info(self):
        return f"Кнопка: Текст='{self.text}', Ширина={self.width}, Высота={self.height}, Цвет={self.color}, Действие='{self.action}', Активна'={self.is_enabled}"
