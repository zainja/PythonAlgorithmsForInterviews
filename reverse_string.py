def reverse(s):
    length = len(s)
    spaces = [' ']
    words = []
    i = 0  # index tracker
    while i < length:
        if s[i] not in spaces:
            word_start = i
            while i < length and s[i] not in spaces:
                i += 1
            words.append(s[word_start:i])
        i += 1
    return " ".join(reversed(words))

    # return " * ".join(s.split()[::-1])


print(reverse('Hello my world'))
