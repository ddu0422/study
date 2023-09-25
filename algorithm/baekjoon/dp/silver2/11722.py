import sys

n = int(sys.stdin.readline().rstrip())
numbers = [0] + list(map(int, sys.stdin.readline().rstrip().split()))


def solution(a):
    d = [1] * len(a)

    for i in range(1, n + 1):
        for j in range(1, i):
            if a[i] < a[j] and d[i] < d[j] + 1:
                d[i] = d[j] + 1

    return max(d)


print(solution(numbers))
