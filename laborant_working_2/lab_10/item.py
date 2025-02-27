class Item:
    def __init__(self, name, components, durability):
        self._name = name
        self._components = components
        self._durability = durability

    def __str__(self):
        return f"{self._name} (Прочность: {self._durability})"

    def get_name(self):
        return self._name

    def get_components(self):
        return self._components

    def get_durability(self):
        return self._durability

    def set_durability(self, new_durability):
        if new_durability >= 0:
            self._durability = new_durability
        else:
            self._durability = 0
            print("Прочность не может быть отрицательной. Установлено значение 0.")

    def info(self):
        component_info = "\n".join([material.info() for material in self._components])
        return f"Предмет: {self._name}\nПрочность: {self._durability}\nКомпоненты:\n{component_info}"

    def upgrade(self, material):
        if ininstance(material.Material):
            self._components.append(material)
            self._durability += material.get_durability()
            print(f"{self._name} улучшен с помощью {material.get_name()}. Новая прочность: {self._durability}")

