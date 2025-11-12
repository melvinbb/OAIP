import time


class PET:
    def __init__(self, name: str = "Питомчик", species: str = "Тамагочи"):
        self.name = name
        self.species = species
        self.hunger = 5
        self.happiness = 7
        self.energy = 8
        print(f"Питомчик '{self.name}' ({self.species}) родился!")
        self._last_interaction_time = time.time()

    def _update_needs(self):
        elapsed = time.time() - self._last_interaction_time
        if elapsed > 5:
            hunger_increase = int(elapsed / 5)
            happiness_decrease = int(elapsed / 5)
            energy_decrease = int(elapsed / 7)

            self.hunger = min(10, self.hunger + hunger_increase)
            self.happiness = max(0, self.happiness - happiness_decrease)
            self.energy = max(0, self.energy - energy_decrease)
            self._last_interaction_time = time.time()

    def feed(self):
        self._update_needs()
        self.hunger = max(0, self.hunger - 4)
        self.happiness = min(10, self.happiness + 2)
        print(f"{self.name} покормлен. Мням-мням!")
        self.get_status()

    def play(self):
        self._update_needs()
        self.energy = max(0, self.energy - 3)
        self.happiness = min(10, self.happiness + 4)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} поиграл. Весело!")
        self.get_status()

    def sleep(self):
        self._update_needs()
        self.energy = min(10, self.energy + 5)
        self.happiness = min(10, self.happiness + 1)
        self.hunger = min(10, self.hunger + 1)
        print(f"{self.name} спит... Зззз.")
        self.get_status()

    def get_status(self):
        self._update_needs()
        print(f"\n--- Статус {self.name} ({self.species}) ---")
        print(
            f"Голод: {self.hunger}/10 {'(ОЧЕНЬ ГОЛОДЕН!)' if self.hunger >= 8 else '(голоден)' if self.hunger > 5 else '(сыт)'}")
        print(
            f"Счастье: {self.happiness}/10 {'(ОЧЕНЬ ГРУСТИТ!)' if self.happiness <= 2 else '(грустит)' if self.happiness < 5 else '(счастлив)'}")
        print(
            f"Энергия: {self.energy}/10 {'(ОЧЕНЬ УСТАЛ!)' if self.energy <= 2 else '(устал)' if self.energy < 5 else '(бодр)'}")
        print("---------------------------")
