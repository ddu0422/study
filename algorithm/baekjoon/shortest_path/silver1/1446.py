import sys
import heapq

INF = 1e9

n, d = map(int, sys.stdin.readline().rstrip().split())

distance = [INF] * (10000 + 1)
graph = [[] for _ in range(10000 + 1)]

for i in range(10000):
    graph[i].append((i + 1, 1))

for _ in range(n):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    graph[a].append((b, c))


def dijkstra(distance, start, d):
    q = []
    heapq.heappush(q, (0, start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop(q)

        if distance[now] < dist:
            continue

        for v in graph[now]:
            cost = dist + v[1]
            if distance[v[0]] > cost:
                distance[v[0]] = cost
                heapq.heappush(q, (cost, v[0]))

    return distance[d]


print(dijkstra(distance, 0, d))
