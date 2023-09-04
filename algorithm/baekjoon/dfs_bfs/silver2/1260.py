import sys
from collections import deque
from copy import deepcopy

n, m, v = map(int, sys.stdin.readline().rstrip().split())

graphs = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graphs[a].append(b)
    graphs[b].append(a)

for i in range(1, n + 1):
    graphs[i] = sorted(graphs[i])

visited = [False] * (n + 1)

def bfs(graphs, start, visited):
    queue = deque([start])
    visited[start] = True

    while queue:
        now = queue.popleft()
        print(now, end=" ")

        for v in graphs[now]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True


def dfs(graphs, start, visited):
    visited[start] = True
    print(start, end=" ")
    
    for v in graphs[start]:
        if not visited[v]:
            dfs(graphs, v, visited)


dfs(graphs, v, deepcopy(visited))
print()
bfs(graphs, v, deepcopy(visited))
print()
