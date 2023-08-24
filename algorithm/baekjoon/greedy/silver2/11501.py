"""
1. 주식 하나를 산다.
2. 원하는 만큼 가지고 있는 주식을 판다.
3. 아무것도 안한다.

날 별로 주식의 가격을 알려주었을 때, 최대 이익이 얼마나 되는지 계산하시오.

=== example ==
3일
10, 7, 6 (감소하므로 최대 이익 0)
3, 5, 9  (증가하므로 최대 이익 12가 맞지 않나..? 3, 5에 사서 9에 팔기 10)

5
1 1 3 1 2

1 1 3 => 2원 2원
1 2 => 1원
"""
import sys

t = int(sys.stdin.readline().rstrip())


def solution(prices):
    answer = 0
    prices = prices[::-1]
    max_value = prices[0]

    for value in prices:
        if max_value < value:
            max_value = value
        else:
            answer += max_value - value
    
    return answer


for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    print(solution(list(map(int, sys.stdin.readline().rstrip().split()))[:n]))
