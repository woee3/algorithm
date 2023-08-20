def determine(stones, k, n):
    cnt = 0
    for s in stones:
        if s - n < 1:
            cnt += 1
        else:
            cnt = 0
        if cnt == k:
            return False
    return True


def solution(stones, k):
    left = 0
    right = 200_000_000
    while right - left > 1:

        mid = (left + right) // 2
        if determine(stones, k, mid):
            left = mid
        else:
            right = mid

    return right