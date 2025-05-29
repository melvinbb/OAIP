from flags_register import FlagsRegister


class Register:
    def __init__(self, name, size=32):
        self.name = name
        self.size = size
        self.value = [0] * size
        self.flags = FlagsRegister()

    def load(self, value):
        value = value % (1 << self.size)
        if value >= 2 **(self.size - 1):
            value -= 1 << self.size
        self.value = self._int_to_twos_complement(value)

    def to_int(self):
        return self._twos_complement_to_int(self.value)

    def add(self, other):
        operand1 = self.to_int()
        operand2 = other.to_int()
        result = operand1 + operand2
        self.load(result % (2 ** self.size))
        self.flags.update(self.value, operand1, operand2, "add")

    def sub(self, other):
        operand1 = self.to_int()
        operand2 = other.to_int()
        result = operand1 - operand2
        self.load(result % (2 ** self.size))
        self.flags.update(self.value, operand1, operand2, "sub")

    def mul(self, other):
        result = self.to_int() * other.to_int()
        self.load(result % (2 ** self.size))
        self.flags.update(self.value, 0, 0, "mul")

    def div(self, other):
        if other.to_int() == 0:
            raise ZeroDivisionError("Division by zero")
        result = self.to_int() // other.to_int()
        self.load(result % (2 ** self.size))
        self.flags.update(self.value, 0, 0, "div")

    def _int_to_twos_complement(self, value):
        if value < 0:
            value += (1 << self.size)
        return list(map(int, f"{value:0{self.size}b}"))

    def _twos_complement_to_int(self, bits):
        if bits[0] == 1:
            return -(2 ** (self.size - 1)) + int("".join(map(str, bits[1:])), 2)
        return int("".join(map(str, bits)), 2)

    def __repr__(self):
        return f"Register({self.name}, Value={self.to_int()}, Flags={self.flags.__dict__})"