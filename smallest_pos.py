def solution(A):
    # write your code in Python 3.6
    missing_pos = []
    for i in range(len(A)):
        if i not in A and i != 0:
            missing_pos.append(i)
    if not missing_pos:
        missing_pos.append(A[len(A)-1] + 1)
    missing_pos = sorted(missing_pos)
    # print(missing_pos)
    return missing_pos[0]


