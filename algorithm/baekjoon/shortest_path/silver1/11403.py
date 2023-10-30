import sys

INF = 1e9

n = int(sys.stdin.readline().rstrip())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    numbers = list(map(int, sys.stdin.readline().rstrip().split()))
    for index, value in enumerate(numbers):
        if value:
            graph[i][index + 1] = 1


for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


for i in range(1, n + 1):
    for j in range(1, n + 1):
        print(0 if graph[i][j] == INF else 1, end=' ')
    print()
