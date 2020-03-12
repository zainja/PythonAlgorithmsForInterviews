"""
intersection between the sets
"""


def common_elements(a, b):
    p1 = 0
    p2 = 0
    result = []

    while p1 < len(a) and p2 < len(b):
        if a[p1] == b[p2]:
            result.append(a[p1])
            p1 += 1
            p2 += 1
        elif a[p1] > b[p2]:
            p2 += 1
        else:
            p1 += 1
    return result


print(common_elements([1, 3, 4, 6, 7, 9], [1, 2, 4, 5, 9, 10]))
