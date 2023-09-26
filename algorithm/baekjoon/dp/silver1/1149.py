"""
RGB 거리에는 집이 N개 있다.
거리는 선분으로 나타낼 수 있고, 1번 집부터 N번 집이 순서대로 있다.

빨강, 초록, 파랑 중 하나의 색으로 칠해야 한다.
모든 집을 칠하는 비용의 최솟값은?

1. 1번 집의 색은 2번 집의 색과 같지 않아야 한다.
2. N번 집의 색은 N-1번 집의 색과 같지 않아야한다.
3. i번째 집의 색은 i-1번 / i+1번 집의 색과 같지 않아야 한다.
"""
import sys

n = int(sys.stdin.readline().rstrip())
colors = [(0, 0, 0)]
for _ in range(n):
    r, g, b = map(int, sys.stdin.readline().rstrip().split())
    colors.append([r, g, b])


def solution(a):
    d = [[0, 0, 0] for _ in range(len(a))]
    d[1][0] = a[1][0]
    d[1][1] = a[1][1]
    d[1][2] = a[1][2]

    for i in range(2, len(a)):
        d[i][0] = a[i][0] + min(d[i - 1][1], d[i - 1][2])
        d[i][1] = a[i][1] + min(d[i - 1][2], d[i - 1][0])
        d[i][2] = a[i][2] + min(d[i - 1][0], d[i - 1][1])
    
    return min(d[n])


print(solution(colors))
