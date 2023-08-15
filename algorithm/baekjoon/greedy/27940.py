"""
N: 농장 층수
제일 낮은 곳: 1층
제일 높은 곳: N층

M: 비가 쏟아지는 횟수
i번째 비가 오는 순간 1층부터 ti층이 동시에 빗물을 각각 ri만큼 받음
(빗물의 양은 마지막 비가 내린 직후까지 누적)

K: 층 별 받을 수 있는 빗물의 양 (넘어가는 경우 무너짐)
"""
import sys

n, m, k = map (int, sys.stdin.readline().rstrip().split())
rains = []
for _ in range(m):
    t, r = map(int, sys.stdin.readline().rstrip().split())
    rains.append((t, r))


def solution(rains, k):
    answer = 0
    floor = 100001

    for index, value in enumerate(rains):
        t, r = value
        answer += r
        floor = min(floor, t)
        if answer > k:
            return [index + 1, floor]

    return [-1]


print(*solution(rains, k))
