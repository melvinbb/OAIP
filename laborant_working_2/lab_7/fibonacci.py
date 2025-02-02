def fibonacci(fib_n):
    if fib_n == 0:
        return 0
    elif fib_n == 1:
        return 1
    else:
        return fibonacci(fib_n - 1) + fibonacci(fib_n - 2)