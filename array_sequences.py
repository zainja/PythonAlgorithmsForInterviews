# list
# tuple
# string
# the original list will not change
# if we change another list pointing to it
import sys

n = 10
data = []
for i in range(n):
    a = len(data)
    b = sys.getsizeof(data)
    print(f'length: {a:3d}; Size in bytes: {b:4d}')
    data.append(n)


# the arrays are automatically expanded when it is needed
# then the older reference will be scrapped
print('string manipulations')


# string manipulations
def anagram(s1, s2):
    s1 = s1.replace(' ', '').lower()
    s2 = s2.replace(' ', '').lower()

    if len(s1) != len(s2):
        return False

    count = {}

    for letter in s1:
        if letter in count:
            count[letter] += 1
        else:
            count[letter] = 1
    for letter in s2:
        if letter in count:
            count[letter] -= 1
        else:
            count[letter] = 1
    for k in count:
        if count[k] != 0:
            return False
    return True