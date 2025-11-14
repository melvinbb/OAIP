class Button:
    def __init__(self, label="Кнопка", action=None):
        self.label = label
        self.is_pressed = False
        self._action = action
        print(f"Кнопка '{self.label}' создана.")

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
