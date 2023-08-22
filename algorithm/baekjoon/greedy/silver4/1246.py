"""
N: 달갈 개수
M: 고객 수

i번째 고객은 각자 달걀을 Pi 가격 이하로 살 수 있다.
- 고객은 하나의 달걀만 살 수 있음.

최대 수익을 올릴 수 있는 달걀의 가장 낮은 가격과 이 때의 총 수익은?

=== example ===
5 4
2
8
10
7

7 21
7로 책정하는 경우 8 / 10 / 7 이하인 경우 달걀을 구매하는 인원이 있다.
즉 7이 이 때의 달걀의 가장 낮은 가격이고 총 수익은 21이다.

"""
import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
customers = []
for _ in range(m):
    customers.append(int(sys.stdin.readline().rstrip()))


def solution(n, customers):
    # 내림차순으로 정렬하여 높은 예산을 지닌 고객에게 먼저 판매한다.
    # 높은 예산 * 고객 수를 진행했을 때, 예산이 가장 큰 금액을 구하면 된다.
    customers = sorted(customers, reverse=True)
    max_benefit = 0
    min_egg_price = 0

    for i in range(min(n, len(customers))):
        # <가 아니라 <=인 이유는 이익이 동일할 때, 달걀 가격을 최소화해야하기 때문이다.
        if max_benefit <= (i + 1) * customers[i]:
            max_benefit = (i + 1) * customers[i]
            min_egg_price = customers[i]

    return [min_egg_price, max_benefit]


max_price, max_benefit = solution(n, customers)
print(max_price, max_benefit, sep=" ")
