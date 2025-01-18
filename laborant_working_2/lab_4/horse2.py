def horse2(a: str):
    cols = 'abcdefgh'
    rows = '12345678'
    x, y = cols.index(a[0]), rows.index(a[1])
    moves = [(-2, 1), (-2, -1), (-1, 2), (-1, -2), (1, 2), (1, -2), (2, 1), (2, -1)]
    result = []
    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 8 and 0 <= ny < 8:
            result.append(cols[nx] + rows[ny])
    print(*sorted(result), sep='\n')
