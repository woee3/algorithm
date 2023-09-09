def closer(left, right, n, hand):
    loc = [2, n // 3 + 1]
    if n == 0:
        loc[1] = 4

    left_d = abs(loc[0] - left[0]) + abs(loc[1] - left[1])
    right_d = abs(loc[0] - right[0]) + abs(loc[1] - right[1])
    if left_d < right_d:
        return loc, "L"
    elif right_d < left_d:
        return loc, "R"
    else:
        if hand == "right":
            return loc, "R"
        else:
            return loc, "L"


def solution(numbers, hand):
    answer = ''
    left = [1, 4]
    right = [3, 4]
    for i in numbers:
        if i in [1, 4, 7]:
            answer += "L"
            left = [1, i // 3 + 1]
        elif i in [3, 6, 9]:
            answer += "R"
            right = [3, i // 3]
        else:
            loc, s = closer(left, right, i, hand)
            if s == "R":
                right = loc
            else:
                left = loc
            answer += s
    return answer