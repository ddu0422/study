import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
count = int(sys.stdin.readline().rstrip())
edges = []
visited = [False for _ in range(n + 1)]
for _ in range(count):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    edges.append((a, b))


def solution(n, edges, visited):
    graphs = [[] for _ in range(n + 1)]

    for a, b in edges:
        graphs[a].append(b)
        graphs[b].append(a)

    queue = deque([1])
    visited[1] = True

    while queue:
        now = queue.popleft()

        for v in graphs[now]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)

    return visited.count(True) - 1


print(solution(n, edges, visited))
