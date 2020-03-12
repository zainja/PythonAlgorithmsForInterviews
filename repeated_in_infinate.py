def repeatedString(s, n):
    if len(s) == 1 and s == 'a':
        return n
    complete_set = n // len(s)
    remaining = n % len(s)

    counter = 0
    for i in range(len(s)):
        if s[i] == 'a':
            counter += 1
    counter = counter * complete_set
    for i in range(remaining):
        if s[i] == 'a':
            counter += 1
    return counter


print(repeatedString('x', 1000000000000))
