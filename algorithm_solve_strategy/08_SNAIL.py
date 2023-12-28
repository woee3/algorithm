
case = input()
case = int(case)
answers = []

for _ in range(case):
    temp = list(input().split())
    n = int(temp[0])
    m = int(temp[1])
    board = [[0] * (m + 1) for _ in range(m * 2 + 1)]
    board[0][0] = 1000000000
    for i in range(n):
        for j in range(m):
            if i >= n:
                ans += board[i][j]
                continue
            if board[i][j] != 0:
                board[i + 1][j + 1] += int(board[i][j] * 0.25)
                board[i + 2][j + 1] += int(board[i][j] * 0.75)

    ans = 0
    for k in range(n, len(board)):
        ans += sum(board[k])
        if k > n+2:
            break
    answers.append("0."+str(ans))

for a in answers:
    print(a)

# 에러코드
# RTE (nonzero return code)

# 시도_1
# 소수점 삭제 이후 모두 int 값으로 변경

# 시도_2
# import sys 삭제 후 input()으로 변경