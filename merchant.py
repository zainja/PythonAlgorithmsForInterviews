def sockMerchant(n, ar):
    total_dict = {}
    count = 0
    for item in ar:
        if item not in total_dict:
            total_dict[item] = 1
        else:
            total_dict[item] += 1
    print(total_dict)
    for index in total_dict:
        count += total_dict[index] // 2
    return count


print(sockMerchant(9, [10, 20, 20, 10, 10, 30, 50, 10, 20]))
