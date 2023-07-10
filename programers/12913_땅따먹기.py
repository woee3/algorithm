import copy


def solution(land):
    # land를 깊은 복사
    copy_land = copy.deepcopy(land)

    # 위에서 부터 갱신하면서 내려가기
    for i in range(1, len(land)):
        for j in range(4):
            for k in range(4):
                # 인덱스가 같다면 건너 뛰기
                if k == j:
                    continue
                temp = copy_land[i-1][j] + land[i][k]

                # 이전 행과 현재 행의 합이 크다면 갱신
                if temp > copy_land[i][k]:
                    copy_land[i][k] = temp
            print(copy_land)
        # print(land)
    return max(copy_land[-1])

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]))