"""
피보나치수열
d[n] = d[n - 1] + d[n - 2]
"""
n = int(input())


def solution(n):
    d = [0] * (10000 + 1)
    d[1] = d[2] = 1

    for i in range(3, n + 1):
        d[i] = d[i - 1] +  d[i - 2]

    return d[n]


print(solution(n))
