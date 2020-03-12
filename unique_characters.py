# def unique(string):
#     string = string.replace(' ', '')
#     return len(set(string)) == len(string)
#
# print(unique('a b cdef'))

def unique(s):
    s = s.replace(' ', '')
    characters = set()
    for letter in s:
        if letter not in characters:
            characters.add(letter)
    return characters


print(unique('aaaaaaaaaaaaaa'))
