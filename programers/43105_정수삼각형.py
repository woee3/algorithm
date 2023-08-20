import copy


def solution(triangle):
    # 삼각형을 깊은 복사한다.
    copy_tri = copy.deepcopy(triangle)

    # 내려가면서 계산, 합이 클 때만 갱신
    for i in range(len(triangle) - 1):
        for j in range(len(triangle[i])):
            if copy_tri[i + 1][j] < triangle[i + 1][j] + copy_tri[i][j]:
                copy_tri[i + 1][j] = triangle[i + 1][j] + copy_tri[i][j]
            if copy_tri[i + 1][j + 1] < triangle[i + 1][j + 1] + copy_tri[i][j]:
                copy_tri[i + 1][j + 1] = triangle[i + 1][j + 1] + copy_tri[i][j]

    # 마지막 합이 모인 리스트에서 가장 큰 수를 반환
    return max(copy_tri[-1])
