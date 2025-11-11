from typing import Callable, Optional

class BUTTON:
    def __init__(self, label: str = "Кнопка", action: Optional[Callable[[], None]] = None):
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
            self.release()
        else:
            print(f"Кнопка '{self.label}' уже нажата.")

    def release(self):
        if self.is_pressed:
            self.is_pressed = False
            print(f"Кнопка '{self.label}' отпущена.")

    def set_label(self, new_label: str):
        self.label = new_label
        print(f"Надпись на кнопке изменена на '{self.label}'.")
