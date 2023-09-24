"""
       1
      1 1
     1 2 1
    1 3 3 1
   1 4 6 4 1
  1 5 10 5 1
 1 6 15 15 6 1
1 7 21 30 21 7 1
"""
n, k = map(int, input().split())
MOD = 10007


def solution(n, k):
    k = min(n - k, k)
    d = [[0] * (n + 1) for _ in range(n + 1)]
    d[0][0] = d[1][0] = d[1][1] = 1

    for i in range(2, n + 1):
        for j in range(n + 1):
            d[i][j] = (d[i - 1][j] + d[i - 1][j - 1]) % MOD

    return d[n][k]


print(solution(n, k))
