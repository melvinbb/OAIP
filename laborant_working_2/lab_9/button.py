import random

all_items = {

    "Консервы": True,
    "Бутылка с водой": True,
    "Аптечка": True,
    "Антирад": True,
    "Патроны 9мм": True,
    "Патроны 7.62мм": True,
    "Патроны 12 калибра": True,
    "Батарейка": True,
    "Топливо": True,
    "Железный лом": True,
    "Электроника": True,
    "Резина": True,
    "Ткань": True,
    "Кожа": True,
    "Проволока": True,
    "Гвозди": True,
    "Клей": True,
    "Взрывчатка": True,
    "Фильтр для воды": True,
    "Спички": True,
    "Фонарик": False,
    "Нож": False,
    "Топор": False,
    "Пистолет": False,
    "Дробовик": False,
    "Автомат": False,
    "Снайперская винтовка": False,
    "Бронежилет": False,
    "Каска": False,
    "Маска противогаза": False,
    "Рюкзак": False,
    "Карта местности": False,
    "Рация": False,
    "Ключ от двери": False,
    "Записка": False,
    "Дневник выжившего": False,
    "Карта сокровищ": False,
    "Ящик с инструментами": False,
    "Лопата": False,
    "Контейнер с едой": True,
    "Контейнер с водой": True,
    "Ящик с патронами": True,
    "Ящик с медикаментами": True,
    "Ящик с инструментами2": True,
    "Генератор": False,
    "Солнечная панель": False,
    "Радио": False,
    "Книга по выживанию": False,
    "Карта радиационных зон": False,
    "Компас": False,
    "Бинокль": False,
    "Сигареты": True,
    "Алкоголь": True,
    "Шоколад": True,
    "Консервы с мясом": True,
    "Консервы с овощами": True,
    "Консервы с фруктами": True,
}


class Chest:
    def __init__(self):
        self.lock = False  # Ящик закрыт или нет.
        self.code = 0  # Код для закрытия ящика.
        self.rarity = random.randint(1, 4)  # Уровень редкости - 1: Обычный, 2: Редкий, 3: Эпический, 4: Легендарный.
        self.chest_items = {}  # Предметы в ящике.
        # Вызовы функций для случайного получения предметов, ресурсов и состояния закрытости ящика.
        self.__get_resources()
        self.__get_item()
        self.__get_lock()

    def __get_resources(self):
        # Определение шанса ресурсов в ящике в зависимости от редкости.
        if self.rarity == 4 or random.randint(1, 10) <= self.rarity + 5:
            self.chest_items['Ресурсы'] = random.randint(5, 100) * self.rarity

    def __get_item(self):
        # Определение шанса предметов в ящике в зависимости от редкости.
        if self.rarity not in (1, 2) or random.randint(1, 10) <= self.rarity + 4:
            count_items = random.randint(1, 3) * self.rarity  # Кол-во предметов умножаем на редкость ящика.
            for i in range(count_items):
                temp_item = random.choice(list(all_items.items()))
                item_name, item_value = temp_item[0], temp_item[1]
                if item_name in self.chest_items:  # Проверяем, есть ли предмет в self.chest_items
                    if item_value:  # Если предмет уже есть, проверяем умение стака предмета
                        new_value = random.randint(1, 4)
                        self.chest_items[item_name] += new_value * self.rarity  # Увеличиваем количество предмета
                else:  # Если предмета нет, добавляем его в self.chest_items
                    self.chest_items[item_name] = item_value
                    if item_value:  # Проверяем умение стака предмета
                        new_value = random.randint(1, 2)
                        self.chest_items[item_name] += (new_value * self.rarity) - 1  # Добавляем значение new_values

    def __get_lock(self):

        if self.rarity not in (1, 2, 3) or random.randint(1, 10) <= self.rarity + 5:
            self.lock = True

    def pick_lock(self, user_input=None):
        try:
            user_input = int(user_input)
        except ValueError:
            print('Введен некорректный тип данных, требуется число.')
            return
        if self.lock and self.code == 0:
            open_number = random.randint(1, 5)
            if user_input is None:
                print('Введите число для взлома в аргумент функции.')
            else:
                if user_input < 1 or user_input > 5:
                    print(f'Число должно быть от 1 до 5, попробуйте ещё раз.')
            if user_input == open_number:
                print('Замок взломан!')
                self.lock = False
            else:
                print('Замок не взломан, попробуйте ещё раз!')
        elif self.lock:
            if user_input is None:
                print('Введите код для открытия ящика в аргумент функции.')
            if user_input == self.code:
                print('Ящик открыт!')
                self.lock = False
            else:
                print('Ящик не открылся, попробуйте ещё раз!')
        else:
            print('Ящик был уже открыт!')

    def get_rarity(self):
        rarity_names = {1: 'обычный', 2: 'редкий', 3: 'эпический', 4: 'легендарный'}
        return rarity_names.get(self.rarity)

    def open_chest(self):
        if self.lock:
            print('Ящик закрыт. Взломайте его или откройте ключом!' if self.code == 0
                  else 'Ящик закрыт специальным ключом, надо открыть его!')
            return
        print(f'Ящик типа: {self.get_rarity()}, открывается...')
        if not self.chest_items:
            print('В этом ящике ничего нет!')
        else:
            print('Вот что лежит в ящике:')
            if self.chest_items:
                for item_name, item_value in self.chest_items.items():
                    if item_value is not False:
                        print(f'>\t{item_name} - {item_value} шт.')
                    else:
                        print(f'>\t{item_name}')

    def close_chest(self, user_input=None):
        try:
            user_input = int(user_input)
        except ValueError or TypeError:
            print('Введен некорректный тип данных, требуется число.')
            return
        if self.lock:
            print('Ящик закрыт. Взломайте его или откройте ключом!' if self.code == 0
                  else 'Ящик закрыт специальным ключом, надо открыть его!')
            return
        if user_input is None:
            print('Введите число для специального ключа в аргумент функции.')
        elif user_input > 0:
            print('Замок закрыт на ключ! Запомните его.')
            self.lock = True
            self.code = user_input
        else:
            print('Ваше число меньше 1.')

    def get_item(self, item):
        if self.lock:
            print('Ящик закрыт. Взломайте его или откройте ключом!' if self.code == 0
                  else 'Ящик закрыт специальным ключом, надо открыть его!')
            return
        if self.chest_items == {}:
            print('Ящик пуст!')
            return
        if item not in self.chest_items:
            print('Такого предмета нет в ящике.')
            return
        if self.chest_items[item]:
            while True:
                try:
                    count = int(input('В каком количестве вы хотите взять этот тип предмета:\n>\t'))
                except ValueError:
                    print('Неправильно введено число.')
                    continue
                if count <= 0:
                    print('Количество должно быть больше нуля.')
                    continue
                elif count > self.chest_items[item]:
                    print('Количество предмета превышает доступное.')
                    continue
                else:
                    self.chest_items[item] -= count
                    if self.chest_items[item] == 0:
                        del self.chest_items[item]  # Удаляем предмет, если его количество стало нулевым
                    return item, count
        else:
            del self.chest_items[item]
            return item, None
