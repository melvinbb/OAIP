def horse2(a: str):
    speakers = a[:1]
    line = a[1:]
    all_speakers = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
    all_lines = ['1', '2', '3', '4', '5', '6', '7', '8']
    a = all_speakers.index(speakers)
    b = all_lines.index(line)

    ab = [(a - 2, b + 1), (a - 2, b - 1), (a - 1, b + 2),
          (a - 1, b - 2), (a + 1, b + 2), (a + 1, b - 2),
          (a + 2, b + 1), (a + 2, b - 1)]

    result = []
    for (a, b) in ab:
        if (a >= 0) and (b >= 0) and (a < 8) and (b < 8):
            result += [f'{all_speakers[a]}{all_lines[b]}']
    print(*sorted(result), sep='\n')
