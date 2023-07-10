def solution(n):
    # 1 => 1
    # 2 => 2
    # 3 => 3
    # 4 => 5
    # 5 => 8
    # 6 =>
    # 111111
    # 11112
    # 11121
    # 11211
    # 12111
    # 21111
    # 1122
    # 1221
    # 2211
    # 1212
    # 2112
    # 2121
    # 222
    answer = [1, 2]
    for i in range(n - 2):
        answer.append((answer[-1] + answer[-2]) % 1234567)

    return answer[n - 1]