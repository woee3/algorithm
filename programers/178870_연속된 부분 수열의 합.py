def solution(sequence, k):
    answer = [0, len(sequence)]
    dp = [0] * len(sequence)
    s = 0
    e = 0
    value = 0
    for i in range(len(sequence)):
        value += sequence[i]
        e = i
        while value > k:
            value -= sequence[s]
            s += 1
        if value == k:
            if answer[1] - answer[0] > e - s:
                answer = [s, e]
    return answer