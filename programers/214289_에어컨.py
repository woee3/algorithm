import sys

limit_number = 15000
sys.setrecursionlimit(limit_number)


def solution(temperature, t1, t2, a, b, onboard):
    # 희망온도 구하기
    t = 0
    if temperature < t1:
        temperature = -temperature + t2
        t2 -= t1
        t1 = 0
    else:
        temperature -= t1
        t2 -= t1
        t1 = 0

    answer = (temperature - t2) * a

    # 탑승 정보 숫자화 하기
    start = 0
    end = 0
    # for i in range(len(onboard)):
    #     if onboard[i] == 1:
    #         start = i
    #         break
    for i in range(len(onboard) - 1, -1, -1):
        if onboard[i] == 1:
            end = i + 1
            break
    board = onboard[:end]
    global temp_cost
    temp_cost = float("inf")

    def dfs(t_now, setting, index=0, cost=0):
        global temp_cost
        if board[index] == 1 and not 0 <= t_now <= t2:
            return
        if temp_cost < cost:
            return
        if index > len(board) - 2:
            if temp_cost > cost:
                temp_cost = cost
            return

        for i in [True, False]:
            if i:
                if t_now > setting:
                    dfs(t_now - 1, setting, index + 1, cost + a)
                else:
                    dfs(t_now, setting, index + 1, cost + b)
            elif not i:
                if t_now < temperature:
                    dfs(t_now + 1, setting, index + 1, cost)
                else:
                    dfs(t_now, setting, index + 1, cost)

    if a < b * 2:
        dfs(temperature, -t2)
    else:
        dfs(temperature, t2)

    return temp_cost

print(solution(	11, 8, 10, 10, 100, [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]))
print()
print(solution(	11, 8, 10, 10, 1, [0, 1, 1, 1, 1, 1, 1, 0, 0, 0, 1, 1]))