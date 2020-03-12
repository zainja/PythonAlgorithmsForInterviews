def longest_substring(s):
    p1 = 0
    p2 = 0
    seen = set()
    lengths = []
    if s == '':
        return 0
    if len(s) == 1:
        return 1
    while p1 < len(s) and p2 < len(s):
        if s[p1] not in seen:
            seen.add(s[p1])
        else:
            if s[p1] == s[p1 - 1]:
                p2 = p1
            else:
                p2 = p1 - 1
            seen.remove(s[p1])
        lengths.append(p1 - p2 + 1)
        p1 += 1
    lengths.sort()
    return lengths



print(longest_substring("pwwkew"))
