"""
d[n]: n kg을 가져갈 설탕 봉지의 최소 개수
"""
n = int(input())
INF = 10**9 + 1


def solution(n):
    d = [INF] * (n + 1)

    for i in range(3, n + 1):
        if not i % 3:
            d[i] = min(d[i], i // 3)

        if not i % 5:
            d[i] = min(d[i], i // 5)

        d[i] = min(d[i], d[i - 3] + 1, d[i - 5] + 1)

    return d[n] if d[n] != INF else -1


print(solution(n))
