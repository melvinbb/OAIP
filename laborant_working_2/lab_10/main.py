from resources import *
from items import *


class EnchantedStoneSword(Sword):
    def __init__(self):
        super().__init__('Зачарованный Каменный Меч', 6, 150)
        self.enchantment_level = 1

    def info(self):
        base_info = super().info()
        return f"{base_info.replace('Меч: Каменный Меч', 'Меч: Зачарованный Каменный Меч')} (Уровень {self.enchantment_level})"


class EnchantedIronSword(Sword):
    def __init__(self):
        super().__init__('Зачарованный Железный Меч', 8, 300)
        self.enchantment_level = 1

    def info(self):
        base_info = super().info()
        return f"{base_info.replace('Меч: Железный Меч', 'Меч: Зачарованный Железный Меч')} (Уровень {self.enchantment_level})"


class EnchantedDiamondSword(Sword):
    def __init__(self):
        super().__init__('Зачарованный Алмазный Меч', 11, 2000)
        self.enchantment_level = 1

    def info(self):
        base_info = super().info()
        return f"{base_info.replace('Меч: Алмазный Меч', 'Меч: Зачарованный Алмазный Меч')} (Уровень {self.enchantment_level})"


# ===============================================


class CraftingTable:
    def __init__(self):
        self.__resources = {
            'stick': 0,
            'stone': 0,
            'iron': 0,
            'diamond': 0
        }
        self.__crafting_recipes = {
            'stone_sword': {'stick': 1, 'stone': 2},
            'iron_sword': {'stick': 1, 'iron': 2},
            'diamond_sword': {'stick': 1, 'diamond': 2}
        }

        self.__crafting_classes = {
            'stone_sword': StoneSword,
            'iron_sword': IronSword,
            'diamond_sword': DiamondSword
        }

        self.__crafting_recipes['enchanted_stone_sword'] = {'stick': 1, 'stone': 2, 'diamond': 1}
        self.__crafting_recipes['enchanted_iron_sword'] = {'stick': 1, 'iron': 2, 'diamond': 1}
        self.__crafting_recipes['enchanted_diamond_sword'] = {'stick': 1, 'diamond': 2, 'diamond': 1}

        self.__crafting_classes['enchanted_stone_sword'] = EnchantedStoneSword
        self.__crafting_classes['enchanted_iron_sword'] = EnchantedIronSword
        self.__crafting_classes['enchanted_diamond_sword'] = EnchantedDiamondSword

        self.__disassembly_recipes = {
            'stone_sword': {'stick': 1, 'stone': 2},
            'iron_sword': {'stick': 1, 'iron': 2},
            'diamond_sword': {'stick': 1, 'diamond': 2},
            'enchanted_stone_sword': {'stick': 1, 'stone': 2, 'diamond': 1},
            'enchanted_iron_sword': {'stick': 1, 'iron': 2, 'diamond': 1},
            'enchanted_diamond_sword': {'stick': 1, 'diamond': 2, 'diamond': 1}
        }

        self.__item_class_to_name_map = {
            StoneSword: 'stone_sword', IronSword: 'iron_sword', DiamondSword: 'diamond_sword',
            EnchantedStoneSword: 'enchanted_stone_sword', EnchantedIronSword: 'enchanted_iron_sword',
            EnchantedDiamondSword: 'enchanted_diamond_sword'
        }
        # -----------------------------------------------

    def add_resource(self, resource):
        if isinstance(resource, Stick):
            self.__resources['stick'] += resource.get_amount()
        elif isinstance(resource, Stone):
            self.__resources['stone'] += resource.get_amount()
        elif isinstance(resource, Iron):
            self.__resources['iron'] += resource.get_amount()
        elif isinstance(resource, Diamond):
            self.__resources['diamond'] += resource.get_amount()
        else:
            print(f">> Неизвестный тип ресурса: {type(resource).__name__} <<")

    def craft_item(self, item):
        if item in self.__crafting_recipes:
            recipe = self.__crafting_recipes[item]
            for resource, amount in recipe.items():
                if self.__resources[resource] < amount:
                    print(f">> Недостаточно ресурсов для крафта {item.replace('_', ' ').capitalize()}. <<")
                    return None
            for resource, amount in recipe.items():
                self.__resources[resource] -= amount
            crafted_item_class = self.__crafting_classes[item]
            return crafted_item_class()
        else:
            print(f">> Рецепт для {item} не найден. <<")
            return None

    def disassemble_item(self, item_to_disassemble):
        item_class = type(item_to_disassemble)
        if item_class in self.__item_class_to_name_map:
            item_name = self.__item_class_to_name_map[item_class]
            if item_name in self.__disassembly_recipes:
                recipe = self.__disassembly_recipes[item_name]
                print(f">> Разбор {item_name.replace('_', ' ').capitalize()}... <<")
                gained_resources = {}
                for resource, amount in recipe.items():
                    self.__resources[resource] += amount
                    gained_resources[resource] = amount
                print(f">> Получены ресурсы: {', '.join(f'{v} {k}' for k, v in gained_resources.items())} <<")
                return gained_resources
            else:
                print(f">> Рецепт разбора для {item_name.replace('_', ' ').capitalize()} не найден. <<")
                return None
        else:
            print(f">> Неизвестный предмет для разбора. <<")
            return None

    def info(self):
        output = '\n'
        for key, value in self.__resources.items():
            if key == 'stick':
                output += f'> {"Палка"}: {value}\n'
            elif key == 'stone':
                output += f'> {"Камень"}: {value}\n'
            elif key == 'iron':
                output += f'> {"Железо"}: {value}\n'
            elif key == 'diamond':
                output += f'> {"Алмаз"}: {value}\n'
        return f">> Ресурсы на столе крафта << {output}"


