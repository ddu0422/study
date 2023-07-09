"""
입력
3 2 1
1 2 4
1 3 2

출력
2 4
"""
# 사전 준비
import heapq

INF = int(1e9)
n, m, start = map(int, input().split())
graph = [
  [] for _ in range(n + 1)
]
distance = [INF] * (n + 1)

for _ in range(m):
  a, b, c = map(int, input().split())
  # 단방향
  graph[a].append((b, c))


# 문제 풀이
def dijkstra(start):
  q = []
  distance[start] = 0
  heapq.heappush(q, (0, start))

  while q:
    dist, now = heapq.heappop(q)

    if distance[now] < dist:
      continue

    for i in graph[now]:
      cost = dist + i[1]
      if distance[i[0]] > cost:
        distance[i[0]] = cost
        heapq.heappush(q, (cost, i[0]))

dijkstra(start)

max_value = 0
result = 0

for value in distance:
  if value == INF:
    continue

  max_value = max(max_value, value)
  result += 1


print(result - 1, max_value)
