def solution(lines):
    answer = 0
    que = []
    end_time = 0
    for t in lines:
        time = t.split(" ")
        e = time[1].split(":")
        end = int(e[0]) * 3600000
        end += int(e[1]) * 60000
        e = e[2].split(".")
        end += int(e[0]) * 1000
        end += int(e[1])
        s = time[2][:-1].split(".")
        start = int(s[0]) * 1000
        if len(s) > 1:
            start += int(s[1])
        start = end - start + 1
        que.append([start, end])

    for i in range(len(que)):
        s, e = que[i]
        temp_answer = 1
        i += 1
        while i < len(que) and que[i][1] < e + 3999:
            if que[i][0] <= e + 999:
                temp_answer += 1
            i += 1
        answer = max(answer, temp_answer)
    return answer