import heapq
def solution(n, works):
    answer = 0
    works_heap = []
    for i in works:
        heapq.heappush(works_heap, -i)
    for i in range(n):
        w = heapq.heappop(works_heap)
        if w < 0:
            heapq.heappush(works_heap, w+1)
        else: break
    for elem in works_heap:
        answer += (-elem)**2
    return answer