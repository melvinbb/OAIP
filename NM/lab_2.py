import math
from builtins import print

print('УСТОЙЧИВЫЙ АЛГОРИТМ')
p = 2 * math.sqrt(2)
p1 = [0, 0, 2 * 2 ** 0.5]
for i in range(3, 61):
    p1.append(2 * (i - 1) * math.sqrt(
        (2 * (p1[i - 1] / 2 ** (i - 1)) ** 2) / (1 + math.sqrt(1 - (p1[i - 1] / 2 ** (i - 1)) ** 2))))
    print(f'p({i}) = {str(p1[i]).ljust(28)}', end='\t')
    if p > 0:
        print('Δ =', (abs(math.pi - p1[i])) / p1[i])
    else:
        print('Δ =')
