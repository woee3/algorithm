import copy


def solution(numbers):
    answer = []
    # 각 숫자에 대해서 계산 해보기 위해 for문 사용
    for number in numbers:
        binary = []
        # 시작 숫자 저장
        answer.append(number)
        # 이진수로 변경(역순으로)
        while number > 0:
            binary.append(number % 2)
            number = number // 2
        binary.append(0)
        # 2개 이하로 다른 비트를 찾으려면 더해지는 비트는 반드시 1이 하나만 포함되어야 함
        # 예) 1, 10, 100, 1000, ...
        for i in range(len(binary)):
            # 1비트가 더해 질때 변한 자릿수 카운트
            count = 0
            for j in range(i, len(binary)):
                # 해당 자리 수 부터 순차적으로 이동
                count += 1
                # 1이 더해 졌다면 다음 자리도 변할 것이므로 계속해서 카운트 진행
                if binary[j] == 1:
                    continue
                # 카운트가 2 초과 된다면 해당 비트를 더해서는 답을 찾을 수 없으므로 배제
                elif count > 2:
                    break
                # 첫번째와 두번째에 걸러 지지 않았다면 2번 이하로 자리 수가 변하였다는 뜻
                else:
                    break
            # 마지막 결과만 거르기 위함 if문.
            if count <= 2:
                # 저장한 값에 비트를 10진수로 변경
                # 예) 더해진 비트 100, => 2^2 = 4
                answer[-1] += 2 ** i
                break

    return answer