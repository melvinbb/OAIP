from quarters import quarters
from future import future
from circuit_resistance import circuit_resistance
def main():
    points = [(1, 1), (-1, 2), (-3, -1)]
    result1 = quarters(*points)
    for quater, count in result1.items():
        print(f"{quater}: = {count}")

    mass = [1, 2, 3, 4, 5]
    const = {"e0": 9, "mu0": 4}
    print(future(*mass, **const))

    resistance = circuit_resistance(30, 30, 30, connection='parallel')
    print(resistance)


if __name__ == '__main__':
    main()