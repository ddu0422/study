"""
입력
4
7
1 2 4
1 4 6
2 1 3
2 3 7
3 1 5
3 4 4
4 3 2

출력
0 4 8 6
3 0 7 9
5 9 0 4
7 11 2 0
"""

# 사전 준비
INF = int(1e9)
n = int(input())
m = int(input())

graph = [
  [INF] * (n + 1) for _ in range(n + 1)
]

# 자기 자신 비용 0
for i in range(1, n + 1):
  for j in range(1, n + 1):
    if i == j :
      graph[i][j] = 0

# 정점사이의 이동 비용
for _ in range(m):
  a, b, c = map(int, input().split())
  graph[a][b] = c

# 문제풀이
for k in range(1, n + 1):
  for i in range(1, n + 1):
    for j in range(1, n + 1):
      graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])

# 출력
for i in range(1, n + 1):
  for j in range(1, n + 1):
    print("INF" if graph[i][j] == INF else graph[i][j], end=" ")
  print()