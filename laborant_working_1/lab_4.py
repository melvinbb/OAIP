def main():

#1
    number = ""
    for _ in range(8):
        digit = input()
        number += digit

    print(number, end="")
#2
    n = int(input())

    for i in range(n):
        name = input()
        print(f"{name} - {i+1}")
#3
    n = int(input("Введите день начала полетов: "))
    m = int(input("Введите шаг между полетами: "))

    for i in range(n, 32, m):
        if i <= 31:
            print(i, end=" ")
#4
    letter = input("Введите букву: ")
    n = int(input("Введите количество букв: "))

    max_count = 0
    current_count = 0

    for i in range(n):
        char = input("Введите букву: ")
        if char == letter:
            current_count += 1
            max_count = max(max_count, current_count)
        else:
            current_count = 0

    print(f"Наибольшее количество повторений буквы '{letter}' подряд: {max_count}")
#5
    n = int(input("Введите число: "))
    summa = 0
    for i in range(1, n + 1):
     if n % i == 0:
      summa += i
    print("Сумма делителей:", summa)
#6
    text = input("Введите строку: ")
    vowels = "аяоёэеуюыи"
    unstressed_count = 0
    for i in range(len(text)):
     if text[i] in vowels:
      if i == 0 or text[i - 1] == ' ':
       if i == len(text) - 1 or text[i + 1] == ' ':
        unstressed_count += 1
    print("Количество безударных гласных:", unstressed_count)
#7
    word = input("Введите слово: ")
    n = int(input("Введите натуральное число: "))

    for i in range(1, n + 1):
      print(word * i)
#8
    phone_number = input("Введите номер телефона: ")

    if not phone_number.isdigit() and phone_number[0] != "+":
        print("Неправильный номер телефона!")
    else:
        print("Авторизация по номеру телефона прошла успешно!")
#9
    password = input("Введите пароль: ")
    encrypted_password = ""
    vowels = "аеёиоуыэюя"

    for char in password:
        if char.lower() in vowels:
            encrypted_password += "0"
        else:
            encrypted_password += "1"

    print(encrypted_password)
#10
    message = 'ППррииввеетт!! ККаакк ддееллаа?? ССееггоодднняя ттааккааяя ххоорроошшааяя ппооггооддаа,, ммоожжеетт ппооггуулляяеемм??'

    corrected_message = ''
    for i in range(0, len(message), 2):
     corrected_message += message[i]

    print(corrected_message)

if __name__ == "__main__":
    main()