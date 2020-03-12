def most_frequent(lst):
    count = {}
    max_count = 0
    max_item = None

    for i in lst:
        if i not in count:
            count[i] = 1
        else:
            count[i] += 1
        if count[i] > max_count:
            max_count = count[i]
            max_item = i

    return max_item


print(most_frequent([1, 2, 3, 4, 1, 1]))
