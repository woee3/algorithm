def solution(numbers):
    strNum = [str(i) for i in numbers]
    strNum.sort(key=lambda x: (x * 4)[:4], reverse=True)

    return str(int("".join(strNum)))