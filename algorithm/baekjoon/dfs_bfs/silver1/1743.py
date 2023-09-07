"""
세로 길이: N
가로 길이: M
음식물 쓰레기의 개수: K
움식물이 떨어진 좌표: R, C
"""
import sys
from collections import deque

n, m, k = map(int, sys.stdin.readline().rstrip().split())
graphs = [[0 for _ in range(m + 1)] for _ in range(n + 1)]
for _ in range(k):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    graphs[a - 1][b - 1] = 1
visited = [[False for _ in range(m + 1)] for _ in range(n + 1)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def solution(graphs):
    result = [0]

    for x in range(n):
        for y in range(m):
            if not visited[x][y] and graphs[x][y]:
                result.append(bfs(graphs, x, y, visited))


    return max(result)


def bfs(graphs, x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    number = 1

    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if visited[nx][ny] or not graphs[nx][ny]:
                continue

            queue.append((nx, ny))
            visited[nx][ny] = True
            number += 1

    return number


print(solution(graphs))
