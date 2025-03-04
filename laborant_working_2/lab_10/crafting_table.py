class CraftingTable:
    def __init__(self, name):
        self.name = name
        self._inventory = name

    def add_material(self, material):
        if material.get_name() in self._inventory:
            self._inventory[material.get_name()].set_quantity(self._inventory[material.get_name()].get_quantity() +
                                                              material.get_quantity())
        else:
            self._inventory[material.get_name()] = material
            print(f"{material.get_quantity()}{material.get_name()} добавлено в верстак.")

    def craft_item(self, blueprint):
        recipe = blueprint.get_recipe()
        for material_name, required_quantity in recipe.item():
            if material_name not in self._inventory or self._inventory[material_name].get_quantity() < \
                    required_quantity:
                print(f"Недостаточно материалов для создания {blueprint.get_name()}.")
                return None
        for material_name, required_quantity in recipe.items():
            self._inventory[material_name].set_quantity(self._inventory[material_name].get_quantity() -
                                                        required_quantity)
            components.append(self._inventory[material_name])
            item = Item(blueprint.get_name(), components, durability=100)
            print(f"{blueprint.get_name()} успешно создан!")
            return item

            components = []

    def get_inventory(self):
        return self._inventory
