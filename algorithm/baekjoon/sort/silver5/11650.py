import sys

n = int(sys.stdin.readline().rstrip())
coordinates = []
for _ in range(n):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    coordinates.append((x, y))


def solution(coordinates):
    return sorted(coordinates, key=lambda x: (x[0], x[1]))


for x, y in solution(coordinates):
    print(x, y, end='\n')
