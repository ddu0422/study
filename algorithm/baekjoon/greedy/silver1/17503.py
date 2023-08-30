"""
N일 동안 맥주 축제
K종류의 맥주를 무료로 제공

참가자들은 하루에 맥주 1병만 받을 수 있다.
이전에 받았던 종류의 맥주는 다시 받을 수 없다.

N일 동안 맥주 N병을 마시려고 한다. (도수가 높은 맥주를 마시면 기절하는 맥주병)

K종류의 맥주에 '선호도'와 '도수 레벨'을 정함.

1. 마시는 맥주의 도수 레벨이 간 레벨보다 높으면 맥주병이 발병한다.
2. 맥주병에 걸리지 않으면서 좋아하는 맥주를 많이 마시고 싶다.
3. 맥주 N개의 선호도 합이 M이상이 되어야한다.

1 2
3 3
4 3
2 5
4 6

1 5
4 2
4 3
5 3
8 3
8 6
"""
import sys
import heapq

n, m, k = map(int, sys.stdin.readline().rstrip().split())
beers = []
for _ in range(k):
    preference, level = map(int, sys.stdin.readline().rstrip().split())
    beers.append((preference, level))


def solution(n, m, beers):
    # 선호도
    queue = []

    # 도수 레벨, 선호도 순으로 정렬
    beers = sorted(beers, key=lambda x: (x[1], x[0]))
    total = 0
    level = 0
    
    for beer in beers:
        # 최대 N개까지 맥주를 마셔야한다.
        if len(queue) < n:
            total += beer[0]
            level = max(level, beer[1])
            heapq.heappush(queue, beer)
            continue

        # 선호도를 충족하지 않는 경우 선호도가 가장 낮은 맥주를 빼고 다음 맥주를 선택한다.
        if total < m:
            total -= heapq.heappop(queue)[0]
            total += beer[0]
            level = max(level, beer[1])
            heapq.heappush(queue, beer)

    return level if total >= m else -1


print(solution(n, m, beers))
