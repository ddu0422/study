import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
a = []
for _ in range(n):
    a.append(sys.stdin.readline().rstrip())
b = []
for _ in range(m):
    b.append(sys.stdin.readline().rstrip())


def solution(a, b):
    result = set(a) & set(b)

    return [len(result), *sorted(result)]


print(*solution(a, b), sep='\n')
