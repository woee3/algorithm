def solution(storey):
    answer = 0
    number = []
    length = len(str(storey))

    for i in range(length, -1, -1):
        number.append(storey // (10 ** i))
        storey %= (10 ** i)

    for i in range(length, -1, -1):
        if number[i] == 10:
            number[i - 1] += 1
        elif number[i] > 4 and number[i - 1] > 4:
            answer += (10 - number[i])
            number[i - 1] += 1
        elif number[i] > 5:
            answer += (10 - number[i])
            number[i - 1] += 1
        else:
            answer += number[i]
    return answer