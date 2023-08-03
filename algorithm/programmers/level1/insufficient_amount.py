"""
기존 이용료: price
n번째 이용시: 기존 이용료 * n
예산 - 놀이기구 count번 이용 시 총 금액
"""

def solution(price, money, count):
    return max(price * count * (count + 1) // 2 - money, 0)

print(solution(3, 20, 4))