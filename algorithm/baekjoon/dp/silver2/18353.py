import sys

n = int(sys.stdin.readline().rstrip())
numbers = [0] + list(map(int, sys.stdin.readline().rstrip().split()))


def soluion(a):
    d = [1] * len(a)

    for i in range(1, len(a)):
        for j in range(1, i):
            if a[i] < a[j] and d[i] < d[j] + 1:
                d[i] = d[j] + 1

    return len(a) - 1 - max(d)


print(soluion(numbers))
