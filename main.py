# Задача 1: Сравнение строк
string1 = input()
string2 = input()

if string1 and string2 and string1[-1] == string2 [0] :
    print("ВЕРНО")
else:
    print("НЕВЕРНО")

# Задача 2: Максимальное количество орлов
s = input()
max_consecutive_heads = 0
current_consecutive_heads = 0

for char in s:
    if char == 'о':
        current_consecutive_heads += 1
        max_consecutive_heads = max(max_consecutive_heads, current_consecutive_heads)
    else:
        current_consecutive_heads = 0

print(max_consecutive_heads)

# Задача 3: Рисование прямоугольника
height = int(input())
width = int(input())
symbol = input()

for _ in range(height):
    print(symbol * width)

# Задача 4: Простые числа
n = int(input())
primes = []

for num in range(2, n):
    is_prime = True
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            is_prime = False
            break
    if is_prime:
        primes.append(num)

print(*primes)

# Задача 5: Рисование пути улитки (очень приблизительно, нужны детали)
initial_symbol = input()[0]  # Получаем начальный символ
instructions = input()

x = 0
y = 0

print("Эту задачу сложно реализовать без полного описания")
