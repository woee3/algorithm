def solution(a):
    answer = 1
    m = min(a)
    i = a.index(m)
    left = a[:i]
    right = a[i + 1:]

    if left:
        l = left[0]
    for k in range(len(left)):
        if left[k] <= l:
            answer += 1
            l = left[k]
    if right:
        r = right[-1]
    for k in range(len(right) - 1, -1, -1):
        if right[k] <= r:
            answer += 1
            r = right[k]

    return answer