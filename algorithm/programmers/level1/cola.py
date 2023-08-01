"""
a: 마트가 받는 콜라 병 수
b: 마트가 주는 콜라 병 수
n: 마트에 가져가는 빈 병 수
"""

def solution(a, b, n):
    answer = 0

    while n >= a:
        refund = n // a * b
        answer += refund
        n = refund + n % a

    return answer


print(solution(3, 1, 20))