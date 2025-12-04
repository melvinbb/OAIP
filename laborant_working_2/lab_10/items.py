

class Item:
    def __init__(self, name, durability):
        self.name = name
        self.durability = durability

    def info(self):
        return f"Предмет: {self.name}, Прочность: {self.durability}"


class Sword(Item):
    def __init__(self, name, damage, durability):

        super().__init__(name, durability)
        self.damage = damage

    def info(self):
        # Переопределяем info для отображения урона меча
        return f"Меч: {self.name}, Урон: {self.damage}, Прочность: {self.durability}"


class StoneSword(Sword):
    def __init__(self):
        super().__init__('Каменный Меч', 5, 100)  # Имя, Урон, Прочность


class IronSword(Sword):
    def __init__(self):
        super().__init__('Железный Меч', 7, 200)


class DiamondSword(Sword):
    def __init__(self):
        super().__init__('Алмазный Меч', 10, 1000)
