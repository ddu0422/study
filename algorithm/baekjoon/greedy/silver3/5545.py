"""
최고의 피자란, 피자가게에서 주문할 수 있는 피자 중 1원당 열량이 가장 높은 피자를 의미한다.
토핑 N에게서 여러 종류를 선택해서 주문할 수 있다.
- 같은 종류의 토핑을 2개 이상 선택할 수는 없다.
- 토핑을 전혀 선택하지 않을 수도 있다.

A: 도우의 가격
B: 토핑의 가격
K: 토핑의 개수
피자의 가격 = A + B * k
피자의 열량 = 도우와 토핑의 열량의 합

1원당 열량을 출력 (소수점 이하는 버림)
"""
import sys

n = int(sys.stdin.readline().rstrip())
a, b = map(int, sys.stdin.readline().rstrip().split())
c = int(sys.stdin.readline().rstrip())
topping = []
for _ in range(n):
    topping.append(int(sys.stdin.readline().rstrip()))


def solution(a, b, c, topping):
    topping = sorted(topping, reverse=True)
    calorie = c
    coin = a

    for value in topping:
        if calorie / coin < (calorie + value) / (coin + b):
            calorie += value
            coin += b
    
    return int(calorie / coin)


print(solution(a, b, c, topping))
