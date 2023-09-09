def solution(n):
    i = 0
    answer = 0
    while i < n:
        i += 1
        answer += 1
        while "3" in list(str(answer)) or answer % 3 == 0:
            answer += 1
    return answer