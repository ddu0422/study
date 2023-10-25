import sys

n = int(sys.stdin.readline().rstrip())
maps = []

for _ in range(n):
    lines = list(map(int, sys.stdin.readline().rstrip().split()))
    maps.append(lines)

# 경우의 수를 보관할 배열
d = [[0] * n for _ in range(n)]


def solution(n, maps, d):
    d[0][0] = 1

    for i in range(n):
        for j in range(n):
            distance = maps[i][j]

            # 3. 종료 조건 (0은 더 이상 진행을 막는 종착점이다.)
            if not distance:
                break

            # 1. 기준으로부터 아래쪽으로 진행하는 경우
            if 0 <= i + distance < n:
                d[i + distance][j] += d[i][j]
                
            # 2. 기준으로부터 오른쪽으로 진행하는 경우
            if 0 <= j + distance < n:
                d[i][j + distance] += d[i][j]

    return d[n - 1][n - 1]


print(solution(n, maps, d))
