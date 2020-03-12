def countingValleys(n, s):
    pos = valleys = 0

    for steps in s:
        if steps == 'U':
           pos += 1
        else:
            pos -= 1
        if pos == 0 and steps == 'U':
            valleys += 1

    return valleys





print(countingValleys(8,'DDUUDDUDUUUD'))