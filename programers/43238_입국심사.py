import heapq

def solution(n, times):
    time_taken = [0] * len(times)
    heap = []
    for i in range(len(times)):
        heapq.heappush(heap, [times[i], i])

    while n > 0:
        temp = heapq.heappop(heap)
        time_taken[temp[1]] += times[temp[1]]
        temp[0] += times[temp[1]]
        heapq.heappush(heap, temp)
        n -= 1

    return max(time_taken)