def solution(k, d):
    answer = 0
    for i in range(0, d+1, k):
        y = i
        x = int((d**2 - y**2)**0.5)
        answer += x//k+1

    return answer