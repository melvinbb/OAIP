def main():

#1
    n = int(input())
    numbers = []
    for i in range(n):
        numbers.append(int(input()))

    unique_digits = set()
    for number in numbers:
        while number > 0:
            unique_digits.add(number % 10)
            number //= 10

    print(len(unique_digits))
#2
    string1 = input()
    string2 = input()
    string3 = input()

    common_letters = set(string1) & set(string2) & set(string3)

    print(''.join(common_letters))
#3
    number = int(input())

    missing_digits = []
    for i in range(10):
     if str(i) not in str(number):
      missing_digits.append(i)

    print(*missing_digits)
#4
    numbers = []
    n = 1
    while True:
     number = int(input())
     if number == 0:
      break
     numbers.append(number)
     n += 1

    multiples = []
    for number in numbers:
     if number % n == 0:
      multiples.append(number)

    print(multiples)
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
    while True:
     age = input()
     if age == "":
      break
     age = int(age)

     if age >= 4500:
      print("Archean")
     elif age >= 2500:
      print("Proterozoic")
     elif age >= 540:
      print("Paleozoic")
     elif age >= 250:
      print("Mesozoic")
     else:
      print("Cenozoic")
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