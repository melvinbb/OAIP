import random


class Pet:
    def __init__(self, name):
        self.name = name
        self.hunger = 50
        self.sleepiness = 50
        self.happiness = 50
        self.health = 100
        self.age = 0

        print(f"Привет! меня зовут {self.name}!")

    def __str__(self):
        return (f"{self.name}:n"
                f" Возраст: {self.age}n"
                f" Голод: {self.hunger}n"
                f" Усталость: {self.sleepiness}n"
                f" Счастье: {self.happiness}n"
                f" Здоровье: {self.health}")

    def _update_stats(self):
        self.hunger += random.randint(-5, 10)
        self.sleepiness += random.randint(-5, 10)
        self.happiness += random.randint(-10, 5)
        self.age += 1 / 24
        self.hunger = max(0, min(self.hunger, 100))
        self.sleepiness = max(0, min(self.sleepiness, 100))
        self.happiness = max(0, min(self.happiness, 100))
        self.health -= (self.hunger / 20) + (self.sleepiness / 20) + (100 - self.happiness) / 10
        self.health = max(0, min(self.health, 100))

        if self.health <= 0:
            print(f"Увы, {self.name} умер...")
            return True

    def feed(self, food_quality=1):
        if not self._update_stats():
            return
        print(f"{self.name} ест...")
        self.hunger -= 20 * food_quality / 5
        self.happiness += 10 * food_quality / 5
        self.hunger = max(0, self.hunger)
        self.happiness = min(100, self.happiness)
        print(f"{self.name} выглядит довольным!")

    def play(self, play_time=1):
        if not self._update_stats():
            return
        print(f"Вы играете с {self.name}...")
        self.happiness += 15 * play_time / 5
        self.sleepiness += 10 * play_time / 5
        self.happiness = min(100, self.happiness)
        print(f"{self.name} весело проводит время!")

    def sleep(self, sleep_time=1):
        if not self._update_stats():
            print(f"{self.name} спит...")
            self.sleepiness -= 30 * sleep_time / 5
            self.hunger += 5 * sleep_time / 5
            self.sleepiness = max(0, self.sleepiness)
            self.hunger = min(100, self.hunger)
            print(f"{self.name} проснулся отдохнувшим!")

    def check_status(self):
        if not self._update_stats():
            return False
        print(self)
        return True
