"""
스터커를 선택 후 붙어있는 상하좌우 스티커는 사용할 수 없다.

101 / 102
121
212

1
5
50 10 100 20 40
30 50 70 10 60
"""
import sys

t = int(sys.stdin.readline().rstrip())


def solution(n, a, b):
    d = [[0, 0] for _ in range(n + 1)]
    d[1][0] = a[1]
    d[1][1] = b[1]

    for i in range(2, n + 1):
        d[i][0] = max(
            max(d[i - 2][0], d[i - 2][1]) + a[i],
            d[i - 1][1] + a[i],
        )
        d[i][1] = max(
            max(d[i - 2][0], d[i - 2][1]) + b[i],
            d[i - 1][0] + b[i]
        )

    return max(d[n])


result = []
for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    a = [0] + list(map(int, sys.stdin.readline().rstrip().split()))[:n]
    b = [0] + list(map(int, sys.stdin.readline().rstrip().split()))[:n]
    result.append(solution(n, a, b))
print(*result, sep='\n')
