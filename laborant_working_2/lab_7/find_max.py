def find_max(list):
    if len(list) == 1:
        return list[0]
    else:
        max_rest = find_max(list[1:])
        return list[0] if list[0] > max_rest else max_rest