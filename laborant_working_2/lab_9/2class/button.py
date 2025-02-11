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
