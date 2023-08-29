"""
L과 R이 주어진다.
L보다 크거나 같고, R보다 작거나 같은 자연수 중 8이 가장 적에 들어있는 수에 들어있는 8의 개수는?
108 208

각 자리수에서 8이 나오지 않을 수 있는지 확인

48880
38808
"""
l, r = input().split()


def solution(l, r):    
    if len(r) > len(l):
        return 0

    carry_bit = False
    answer = 0

    for i, j in zip(l, r):
        if not carry_bit and i != j:
            carry_bit = True

        if i == '8' and j == '8' and not carry_bit:
            answer += 1

    return answer
    

print(solution(l, r))


def solution_refactor(l, r):
    # 오른쪽 수가 더 크다면 항상 8이 존재하지 않도록 숫자를 만들 수 있다.
    if len(r) > len(l):
        return 0
    
    answer = 0

    for i, j in zip(l, r):
        # 숫자가 동일한 것 중에서
        if i == j:
            # 8이 나오는 경우 8만 만들 수 있다.
            if i == '8':
                answer += 1
        # 숫자가 동일하지 않으면 사이에 8이 들어가지 않는 숫자를 만들 수 있다.
        else:
            break

    return answer
    

print(solution_refactor(l, r))
