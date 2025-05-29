from register import Register


def main():
    reg = Register("ecx")
    reg.load(42)
    assert reg.to_int() == 42
    assert reg.value == [0] * 26 + [1, 0, 1, 0, 1, 0]

    reg.load(-42)
    assert reg.to_int() == -42
    assert reg.value[0] == 1

    reg1 = Register("eax")
    reg2 = Register("ebx")
    reg1.load(15)
    reg2.load(10)
    reg1.add(reg2)
    assert reg1.to_int() == 25
    assert reg1.flags.zero == 0
    assert reg1.flags.negative == 0
    assert reg1.flags.overflow == 0
    assert reg1.flags.carry == 0

    reg1.load(2147483647)
    reg2.load(1)
    reg1.add(reg2)
    assert reg1.to_int() == -2147483648
    assert reg1.flags.zero == 0
    assert reg1.flags.negative == 1
    assert reg1.flags.overflow == 1
    assert reg1.flags.carry == 0

    print("Все тесты пройдены успешно!")


if __name__ == "__main__":
    main()