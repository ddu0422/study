"""
d[n]: 적당한 시점에 사고 적당힌 시점에 팔아서 얻을 수 있는 최대 이득
첫날은 이득이 없다.
a => n일의 가격
"""
import sys

n = int(sys.stdin.readline().rstrip())
INF = 10**9 + 1
stocks = [INF] + list(map(int, sys.stdin.readline().rstrip().split()))


def solution(a):
    d = [0] * len(a)
    min_value = INF

    for i in range(1, len(a)):
        if min_value > a[i - 1]:
            min_value = a[i - 1]
        d[i] = max(d[i], a[i] - min_value)

    return max(d)


print(solution(stocks))
