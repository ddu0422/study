import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
visited = [False] * (n + 1)
graphs = [[] for _ in range(n + 1)]
for _ in range(m):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graphs[a].append(b)
    graphs[b].append(a)


def solution(graphs, start, visited):
    if visited[start]:
        return False

    queue = deque([start])
    visited[start] = True

    while queue:
        now = queue.popleft()

        for v in graphs[now]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True

    return True


answer = 0

for i in range(1, n + 1):
    if solution(graphs, i, visited):
        answer += 1

print(answer)
