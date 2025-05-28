from register import Register


class StackOverflow(Exception):
    # Исключение при переполнении стека
    pass


class StackUnderflow(Exception):
    # Исключение при попытке извлечь из пустого стека
    pass


class Stack:
    def __init__(self, size=8):
        # Инициализация стека с указанным размером (8 по умл)
        self.registers = [Register() for _ in range(size)]
        self.size = size
        self.sp = 0  # Указатель на следующую свободную позицию

    def push(self, value):
        # Добавляет значение на вершину стека
        if self.is_full():
            raise StackOverflow("Stack overflow")

        self.registers[self.sp].set(value)
        self.sp += 1

    def pop(self):
        # Извлекает значение с вершины стека
        if self.is_empty():
            raise StackUnderflow("Stack underflow")

        self.sp -= 1
        value = self.registers[self.sp].get()
        return value

    def is_empty(self):
        # Проверяет пуст ли стек
        return self.sp == 0

    def is_full(self):
        # Проверяет заполнен ли стек
        return self.sp == self.size

    def clear(self):
        # Очищает стек сбрасывая указатель и регистры
        self.sp = 0
        for reg in self.registers:
            reg.set(0)

    def __repr__(self):
        return f"Stack(sp={self.sp}, registers={self.registers})"
