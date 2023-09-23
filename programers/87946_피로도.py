from itertools import permutations
def solution(k, dungeons):
    answer = 0
    num = [i for i in range(len(dungeons))]
    per = list(permutations(num, len(num)))
    for p in per:
        temp = k
        ans = 0
        for i in p:
            if temp >= dungeons[i][0] and temp >= dungeons[i][1]:
                temp -= dungeons[i][1]
                ans += 1
            else:
                break
        answer = max(answer, ans)
        if answer == len(dungeons):
            break
    return answer