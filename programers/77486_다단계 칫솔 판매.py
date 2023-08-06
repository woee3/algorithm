def solution(enroll, referral, seller, amount):
    answer = [0] * len(enroll)
    organization = {}
    for name, refer, i in zip(enroll, referral, range(len(enroll))):
        organization[name] = [refer, i]

    for name, earn in zip(seller, amount):
        earn *= 100
        while name != "-":
            answer[organization[name][1]] += earn - (earn // 10)
            name = organization[name][0]
            if earn < 10:
                break
            earn = earn // 10

    return answer

print(solution(["john", "mary", "edward", "sam", "emily", "jaimie", "tod", "young"], ["-", "-", "mary", "edward", "mary", "mary", "jaimie", "edward"], ["young", "john", "tod", "emily", "mary"], [12, 4, 2, 5, 10]))