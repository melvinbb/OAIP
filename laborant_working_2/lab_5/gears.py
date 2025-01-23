def gears(data, n, m):
    a, b = {}, {}
    for gear_list in data:
        for gear in gear_list:
            if gear % n == 0 and gear >= n:
                rn = gear // n
                if rn in b and rn not in a:
                    return gear, b[rn]
                a[rn] = gear
            elif gear % m == 0 and gear >= m:
                rm = gear // m
                if rm in a and rm not in b:
                    return a[rm], gear
                b[rm] = gear
    return None, None
