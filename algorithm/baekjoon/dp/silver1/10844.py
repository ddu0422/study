"""
계단 수: 인접한 모든 자리의 차이가 1이다.

2자리 이상인 경우
마지막으로 끝나는 수: 0, 9 => 1개씩만 존재
나머지는 2개씩 존재
"""
n = int(input())
MOD = 1000000000


def solution(n):
    d = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(n + 1)]
    d[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

    for i in range(2, n + 1):
        for j in range(10):
            if j == 0:
                d[i][j] = d[i - 1][1] % MOD
                continue
            
            if j == 9:
                d[i][j] = d[i - 1][8] % MOD
                continue
            
            d[i][j] = (d[i - 1][j - 1] + d[i - 1][j + 1]) % MOD


    return sum(d[n]) % MOD


print(solution(n))
