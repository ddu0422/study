import sys
from collections import deque

INF = 1e9

n, m, k, x = map(int, sys.stdin.readline().rstrip().split())
distance = [INF] * (n + 1)
graph = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, 1))


def bfs(start, distance, graph, k):
    queue = deque([])
    queue.append((start, 0))
    distance[start] = 0

    while queue:
        now, dist = queue.popleft()

        for v in graph[now]:
            cost = dist + v[1]

            if distance[v[0]] > cost:
                distance[v[0]] = cost
                queue.append((v[0], cost))

    return [i for i in range(1, n + 1) if distance[i] == k] or [-1]


for value in sorted(bfs(x, distance, graph, k)):
    print(value)
