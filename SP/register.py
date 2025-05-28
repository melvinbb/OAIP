from flags_register import FlagsRegister


class Register:
    def __init__(self, name="stack_register", size=32):
        self.name = name
        self.size = size
        self.value = [0] * size
        self.flags = FlagsRegister()

    # Устанавливает значение и обновляет флаги
    def set(self, value):
        value = value % (1 << self.size)
        if value >= 2 ** (self.size - 1):
            value -= 1 << self.size
        self.value = self._int_to_twos_complement(value)
        self._update_flags()

    # Возвращает текущее значение как целое число
    def get(self):
        return self._twos_complement_to_int(self.value)

    # Сложение с другим регистром
    def add(self, other):
        result = self.get() + other.get()
        self.set(result)
        self.flags.update(self.value, self.get(), other.get(), "add")

    # Вычитание другого регистра
    def sub(self, other):
        result = self.get() - other.get()
        self.set(result)
        self.flags.update(self.value, self.get(), other.get(), "sub")

    # Умножение на другой регистр
    def mul(self, other):
        result = self.get() * other.get()
        self.set(result)
        self.flags.update(self.value, 0, 0, "mul")

    # Деление на другой регистр
    def div(self, other):
        if other.get() == 0:
            raise ZeroDivisionError("Division by zero")
        result = self.get() // other.get()
        self.set(result)
        self.flags.update(self.value, 0, 0, "div")

    # Обновляет флаги zero и negative
    def _update_flags(self):
        int_value = self.get()
        self.flags.zero = int_value == 0
        self.flags.negative = int_value < 0

    def _int_to_twos_complement(self, value):
        if value < 0:
            value += (1 << self.size)
        return list(map(int, f"{value:0{self.size}b}"))

    def _twos_complement_to_int(self, bits):
        if bits[0] == 1:
            return -(2 ** (self.size - 1)) + int("".join(map(str, bits[1:])), 2)
        return int("".join(map(str, bits)), 2)

    def __repr__(self):
        return f"Register({self.name}, Value={self.get()}, Flags={self.flags.__dict__})"
