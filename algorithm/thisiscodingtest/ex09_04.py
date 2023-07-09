"""
입력
5 7
1 2
1 3
1 4
2 4
3 4
3 5
4 5
4 5

출력
3

입력
4 2
1 3
2 4
3 4

출력
-1
"""
# 사전 준비
from copy import deepcopy
import heapq

INF = int(1e9)
n, m = map(int, input().split())
graph = [
  [] for _ in range(n + 1)
]
floyd_warshall_distance = [
  [INF] * (n + 1) for _ in range(n + 1)
]
dijkstra_distance = [INF] * (n + 1)

for _ in range(m):
  a, b = map(int, input().split())
  # 양방향
  floyd_warshall_distance[a][b] = 1
  floyd_warshall_distance[b][a] = 1
  graph[a].append((b, 1))
  graph[b].append((a, 1))

x, k = map(int, input().split())

# 문제 풀이
def floyd_warshall(distance):
  for k in range(1, n + 1):
    for i in range(1, n + 1):
      for j in range(1, n + 1):
        if i == j:
          distance[i][j] = 0
          continue
        distance[i][j] = min(distance[i][j], distance[i][k] + distance[k][j])

  result = distance[1][k] + distance[k][x]

  print(-1 if result >= INF else result)

floyd_warshall(deepcopy(floyd_warshall_distance))


def dijkstra(distance, start):
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

  return distance


print(dijkstra(deepcopy(dijkstra_distance), 1)[k] + dijkstra(deepcopy(dijkstra_distance), k)[x])