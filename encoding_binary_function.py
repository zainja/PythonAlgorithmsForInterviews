def to_binary(a, b) -> int:
    counter = a
    two_powers = 1
    while counter > 0:
        two_powers += two_powers
        counter -= 1
    print(two_powers)
    r2 = b*2 + 1
    r3 = two_powers * r2
    return r3 - 1

print(to_binary(3, 4))
