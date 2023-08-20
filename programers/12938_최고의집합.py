# n개의 자연수로 나누어서 곱이 가장 큰 집합은 중간 값을 갖는 자연수의 집합이다.
def solution(n, s):
    division = s // n
    # 나누어서 0이 나온다면 나눌수 없으므로 -1 반환
    if division == 0:
        return [-1]

    remain = s % n
    answer = []
    # 가장 중간 값은 나머지를 1씩 배분 해주어야한다.
    # 다만 작은 수가 앞에 나와야 하므로 작은 수부터 집합에 추가
    for i in range(n - remain):
        answer.append(division)
    for i in range(remain):
        answer.append(division + 1)

    return answer
