"""
1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11
1, 1, 1, 2, 2, 3, 4, 5, 7, 9, 12

5 = 4 0
6 = 5 1
7 = 6 2
8 = 7 3
9 = 8 4
10 = 9 5
11 = 10 6
12 = 11 7
"""
import sys
t = int(sys.stdin.readline().rstrip())


def solution(n):
    if n <= 3:
        return 1
    
    if n == 4:
        return 2

    d = [0] * (n + 1)
    d[1] = d[2] = d[3] = 1
    d[4] = 2

    for i in range(5, n + 1):
        d[i] = d[i - 1] + d[i - 5]

    return d[n]



for _ in range(t):
    print(solution(int(sys.stdin.readline().rstrip())))
