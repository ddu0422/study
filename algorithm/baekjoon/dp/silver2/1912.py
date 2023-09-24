"""
d[n]: 연속된 몇 개의 수를 선택하여 가장 큰 합
"""
import sys

n = int(sys.stdin.readline().rstrip())
numbers = [0] + list(map(int, sys.stdin.readline().rstrip().split()))[:n]


def solution(a):
    d = [0] * len(a)

    for i in range(1, len(a)):
        d[i] = max(d[i - 1] + a[i], a[i])

    return max(d[1:])


print(solution(numbers))
