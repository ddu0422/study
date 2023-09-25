"""
1 = 1
2 = 2
3 = 1 + 2
    2 + 1
    3
4 = 1 + 2 + 1 (3을 만들 수 있는 경우 중 2개)
    1 + 3
    3 + 1     (1을 만들 수 있는 경우 중 1개)
    
5 = 1 + 3 + 1

    2 + 1 + 2 
    3 + 2

    2 + 3     
    
6 = 2 + 1 + 2 + 1
    2 + 3 + 1
    3 + 2 + 1

    1 + 2 + 1 + 2
    1 + 3 + 2
    3 + 1 + 2

    1 + 2 + 3
    2 + 1 + 3
"""
import sys

MOD = 1000000009

t = int(sys.stdin.readline().rstrip())
numbers = []
for _ in range(t):
    numbers.append(int(sys.stdin.readline().rstrip()))
d = [(0, 0, 0)] * 100001


def solution(numbers):
    d[1] = (1, 0, 0)
    d[2] = (0, 1, 0)
    d[3] = (1, 1, 1)

    for i in range(4, 100001):
        d[i] = (
            (d[i - 1][1] + d[i - 1][2]) % MOD,
            (d[i - 2][0] + d[i - 2][2]) % MOD,
            (d[i - 3][0] + d[i - 3][1]) % MOD
        )

    return [sum(d[n]) % MOD for n in numbers]


print(*solution(numbers), sep='\n')
