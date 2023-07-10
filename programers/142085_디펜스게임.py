import heapq
def solution(n, k, enemy):
    answer = 0
    defense = []
    #무적권 없이 막는 적의 수
    total_enemy = 0
    for i in enemy:
        # 최대 힙에 삽입
        heapq.heappush(defense, -i)
        # 적의 수 갱신
        total_enemy += i

        # 무적권을 있는데 더이상 적을 못막을 때
        if n < total_enemy and k > 0:
            # 무적권 소모
            k -= 1
            # 최대 적이 나온 라운드 추출
            invinc = heapq.heappop(defense)
            # 무적권을 사용한 뒤 적의 수에 반영
            total_enemy += invinc
        # 이제 더이상 못 막을 때
        if n < total_enemy:
            break
        # 무적권 사용하니 막았을 때
        else:
            answer += 1
    return answer