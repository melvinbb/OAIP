from abc import ABC, abstractmethod
class GameItem(ABC):
    def __init__(self, item_name, weight, rarity):
        self.item_name = item_name
        self.weight = weight
        self.rarity = rarity
    def use(self):
        pass
    def get_description(self):
        return f'{self.__class__.__name__}"{self.item_name}" (Редкость: {self.rarity}, Вес: {self.weight})'

class HealthPotion(GameItem):
    def __init__(self, item_name, weight, rarity):
        super().__init__(item_name, weight, rarity)
    def use(self):
        print(f'{self.get_description()} использовано: +50 HP')
    def get_description(self):
        return super().get_description()

class ManaCrystal(GameItem):
    def __init__(self, item_name, weight, rarity):
        super().__init__(item_name, weight, rarity)
    def use(self):
        print(f'{self.get_description()} использовано: +30 MP')
    def get_description(self):
        return super().get_description()

health_potion = HealthPotion("Большой флакон", 0.5, "Обычное")
mana_crystal = ManaCrystal("Синий осколок", 0.3, "Редкое")

health_potion.use()
mana_crystal.use()