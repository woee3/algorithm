from collections import deque


def find_location(s, maps, len_y, len_x):
    for i in range(len_y):
        for j in range(len_x):
            if maps[i][j] == s:
                return [i, j]


def move_point_to_point(start, end, maps, len_y, len_x):
    # 맵의 크기로 방문 기록 남김
    visited = [[0] * len_x for _ in range(len_y)]
    # 시작 지점 삽입
    que = deque([start])
    # 지나 갈 수 있는 길
    pass_list = ["O", "S", "E"]
    # 상, 하, 좌, 우 움직임
    movements = [[0, 1], [0, -1], [1, 0], [-1, 0]]

    while que:
        current = que.popleft()
        # 현재 위치의 방문 기록 = 움직인 칸 수
        count = visited[current[0]][current[1]]

        for move in movements:
            next_point = [0, 0]
            next_point[0] = current[0] + move[0]
            next_point[1] = current[1] + move[1]
            # 맵 밖으로 나갔을 때 처리
            if (next_point[0] < 0 or next_point[0] > len_y - 1 or
                    next_point[1] < 0 or next_point[1] > len_x - 1):
                continue
            # 도착 지점에 도달 했을 때 방문기록으로 인해서 남겨진 카운트를 확인해서 리턴
            if next_point == end:
                return count + 1
            # 1. 통과 가능 길인지 확인
            # 2. 같은 칸에 도착 했는데 카운트가 높거나 같다면 더 이상 진행 할 필요 없음.
            # 따라서 통과 가능 길이고, 카운트가 적은 길이라면 방문 기록을 갱신.
            elif (maps[next_point[0]][next_point[1]] in pass_list and
                    (visited[next_point[0]][next_point[1]] == 0 or
                visited[next_point[0]][next_point[1]] > count + 1)):
                    visited[next_point[0]][next_point[1]] = count + 1
                    que.append(next_point)
    # while문 밖으로 나왔다면 도착 지점에 도달 할 수 없다는 뜻
    return 0



def solution(maps):
    answer = 0
    # x, y 길이 확인
    len_y = len(maps)
    len_x = len(maps[0])

    # 스트링 리스트로 만들기
    for i in range(len_y):
        maps[i] = list(maps[i])
    # 포인트 찾기
    start = find_location("S", maps, len_y, len_x)
    lever = find_location("L", maps, len_y, len_x)
    exit = find_location("E", maps, len_y, len_x)

    # 이동 하기
    # 레버 찾기
    count = move_point_to_point(start, lever, maps, len_y, len_x)
    if count == 0:
        return -1
    answer += count
    # 출구 찾기
    count = move_point_to_point(lever, exit, maps, len_y, len_x)
    if count == 0:
        return -1
    answer += count
    return answer

print(solution(["SOOOL","XXXXO","OOOOO","OXXXX","OOOOE"]))