def solution(S, C):
    # write your code in Python 3.6
    sum_of_loss = 0
    for i in range(len(S) - 1):
        if S[i] == S[i + 1]:
            if C[i] < C[i + 1]:
                sum_of_loss += C[i]
            else:
                sum_of_loss += C[i + 1]
    return sum_of_loss

print(solution('ccc', [0, 1, 2, 3, 4, 5]))