def solution(clothes):
    answer = 1
    kind = {}
    for i, j in clothes:
        if j in kind:
            kind[j] += 1
        else:
            kind[j] = 2
    for k in kind:
        answer *= kind[k]
    return answer-1