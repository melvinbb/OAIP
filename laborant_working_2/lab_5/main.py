from groundhog_day import groundhog_day
from gears import gears
from brackets import brackets


def test_groundhog_day():
    data = [
        'Groundhog Festival in Punxsutawney.',
        'Groundhog Festival in Punksutawney.',
        'Groundhog Festivel in Punxsutowney.'
    ]
    result = groundhog_day(data)
    print("Groundhog Day Test 1:", result)

    data = [
        'February 2 Groundhog Day',
        'february 2 Groundhog Day',
        'February 2 Groundhag Day',
        'February 2 Groundhog Day'
    ]
    result = groundhog_day(data)
    print("Groundhog Day Test 2:", result)


def test_gears():
    data = [[0, 2, 30, 15], [14, 3, 21, 60], [7, 16, 4, 8]]
    result = gears(data, 30, 7)
    print("Gears Test:", result)


def test_brackets():
    line = "[12 / (9) + 2(5{15 * <2 - 3>}6)]"
    result = brackets(line)
    print("Brackets Test 1:", result)

    line = "1{2 + [3}45 - 6] * (7 - 8) 9"
    result = brackets(line)
    print("Brackets Test 2:", result)


def main():
    test_groundhog_day()
    print()
    test_gears()
    print()
    test_brackets()


if __name__ == '__main__':
    main()
