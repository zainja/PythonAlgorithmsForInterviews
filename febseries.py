for line in '1  ':
    a = 0
    b = 1
    if line >= '0':
        if line == '0':
            print(line, end='')
        elif line == '1':
            print(line, end='')
        else:
            for i in range(1, int(line)):
                c = a + b
                a = b
                b = c
            line = b
            print(line, end='')


