"""
d[n] = 가로의 길이가 n일 때 타일을 채울 수 있는 방법의 수

타일의 크기는 1x2 / 2x1이 있다.

d[1] = 1
d[2] = 2

# 2 x 1로 만들 수 있는 방법의 수 + 1 x 2로 만들 수 있는 방법의 수
d[i] = d[i - 1] + d[i - 2]
"""
n = int(input())


def solution(n):
    d = [0] * (n + 1)
    d[0] = 1
    d[1] = 1

    for i in range(2, n + 1):
        d[i] = (d[i - 1] + d[i - 2]) % 10007

    return d[n]



print(solution(n))
