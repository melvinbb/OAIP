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
        if elapsed > 10:
            self.hunger = min(10, self.hunger + int(elapsed / 10))
            self.happiness = max(0, self.happiness - int(elapsed / 10))
            self.energy = max(0, self.energy - int(elapsed / 15))
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
        print(f"Голод: {self.hunger}/10 {'(очень голоден!)' if self.hunger > 7 else ''}")
        print(f"Счастье: {self.happiness}/10 {'(грустит...) ' if self.happiness < 3 else ''}")
        print(f"Энергия: {self.energy}/10 {'(устал!)' if self.energy < 3 else ''}")
        print("---------------------------")


