"""
입구 1 / 각 방마다 번호가 새겨짐
입구에서 최대한 먼 방에 아이스크림을 숨긴다.

1 - 2    (3)
    ㄴ 3 (2)
    ㄴ 4 (4)

1 - 2 - 4 (7)
"""
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
nodes = [[] for _ in range(n + 1)]
visited = [False] * (n + 1)

for _ in range(n - 1):
    a, b, c = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append((b, c))
    nodes[b].append((a, c))


def solution(nodes, visited):
    distance = [0] * len(visited)
    queue = deque([1])
    visited[1] = True
    distance[1] = 0

    while queue:
        now = queue.popleft()

        for v, dist in nodes[now]:
            if not visited[v]:
                # 다음 노드까지의 거리 = 현재까지 노드까지 온 거리 + 현재 노드에서 다음 노드까지의 거리
                distance[v] = distance[now] + dist
                visited[v] = True
                queue.append(v)

    return max(distance)


print(solution(nodes, visited))
