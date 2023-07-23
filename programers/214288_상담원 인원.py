from collections import deque
import heapq
global consultant
consultant = []
def con(k, c, cnt, n=0):
    if cnt == n:
        return consultant.append(c[:])

    for i in range(1, k+1):
        c[i] += 1
        con(k, c, cnt, n+1)
        c[i] -= 1


def solution(k, n, reqs):
    global consultant
    answer = float("inf")
    consult_time = deque([[] for _ in range(k + 1)])
    consult_length = deque([[] for _ in range(k + 1)])
    for a, b, c in reqs:
        consult_time[c].append(a)
        consult_length[c].append(b)

    con(k, [1]*(k+1), n-k)
    for q in consultant:
        print(q)
        total_wait_time = 0
        for i in range(1, k + 1):
            time = 0
            temp_time = deque(consult_time[i])
            temp_length = deque(consult_length[i])
            wait = deque()
            consulting = []
            wait_time = 0
            while True:
                while consulting and consulting[0] <= time:
                    heapq.heappop(consulting)
                if temp_time and temp_time[0] == time:
                    temp_time.popleft()
                    wait.append(temp_length.popleft())
                while wait and len(consulting) < q[i]:
                    heapq.heappush(consulting, wait.popleft()+time)

                if wait:
                    wait_time += 1*len(wait)
                if not temp_time and not wait:
                    break
                time += 1
                # print(time, wait_time)
                # print("con", consulting)
                # print("wait", wait)
            total_wait_time += wait_time
        if answer > total_wait_time:
            answer = total_wait_time

    return answer

print(solution(2, 3, [[5, 55, 2], [10, 90, 2], [20, 40, 2], [50, 45, 2], [100, 50, 2]]))