"""
# Input
15 14
00000111100000
11111101111110
11011101101110
11011101100000
11011111111111
11011111111100
11000000011111
01111111111111
00000000011111
01111111111000
00011111111000
00000001111000
11111111110011
11100011111111
11100011111111

# Output
8

# Input
4 5
00110
00011
11111
00000

# Output
8
"""

# 사전 준비
from collections import deque

n, m = map(int, input().split())
graph = []
visited = []
result = 0

for _ in range(n):
  lines = list(map(int, input()))
  graph.append(lines)
  visited.append([False] * m)


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(graph, x, y, visited):
  if not (graph[x][y] == 0 and not visited[x][y]):
    return 0

  queue = deque([(x, y)])
  visited[x][y] = True

  while queue:
    cx, cy = queue.popleft()

    for i in range(len(dx)):
      nx = cx + dx[i]
      ny = cy + dy[i]

      if not (0 <= nx < n and 0 <= ny < m):
        continue

      if graph[nx][ny] == 0 and not visited[nx][ny]:
        queue.append((nx, ny))
        visited[nx][ny] = True
  
  return 1


for x in range(n):
  for y in range(m):
      result += bfs(graph, x, y, visited)


print(result)
