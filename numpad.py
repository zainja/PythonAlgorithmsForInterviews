def letterCombinations(digits: str):
    numpad = {'2': ['a', 'b', 'c'], '3': ['d', 'e', 'f'], '4': ['g','h','i'],
              '5': ['j','k','l'], '6': ['m', 'n', 'o'],
              '7': ['p', 'q', 'r', 's'], '8': ['t', 'u', 'v'],
              '9': ['w', 'x', 'y', 'z']}
    set_numpad = []
    idv = []
    for i in digits:
        if i != '1':
            set_numpad.append(numpad[i])
    for i in range(len(set_numpad[0])):
        print(set_numpad[0][i])
        for j in range(1,len(set_numpad)):
            for k in range(0,len(set_numpad[j])):
                print(set_numpad[j][k])

    return set_numpad

print(letterCombinations('243'))