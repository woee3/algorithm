def solution(dartResult):
    final = 0
    answer = [0, 0, 0]
    stars = [1, 1, 1]
    num = [str(i) for i in range(11)]
    award = ["*", "#"]

    i = len(dartResult) - 1
    times = 1
    index = 2
    while i > -1:
        r = 1
        a = 0
        two_num = False
        temp = 0
        if dartResult[i] in award:
            r += 1
            a = 1
        if dartResult[i - (r + 1)] in num:
            r += 1
            two_num = True
        if two_num:
            n = int(dartResult[i - r:i - (r - 2)])
            area_index = i - a
        else:
            n = int(dartResult[i - r])
            area_index = i - a
        if dartResult[area_index] == "S":
            temp += n
        elif dartResult[area_index] == "D":
            temp += n ** 2
        else:
            temp += n ** 3

        if a:
            if dartResult[i] == "*":
                stars[index] *= 2
            else:
                temp *= -1
        answer[index] = temp
        i -= (r+1)
        index -= 1
    for k in range(3):
        if k < 2:
            stars[k] *= stars[k+1]
        final += answer[k] * stars[k]
    return final


print(solution("1D2S#10S"))
