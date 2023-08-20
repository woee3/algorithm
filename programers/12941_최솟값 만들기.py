import heapq
def solution(A,B):
    answer = 0
    heapq.heapify(A)
    heap_B = []
    for i in B:
        heapq.heappush(heap_B, -i)
    while A:
        answer += heapq.heappop(A) * -heapq.heappop(heap_B)
    return answer