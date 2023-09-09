def solution(k, m, score):
    answer = 0
    score.sort(reverse=True)
    i = 0
    box = 0
    bad = k
    while i < len(score):
        if score[i] <= k:
            box += 1
            bad = min(bad, score[i])
        if box == m:
            answer += (bad*m)
            box = 0
            bad = k
        i += 1
    return answer