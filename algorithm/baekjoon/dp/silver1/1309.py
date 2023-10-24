n = int(input())
# 1번째 칸에 배치하는 경우, 2번째 칸에 배치하는 경우, 어느 쪽도 배치하지 않는 경우
d = [[0, 0, 0] for _ in range(n + 1)]
MOD = 9901


def solution(d, n):
    d[1][0] = d[1][1] = d[1][2] = 1

    for i in range(2, n + 1):
        # 1번째 칸에 배치하는 경우는 직전 칸에 배치할 때 2번째 칸에 배치하거나 
        d[i][0] = (d[i - 1][1] + d[i - 1][2]) % MOD
        d[i][1] = (d[i - 1][0] + d[i - 1][2]) % MOD
        d[i][2] = (d[i - 1][0] + d[i - 1][1] + d[i - 1][2]) % MOD
    

    return sum(d[n]) % MOD


print(solution(d, n))
