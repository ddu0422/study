"""
00 타일
1  타일

N인 모든 2진 수열을 만들 수 없다.
N = 1 => 1
N = 2 => 00, 11
N = 3 => 100, 001, 111
N = 4 => 0011, 0000, 1001, 1100, 1111

2xn 타일과 동일
0 => 2x1
1 => 1x2
"""
n = int(input())
MOD = 15746


def solution(n):
    if n == 1:
        return 1

    a = 1
    b = 2

    for i in range(3, n + 1):
        if i & 1:
            a = (a + b) % MOD
        else:
            b = (a + b) % MOD

    return a if n & 1 else b


print(solution(n))
