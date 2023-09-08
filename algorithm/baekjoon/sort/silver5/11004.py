import sys

n, k = map(int, sys.stdin.readline().rstrip().split())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))[:n]


def solution(numbers, k):
    return sorted(numbers)[k - 1]


print(solution(numbers, k))
