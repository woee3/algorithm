import heapq


def solution(n, cores):
    answer = 0
    heap = []
    for i in range(len(cores)):
        heapq.heappush(heap, [cores[i], i + 1, cores[i]])
    n -= len(cores)

    while n > 0:
        low = heapq.heappop(heap)
        low[0] += low[2]
        heapq.heappush(heap, low)
        temp = [low[1]]

        while heap and low[0] == heap[0][0]:
            h = heapq.heappop(heap)
            h[0] += h[2]
            heapq.heappush(heap, h)
            temp.append(h[1])
        print(temp)
        if n <= len(temp):
            temp.sort()
            return temp[n - 1]
        n -= len(temp)


print(solution(6, [1, 2, 3]))
