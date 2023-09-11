"""
d[n]: 돈이 n원일 때 2원 짜리와 5원 짜리로 줄 수 있는 동전의 최소 개수
"""
n = int(input())
INF = 987654321


def solution(n):
    if n == 1:
        return - 1
    
    d = [INF] * (n + 1)
    d[2] = 1
    
    for i in range(4, n + 1):
        if not i % 2:
            d[i] = min(d[i], i // 2)

        if not i % 5:
            d[i] = min(d[i], i // 5)

        d[i] = min(d[i], min(d[i - 2] + 1, d[i - 5] + 1))


    return d[n] if d[n] != INF else -1 


print(solution(n))
