def solution(numbers):
    # 리스트 길이 만큼 -1로 구성된 정답 리스트를 생성
    answer = [-1] * len(numbers)

    # 스택에 numbers의 첫번째 원소의 인덱스와 원소를 추가
    stack = [[0, numbers[0]]]

    for i in range(1, len(numbers)):
        # 새로 추가 되는 원소와 스택의 마지막에 있는 원소와 비교
        # 새로운 원소 > 스택에 있는 원소
        # 라면, 정답 리스트에
        # 스택에 있는 원소의 인덱스 위치에 새로운 원소로 값을 지정
        # 조건이 만족하지 않거나, 스택의 길이가 0이 될 때까지 반복
        while len(stack) > 0 and numbers[i] > stack[-1][1]:
            answer[stack[-1][0]] = numbers[i]
            stack.pop()
        # 새로운 원소 추가
        stack.append([i, numbers[i]])
    return answer

print(solution([2, 3, 3, 5]))