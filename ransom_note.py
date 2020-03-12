def checkMagazine(magazine, note):
    dec = {}
    can_be_used = True
    for i in magazine:
        if i not in dec:
            dec[i] = 1
        else:
            dec[i] += 1
    for j in note:
        if j not in dec or dec[j] == 0:
            can_be_used = False
        else:
            dec[j] -= 1
    if can_be_used:
        print('Yes')
    else:
        print('No')

magazine = input().rstrip().split()

note = input().rstrip().split()

checkMagazine(magazine, note)