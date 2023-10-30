import sys

INF = 1e9

n, m = map(int, sys.stdin.readline().rstrip().split())
graph = [[INF] * (n + 1) for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a][b] = 1
    graph[b][a] = 1

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

result = 0
max_value = sum(graph[0])

for i in range(1, n + 1):
    if max_value > sum(graph[i]):
        max_value = sum(graph[i])
        result = i

print(result)
