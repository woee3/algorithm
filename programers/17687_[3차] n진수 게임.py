from collections import deque


def solution(n, t, m, p):
    answer = ''
    hex_num = [hex(i)[2].upper() for i in range(16)]
    transform = []
    s = 0
    while len(transform) < t * m + 1:
        j = s
        temp = deque()
        while j >= n:
            temp.appendleft(j % n)
            j //= n
        temp.appendleft(j)
        transform += temp
        s += 1
    for i in range(p - 1, t * m, m):
        answer += hex_num[transform[i]]

    return answer
