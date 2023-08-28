import heapq


def solution(n, cores):
    answer = 0
    heap = []
    for i in range(len(cores)):
        heapq.heappush(heap, [cores[i], i+1, cores[i]])
    n -= len(cores)

    while n > 0:
        temp = [heapq.heappop(heap)]

        while heap and temp[0][0] == heap[0][0]:
            temp.append(heapq.heappop(heap))
        temp.sort()

        for t, num, c in temp:
            if n == 0:
                heapq.heappush(heap, [t, num, c])
            else:
                heapq.heappush(heap, [t + c, num, c])
                n -= 1
        print(heap)
    heap = list(heap)
    heap.sort()
    return heap[-1][1]


print(solution(6, [1, 2, 3]))
