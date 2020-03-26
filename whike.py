d = 0
y = -2
r = 1
s = 0
c = 0
while y <= r:
    s = r
    c = y
    while c > 0:
        c = c - 1
        s = s - 1

    if r != s:
        d = d + 1
        r = s

print(d, y, r, s, c)