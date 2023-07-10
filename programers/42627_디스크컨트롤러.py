import heapq
def solution(jobs):
    answer = 0
    # 나중에 평균을 위한 전체 길이
    total_working = len(jobs)
    # 힙으로 변환
    heapq.heapify(jobs)
    que = []
    time = 0
    running = -1
    start_time = 0
    # 전체가 종료 될 때까지
    while jobs or que or running > -1:
        # 작업이 시작 가능하다면 que에 추가
        while jobs and jobs[0][0] == time:
            job = heapq.heappop(jobs)
            heapq.heappush(que, (job[1], job[0]))

        # 작업이 끝나면 정답에 더하기
        if running == 0:
            answer += (time - start_time)
            running = -1

        # 시작 할 수 있는 작업 중에 짧은 것부터
        if que and running < 0:
            job = heapq.heappop(que)
            running = job[0]
            start_time = job[1]

        # while문 돌 때마다 시간 증가
        time += 1
        running -= 1

    # 평균 구하기
    return answer // total_working