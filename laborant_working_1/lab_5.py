def main():

#1
    n = int(input())
    digits = set()
    for _ in range(n):
        digits.update(input())
    print(len(digits))

#2
    string1 = input()
    string2 = input()
    string3 = input()

    common_letters = set(string1) & set(string2) & set(string3)

    print(''.join(common_letters))
#3
    digits = input()
    missing = ''.join(sorted(set('0123456789') - set(digits)))
    print(missing)

#4
    numbers = []
    num = " "
    while num != 0:
        num = int(input("Введите число (0 для завершения ввода): "))
        if num != 0:
            numbers.append(num)
    length = len(numbers)
    result = []
    for num in numbers:
        if num % length == 0:
            result.append(num)
    print(f"Числа, кратные длине последовательности:, {result}")


#5
    n = int(input())
    colors = []
    for i in range(n):
     colors.append(input())

    m = int(input())

    result = []
    for i in range(m):
     result.append(colors[i % n])

    print(*result, sep='\n')
#6
    season, era = {
        "Proterozoic": range(635 * 10 ** 6, 2800 * 10 ** 6),
        "Cenozoic": range(0, 145 * 10 ** 6),
        "Mesozoic": range(145 * 10 ** 6, 300 * 10 ** 6),
        "Paleozoic": range(300 * 10 ** 6, 635 * 10 ** 6)
        }, []
    while True:
        x = input()
        if not x:
            break
        era.append(next((key for key, value in season.items() if int(x) * 1000 in value), "Archaea"))
    print('\n'.join(era))
#7
    bird_counts = {}

    while True:
        line = input()
        if line == "":
            break
        bird, count = line.split(": ")
        count = int(count)
        if bird in bird_counts:
            bird_counts[bird] += count
        else:
            bird_counts[bird] = count

    print(bird_counts)
#8
    numbers_str = input()
    numbers = [int(x) for x in numbers_str.split()]

    result = []
    for number in numbers:
     binary_number = bin(number)[2:]
     digits = len(binary_number)
     units = binary_number.count("1")
     zeros = binary_number.count("0")
     result.append({'digits': digits, 'units': units, 'zeros': zeros})

    print(result)

if __name__ == "__main__":
    main()