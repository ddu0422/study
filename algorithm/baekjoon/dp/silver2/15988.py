import sys

MOD = 1000000009

t = int(sys.stdin.readline().rstrip())
d = [0] * 1000001
result = []


def solution(n):
    if n <= 2:
        return n

    d[1] = 1
    d[2] = 2
    d[3] = 4

    for i in range(4, n + 1):
        d[i] = (d[i - 1] + d[i - 2] + d[i - 3]) % MOD

    return d[n] % MOD


for _ in range(t):
    n = int(sys.stdin.readline().rstrip())
    result.append(solution(n))


print(*result, sep='\n')
