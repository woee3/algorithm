import heapq
def solution(operations):
    answer = []
    max_heap = []
    min_heap = []
    for commend in operations:
        if commend[0] == "I":
            num = int(commend[2:])
            heapq.heappush(max_heap, -num)
            heapq.heappush(min_heap, num)
        elif commend == "D 1" and max_heap:
            heapq.heappop(max_heap)
        elif commend == "D -1" and min_heap:
            heapq.heappop(min_heap)
        if not max_heap or not min_heap:
            max_heap = []
            min_heap = []

    min_heap = set(min_heap)
    max_answer = []
    min_answer = []
    for i in max_heap:
        if -i in min_heap:
            heapq.heappush(max_answer, i)
            heapq.heappush(min_answer, -i)
    if max_answer:
        answer.append(-heapq.heappop(max_answer))
    else: answer.append(0)
    if min_answer:
        answer.append(heapq.heappop(min_answer))
    else: answer.append(0)
    return answer