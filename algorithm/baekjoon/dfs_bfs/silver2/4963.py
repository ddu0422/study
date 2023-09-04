import sys
from collections import deque


dx = [-1, -1, -1, 0, 1, 1, 1, 0]
dy = [1, 0, -1, -1, -1, 0, 1, 1]


def solution(graphs, x, y, visited, n, m):
    if visited[x][y] or not graphs[x][y]:
        return False

    queue = deque([(x, y)])
    visited[x][y] = True

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

    return True


for line in sys.stdin:
    x, y = map(int, line.rstrip().split())
    if x == 0 and y == 0:
        break

    graphs = []
    for _ in range(y):
        graphs.append(list(map(int, sys.stdin.readline().rstrip().split())))
    visited = [[False for _ in range(x)] for _ in range(y)]

    answer = 0

    for row in range(x):
        for column in range(y):
            if solution(graphs, column, row, visited, y, x):
                answer += 1

    print(answer)
