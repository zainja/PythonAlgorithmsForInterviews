def non_repeating(s):
    s = s.replace(' ', '').lower()
    char_count = {}
    for c in s:
        if c in char_count:
            char_count[c] += 1

        else:
            char_count[c] = 1
    all_uniques = []
    y = sorted(char_count.items(), key=lambda x: x[1])
    for item in y:
        if item[1] == y[0][1]:
            all_uniques.append(item[0])
    return all_uniques


print(non_repeating('I love apple'))
