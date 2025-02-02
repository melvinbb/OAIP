def prime_number(n2, divisor=None):
    if n2 <= 1:
        return False
    if divisor is None:
        divisor = n2 - 1
    if divisor == 1:
        return True
    if n2 % divisor == 0:
        return False
    return prime_number(n2, divisor - 1)