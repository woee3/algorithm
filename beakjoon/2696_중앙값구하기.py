import sys
import heapq

case = int(sys.stdin.readline())

for _ in range(case):
    count = int(sys.stdin.readline())
    numbers = []
    while len(numbers) < count:
        numbers += list(map(int, sys.stdin.readline().split()))
    answer = []

    # 리스트 두개 생성
    small = [] # 최대 힙
    big = [] # 최소힙
    mid = None

    for i in range(count):
        n = numbers[i]
        if mid is None:
            mid = n
        elif n >= mid:
            heapq.heappush(big, n)
        elif n < mid:
            heapq.heappush(small, -n)

        # 홀수 번째 마다 mid를 기준으로 한칸씩 밀어준다.
        if i % 2 == 0:
            # 작은 쪽의 원소가 많다면 큰 쪽으로 옮긴다.
            while len(small) > len(big):
                heapq.heappush(big, mid)
                mid = -(heapq.heappop(small))
            # 큰 쪽의 원소가 많다면 작은 쪽으로 옮긴다.
            while len(small) < len(big):
                heapq.heappush(small, -mid)
                mid = heapq.heappop(big)
            answer.append(mid)

    # 정답 출력
    print(len(answer))
    for i in range(len(answer)):
        if (i + 1) % 10 > 0:
            if i == len(answer) - 1:
                print(answer[i])
            else:
                print(answer[i], end=" ")
        else:
            print(answer[i])
