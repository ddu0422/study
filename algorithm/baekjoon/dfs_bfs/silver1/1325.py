"""
5 4
3 1
3 2
4 3
5 3

5 5
5 4
4 3
3 2
2 1
1 5

5 5
5 4
4 3
3 2
2 1
1 4
"""
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    nodes[y].append(x)


def solution(nodes):
    result = []
    max_value = 0

    for i in range(1, n + 1):
        count = bfs(nodes, i)
        result.append((i, count))
        max_value = max(max_value, count)

    for index, count in result:
        if count == max_value:
            print(index, end=" ")
    print()


def bfs(nodes, start):
    queue = deque([start])
    visited = [False] * (n + 1)
    visited[start] = True
    count = 1

    while queue:
        now = queue.popleft()

        for v in nodes[now]:
            if not visited[v]:
                queue.append(v)
                visited[v] = True
                count += 1

    return count


solution(nodes)
