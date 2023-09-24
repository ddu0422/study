"""
가장 큰 증가하는 부분 수열의 합
"""
import sys
from copy import deepcopy

n = int(sys.stdin.readline().rstrip())
numbers = [0] + list(map(int, sys.stdin.readline().rstrip().split()))[:n]


def solution(a):
    d = deepcopy(a)

    for i in range(2, len(a)):
        for j in range(1, i):
            if a[i] > a[j] and d[i] < d[j] + a[i]:
                d[i] = d[j] + a[i]

    return max(d)


print(solution(numbers))
