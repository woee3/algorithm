# 새로운 스코빌 = 가장 작은 스코빌 + 두번째로 작은 스코빌*2

# 새로운 스코빌을 만들 때마다 작은 순으로 정렬 해야하기 때문에
# 시간 복잡도를 고려하여 힙정렬을 사용한다.

import heapq


def solution(scoville, K):
    answer = 0
    # 힙 구조에 리스트 삽입
    heapq.heapify(scoville)

    # 최소 스코빌 지수가 K보다 커지거나 리스트의 길이가 1일 될때까지 새로운 스코빌을 만들어서 삽입 반복
    while len(scoville) > 1 and scoville[0] < K:
        A = heapq.heappop(scoville)
        B = heapq.heappop(scoville)
        new = A + (B * 2)
        heapq.heappush(scoville, new)
        answer += 1
    # 반복이 끝난 후에 조건이 만족하는지 확인 하고
    # 아닌경우는 불가능하기 때문에 -1 반환
    if scoville[0] < K:
        answer = -1
    return answer