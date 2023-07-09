"""
입력
7 8
1 2
1 5
2 3
2 6
3 4
4 7
5 6
6 4

출력
1 2 5 3 6 4 7
"""
from collections import deque

n, m = map(int, input().split())
indegree = [0] * (n + 1)
graph = [
  [] for _ in range(n + 1)
]

for i in range(m):
  a, b = map(int, input().split())
  graph[a].append(b)
  indegree[b] += 1


def topology_sort():
  result = []
  q = deque(
    [i for i in range(1, n + 1) if indegree[i] == 0]
  )

  while q:
    now = q.popleft()
    result.append(now)

    for i in graph[now]:
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)

  for i in result:
    print(i, end=' ')

topology_sort()
print()