def solution(m, n, startX, startY, balls):
    answer = []
    for x, y in balls:
        mirroring = [
            [-x, y],
            [x, -y],
            [m*2-x, y],
            [x, n*2-y]
        ]
        # x축이나 y축이 같다면 쿠션 없이 바로 부딫힌다.
        # 그래서 배제 할 것이 생길 수도....
        if x == startX:
            if y < startY:
                mirroring[1] = [0, 0]
            else:
                mirroring[3] = [0, 0]
        if y == startY:
            if x < startX:
                mirroring[0] = [0, 0]
            else:
                mirroring[2] = [0, 0]
        distance_list = []
        for new_x, new_y in mirroring:
            if not new_x == 0:
                distance_list.append((startX - new_x)**2 + (startY - new_y)**2)
        answer.append(min(distance_list))
    return answer