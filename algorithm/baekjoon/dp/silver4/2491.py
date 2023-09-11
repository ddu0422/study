"""
d[n]: n일 때, 가장 긴 구간이 되는 길이
"""
import sys

n = int(sys.stdin.readline().rstrip())
numbers = list(map(int, sys.stdin.readline().rstrip().split()))[:n]


def solution(numbers):
    # 가장 긴 구간이 되는 길이의 최솟값은 1이다.
    d1 = [1] * len(numbers)
    d2 = [1] * len(numbers)

    for i in range(len(numbers) - 1):
        if numbers[i + 1] >= numbers[i]:
            d1[i + 1] = d1[i] + 1

    numbers = numbers[::-1]

    for i in range(len(numbers) - 1):
        if numbers[i + 1] >= numbers[i]:
            d2[i + 1] = d2[i] + 1

    return max(d1 + d2)


print(solution(numbers))
