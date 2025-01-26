def quarters(*points):
    result = {"I": 0, "II": 0, "III": 0, "IV": 0}
    for x, y in points:
        if x > 0 and y > 0:
            result["I"] += 1
        elif x < 0 < y:
            result["II"] += 1
        elif x < 0 and y < 0:
            result["III"] += 1
        elif x > 0 > y:
            result["IV"] += 1

    return result