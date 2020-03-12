line = '195'
count = 1
a = int(line)
rev_number = line[::-1]
b = int(line[::-1])
res = a + b
rev_res = int(str(res)[::-1])
while rev_res != res:
    count += 1
    a = res
    rev_number = str(res)
    rev_number = rev_number[::-1]
    b = int(rev_number)
    res = a + b
    rev_res = int(str(res)[::-1])
print(count, res)