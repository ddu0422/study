n, m, k = map(int, input().split())

d = [[0] * (m + 1) for _ in range(n + 1)]
index = 1
x, y = 0, 0
a = [[0] * (m + 1) for _ in range(n + 1)]
for i in range(1, n + 1):
    for j in range(1, m + 1):
        a[i][j] = index
        if index == k:
            x, y = i, j

        index += 1


def solution(a, d):
    k = a[x][y]
    d[1][1] = 1

    for i in range(1, n + 1):
        for j in range(1, m + 1):
            # 첫번째 칸은 초기화했으므로 건너띈다.
            if i == 1 and j == 1:
                continue

            # k가 있는 경우 k를 영점으로 본다면 1사분면, 3사분면은 기록될 수 없다.
            if k:
                if not ((0 <= i <= x and 0 <= j <= y) or (x <= i <= n and y <= j <= m)):
                    continue

            # 위에서 들어오는 경우와 왼쪽에서 들어오는 경우를 더하면 현재 좌표에 도달할 수 있는 경우의 수를 구할 수 있다.
            d[i][j] = d[i - 1][j] + d[i][j - 1]

    return d[n][m]


print(solution(a, d))
