from material import Material, Plank
from blueprint import Blueprint
from item import Item
from crafting_table import CraftingTable


def main():
    plank = Plank(20, 15, "Pine")
    rope = Material("Rope", 10, 5)
    stone = Material("Stone", 30, 20)

    axe_blueprint = Blueprint("Axe", {"Plank": 10, "Rope": 5, "Stone": 5})
    fishing_rod_blueprint = Blueprint("Fishing Rod", {"Plank": 5, "Rope": 10})

    my_workbench.add_material(plank)
    my_workbench.add_material(rope)
    me_workbench.add_material(stone)

    axe = my_workbench.craft_item(axe_blueprint)
    if axe:
        print(axe)
        print(axe.info())

        my_workbench.add_material(stone)
        axe.upgrade(stone)
        print(axe.info())

    fishing_rod = my_workbench.craft_item(fishing_rod_blueprint)


if __name__ == "__main__":
    main()
