import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
a = list(map(int, sys.stdin.readline().rstrip().split()))[:n]
b = list(map(int, sys.stdin.readline().rstrip().split()))[:m]


def solution(a, b):
    return sorted(a + b)


print(*solution(a, b))
