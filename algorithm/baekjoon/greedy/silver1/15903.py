"""
자연수 n장
i번 카드에는 ai가 쓰여있다.

카드 합체 과정
1. x번 카드와 y번 카드를 골라 두 장에 쓰여진 수를 더한 값을 계산한다. (x != y)
2. 계산한 값을 x번 카드와 y번 카드 두 장 모두 덮어 쓴다.

총 m번 하면 놀이가 종료된다.
m번 후 n장의 카드에 쓰여있는 수를 모두 더한 값이 이 놀이의 점수이다.
이 점수를 가작 작게 만드는 것이 놀이의 목표이다.

1 2 3 4

3 3 3 4
6 6 3 4
"""
import sys
import heapq

n, m = map(int, sys.stdin.readline().rstrip().split())
cards = list(map(int, sys.stdin.readline().rstrip().split()))[:n]


def solution(m, cards):
    queue = []

    for card in cards:
        heapq.heappush(queue, card)
    
    for _ in range(m):
        a, b = heapq.heappop(queue), heapq.heappop(queue)
        heapq.heappush(queue, a + b)
        heapq.heappush(queue, a + b)

    return sum(queue)


print(solution(m, cards))
