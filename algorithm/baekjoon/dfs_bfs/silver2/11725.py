"""
1: [4, 6]
2: [4]
3: [5, 6]
4: [1, 2, 7]
5: [3]
6: [1, 3]

1 - 6 - 3 - 5
  ㄴ 4 - 2
      ㄴ 7

4
6
1
3
1
4
BFS
현재 노드가 부모 노드가 된다.
"""
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
nodes = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append(b)
    nodes[b].append(a)

visited = [False] * (n + 1)


def solution(nodes, visited):
    queue = deque([1])
    visited[1] = True
    parents = [1] * len(visited)

    while queue:
        now = queue.popleft()

        for v in nodes[now]:
            if not visited[v]:
                visited[v] = True
                parents[v] = now
                queue.append(v)

    return parents[2:]


print(*solution(nodes, visited), sep="\n")
