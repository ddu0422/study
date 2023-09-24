"""
d[n]: 가장 긴 증가하는 부분 수열의 길이

10, 20, 10, 20, 30
1, 2, 1, 2, 3

10, 20, 20, 20, 30
1, 2, 2, 2, 3
"""
import sys

n = int(sys.stdin.readline().rstrip())
numbers = [0] + list(map(int, sys.stdin.readline().rstrip().split()))[:n]


def solution(a):
    d = [1] * (len(a))

    for i in range(2, len(numbers)):
        for j in range(1, i):
            # 현재 숫자보다 작은 부분 수열 중 가장 길이가 긴 부분 수열
            if a[i] > a[j] and d[i] < d[j] + 1:
                d[i] = d[j] + 1

    return max(d)


print(solution(numbers))
