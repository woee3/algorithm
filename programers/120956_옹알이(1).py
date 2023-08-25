def solution(babbling):
    answer = 0
    babble = ["aya", "ye", "woo", "ma"]
    for w in babbling:
        temp = w
        for b in babble:
            index = w.find(b)
            if index < 0:
                continue
            w = w[:index]+ " " +w[index+len(b):]
            temp = w.replace(" ", "")

        if not temp:
            answer += 1
    return answer