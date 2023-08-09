"""
최대한 많은 부서의 물품을 구매
구매해줄 때는 일부가 아닌 신청한 금액만큼 모두 지원
"""

def solution(d, budget):
    answer = 0

    for price in sorted(d):
        if budget < price:
            break
        budget -= price
        answer += 1

    return answer


d = [5, 4, 3, 2, 1]
budget = 9
print(solution(d, budget))