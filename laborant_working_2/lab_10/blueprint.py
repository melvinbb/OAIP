class Blueprint:
    def __init__(self, name, recipe):
        self._name = name
        self._recipe = recipe

    def get_name(self):
        return self._name

    def get_recipe(self):
        return self._recipe

    def info(self):
        recipe_info = "\n".join([f"{material_name}: {quantity}"
                                 for material_name, quantity in
                                 self._recipe.items()])
        return f"Чертеж: {self._name}\nРецепт:\n{recipe_info}"
