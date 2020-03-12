'''
Array Pair sum
'''


def pair_sum(array, k):
    if len(array) < 2:
        return print('Too small')
    seen = set()
    output = set()

    for num in array:
        target = k - num

        if target not in seen:
            seen.add(num)
        else:
            output.add((min(num, target), max(num, target)))
    print('\n'.join(map(str, list(output))))

def rec(data):
    if data == 1:
        return data
    else:
        sum = rec(data - 1) + data
        return sum

pair_sum([1, 3, 2, 2], 4)
listt = [3,4,5,2]
listt.sort()
print(listt[0], 'elem0')
print(rec(10))