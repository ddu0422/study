import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
numbers = []
for _ in range(n):
    data = list(map(int, sys.stdin.readline().rstrip().split()))
    numbers.append(data)
coordinates = []
for _ in range(m):
    coordinate = list(map(int, sys.stdin.readline().rstrip().split()))
    coordinates.append(coordinate)


def solution(coordinates, a):
    result = []
    n = len(a)
    d = [[0 for _ in range(n + 1)] for _ in range(n + 1)]

    # 1,1부터 n,n까지 누적된 구역의 합을 구한다.
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            d[i][j] = d[i - 1][j] + d[i][j - 1] - d[i - 1][j - 1] + a[i - 1][j - 1]

    # 구하는 영역을 제외한 나머지 영역을 뺀다 (중복으로 제외한 영역을 더해준다.)
    for x1, y1, x2, y2 in coordinates:
        result.append(
            d[x2][y2] - d[x2][y1 - 1] - d[x1 - 1][y2] + d[x1 - 1][y1 - 1]
        )

    return result


print(*solution(coordinates, numbers), sep='\n')