def print_crafting_result(item_instance, item_name_key):
    if item_instance:
        print(item_instance.info())
    else:
        print(f'>> Крафт {item_name_key.replace("_", " ").capitalize()} не получился <<')
    return item_instance


def attempt_craft(table, item_key):
    print(f"\n--- Попытка крафта '{item_key.replace('_', ' ').capitalize()}' ---")
    item = table.craft_item(item_key)
    return print_crafting_result(item, item_key)


def attempt_disassemble(table, item_object):
    if item_object:
        print(f"\n--- Попытка разобрать '{item_object.name}' ---")
        table.disassemble_item(item_object)
    else:
        print("--- Нечего разбирать (предмет не был создан). ---")


def display_current_resources(table, header=""):
    print(f"\n{header}" if header else "")
    print(table.info())
    print("-" * 40)


if __name__ == "__main__":
    crafting_table = CraftingTable()

    display_current_resources(crafting_table, "Начальные ресурсы")
    crafting_table.add_resource(Stick(5))
    crafting_table.add_resource(Stone(3))
    crafting_table.add_resource(Iron(2))
    crafting_table.add_resource(Diamond(1))
    display_current_resources(crafting_table, "Ресурсы после добавления")

    stone_sword = attempt_craft(crafting_table, 'stone_sword')
    iron_sword = attempt_craft(crafting_table, 'iron_sword')
    diamond_sword = attempt_craft(crafting_table, 'diamond_sword')
    display_current_resources(crafting_table)

    attempt_disassemble(crafting_table, stone_sword)
    display_current_resources(crafting_table)

    print("\n--- Добавляем дополнительные ресурсы для зачарования и новых крафтов ---")
    crafting_table.add_resource(Diamond(5))
    crafting_table.add_resource(Stick(2))
    crafting_table.add_resource(Iron(2))
    crafting_table.add_resource(Stone(2))
    display_current_resources(crafting_table)

    # Крафт зачарованных мечей
    enchanted_stone_sword = attempt_craft(crafting_table, 'enchanted_stone_sword')
    enchanted_iron_sword = attempt_craft(crafting_table, 'enchanted_iron_sword')
    enchanted_diamond_sword = attempt_craft(crafting_table, 'enchanted_diamond_sword')
    display_current_resources(crafting_table)

    # Тестируем разбор зачарованного меча
    attempt_disassemble(crafting_table, enchanted_diamond_sword)
    display_current_resources(crafting_table)
