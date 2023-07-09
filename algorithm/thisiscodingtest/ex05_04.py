"""
# Input
5 6
101010
111111
000001
111111
111111

# Output
10
"""
# 사전 준비
from collections import deque

n, m = map(int, input().split())
graph = []
counts = []

for _ in range(n):
  lines = list(map(int, input()))
  graph.append(lines)
  counts.append([0] * m)

x, y = 0, 0
dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def bfs(graph, start, counts):
  x, y, = start

  queue = deque([start])
  counts[x][y] = 1

  while queue:
    cx, cy = queue.popleft()
    
    for i in range(len(dx)):
      nx = cx + dx[i]
      ny = cy + dy[i]

      if not (0 <= nx < n and 0 <= ny < m):
        continue

      if graph[nx][ny] == 1 and counts[nx][ny] == 0:
        queue.append((nx, ny))
        counts[nx][ny] = counts[cx][cy] + 1

bfs(graph, (x, y), counts)
print(counts[n - 1][m - 1])