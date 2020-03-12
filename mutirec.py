def ex(m, n):
    if m == 0 and n == 0:
        return 0
    elif m == 0:
        return ex(n - 1, 0) + n
    elif n == 0:
        return ex(0, m - 1) + 1
    else:
        return ex(n - 1, m) + 2


def feb(n):
    if n == 0:
        return 1
    elif n == 1:
        return 1
    else:
        return feb(n - 1) + feb(n - 2)


print(feb(122))