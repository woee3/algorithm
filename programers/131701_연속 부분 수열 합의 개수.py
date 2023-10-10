def solution(elements):
    answer = set()
    elements = elements + elements
    for i in range(1, len(elements) // 2 + 1):
        for j in range(len(elements) // 2):
            if j + i > len(elements) - 1:
                break
            answer.add(sum(elements[j:j + i]))

    return len(answer)