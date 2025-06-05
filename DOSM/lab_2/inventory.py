def add(other):
    if not isinstance(other, Inventory):
        raise


class Inventory:
    def __init__(self, capacity):
        self._items = {}
        self._weight_limit = capacity
        self._current_weight = 0
        self._slots = capacity

    def __str__(self):
        return f"Inventory (capacity: {self._weight_limit}): {self._items}"
    def __iter__(self):
        return iter(self._items.items())
    def __len__(self):
        return sum(self._items.values())
    def __getitem__(self, key):
        return self._items.get(key, 0)
    def __setitem__(self, key, value):
        if value < 0:
            raise ValueError("Количество предметов не может быть отрицательным")

        current_item_count = self._items.get(key, 0)
        new_item_weight = value - current_item_count

        if self._current_weight + new_item_weight > self._weight_limit:
            raise ValueError("Превышение допустимого веса инвентаря")

        self._items[key] = value
        self._current_weight += new_item_weight
    def __delitem__(self, key):
        if key not in self._items:
            raise KeyError(f"Предмет '{key}' не найден в инвентаре")

        self._current_weight -= self._items[key]
        del self._items[key]
    def __contains__(self, item):
        return item in self._items
    def __add__(self, other):
        if not isinstance(other, Inventory):
            raise TypeError("Можно объединять только с объектом класса Inventory")

        for item, count in other._items.items():
            try:
                self[item] += count
            except ValueError as e:
                print(f"Превышение веса при добавлении предмета '{item}': {e}")

    def add(self, inventory2):
        pass


inventory1 = Inventory(20)
inventory1["stone"] = 5
inventory1["wood"] = 10

inventory2 = Inventory(15)
inventory2["wood"] = 3
inventory2["gold"] = 2

print(inventory1)
print(len(inventory1))

print("stone" in inventory1)

inventory1.add(inventory2)
print(inventory1)
try:
    inventory1["iron"] = 100
except ValueError as e:
    print(e)

for item, count in inventory1:
    print(f"{item}: {count}")

del inventory1["wood"]
print(inventory1)