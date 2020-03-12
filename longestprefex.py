def longestCommonPrefix(strs) -> str:
    cmn = ""
    for i in range(len(strs[0])):
        current_char = strs[0][i]
        for j in range(1, len(strs)):
            if strs[j][i] != current_char:
                return cmn
        cmn += current_char
    return cmn
print(longestCommonPrefix(["dog","racecar","car"]))