class Material:
    def __init__(self, name, quantity, durability):
        self.name = name
        self._quantity = quantity
        self._durability = durability

    def __str__(self):
        return f"{self.name} (Количество: {self._quantity}, Прочность: {self._durability})"

    def get_name(self):
        return self._name

    def get_quantity(self):
        return self._quantity

    def set_durability(self):
        return self._durability

    def set_quantity(self, new_qunatity):
        if new_qunatity >= 0:
            self._quantity = new_qunatity
        else:
            self._quantity = 0
            print("Количество не может быть отрицательным. Установлено значение 0.")

    def set_durability1(self, new_durability):
        if new_durability >= 0:
            self._durability = new_durability
        else:
            self._durability = 0
            print("Прочность не может быть отрицательной. Установлено значение 0.")

    def info(self):
        base_info = super().info()
        return f"{base_info}\nТип дерева: {self._wood_type}"
