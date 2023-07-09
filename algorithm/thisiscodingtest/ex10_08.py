"""
입력
5
10 -1
10 1 -1
4 1 -1
4 3 1 -1
3 3 -1

출력
10
20
14
18
17

입력
3
30 -1
20 -1
40 2 1 -1

출력
30
20
70
"""
# 사전 준비
from collections import deque
from copy import deepcopy

n = int(input())
graph = [
  [] for _ in range(n + 1)
]
indegree = [0] * (n + 1)
times = [0] * (n + 1)

for i in range(1, n + 1):
  data = list(map(int, input().split()))
  cost, vertex = data[0], data[1:-1]

  times[i] = cost
  for v in vertex:
    graph[v].append(i)


# 문제 풀이
def topology_sort():
  result = deepcopy(times)
  q = deque([i for i in range(1, n + 1) if indegree[i] == 0])
  
  while q:
    now = q.popleft()
    
    for i in graph[now]:
      result[i] = max(result[i], result[now] + times[i])
      indegree[i] -= 1
      if indegree[i] == 0:
        q.append(i)

  for i in range(1, n + 1):
    print(result[i])

topology_sort()