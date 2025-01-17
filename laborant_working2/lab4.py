def horse2(a: str):
    stolbec = a[:1]
    stroka = a[1:]
    stbs = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    strs = ['1', '2', '3', '4', '5', '6', '7', '8']
    n1 = stbs.index(stolbec)
    n2 = strs.index(stroka)

    tmp = [(n1 - 2, n2 + 1), (n1 - 2, n2 - 1), (n1 - 1, n2 + 2),
           (n1 - 1, n2 - 2), (n1 + 1, n2 + 2), (n1 + 1, n2 - 2),
           (n1 + 2, n2 + 1), (n1 + 2, n2 - 1)]

    res = []
    for (a, b) in tmp:
        if (a >= 0) and (b >= 0) and (a <= 8) and (b <= 8):
            res += [f'{stbs[a]}{strs[b]}']
    print(*sorted(res), sep='\n')


if __name__ == '__main__':
    horse2(input())

def func_table(f, x_max, y_max):
    for y in range(y_max + 1):
        row = []
        for x in range(x_max + 1):
            row.append(str(eval(f)))
        print('\t'.join(row))


func_table('x ** 2 + y', 3, 5)
