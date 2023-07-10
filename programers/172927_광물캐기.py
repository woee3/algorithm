def solution(picks, minerals):
    answer = 0
    total_mining = sum(picks)
    minerals_bundle = []
    for i in range(0, len(minerals), 5):
        number = 0
        for element in minerals[i:i+5]:
            if element == "diamond":
                number += 31
            elif element == "iron":
                number += 6
            elif element == "stone":
                number += 1
        minerals_bundle.append(number)


    if len(minerals_bundle) > total_mining:
        minerals_bundle = minerals_bundle[:total_mining]

    minerals_bundle.sort(reverse = True)
    pick_index = 0
    for i in minerals_bundle:
        while picks[pick_index] == 0:
            pick_index += 1
        if pick_index == 0:
            answer += i // 31
            answer += i % 31 // 6
            answer += i % 31 % 6
        elif pick_index == 1:
            answer += i // 31 * 5
            answer += i % 31 // 6
            answer += i % 31 % 6
        elif pick_index == 2:
            answer += i // 31 * 25
            answer += i % 31 // 6 * 5
            answer += i % 31 % 6
        picks[pick_index] -= 1
    return answer