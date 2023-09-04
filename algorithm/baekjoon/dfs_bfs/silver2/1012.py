import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def solution(graph, x, y, n, m):
    if graph[x][y] in [0, -1]:
        return False

    queue = deque([(x, y)])
    graph[x][y] = -1

    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < m):
                continue

            if graph[nx][ny] in [0, -1]:
                continue

            graph[nx][ny] = -1
            queue.append([nx, ny])

    return True


for _ in range(t):
    n, m, k = map(int, sys.stdin.readline().rstrip().split())
    graph = [[0 for _ in range(m)] for _ in range(n)]
    for _ in range(k):
        a, b = map(int, sys.stdin.readline().rstrip().split())
        graph[a][b] = 1

    answer = 0

    for i in range(n):
        for j in range(m):
            if solution(graph, i, j, n, m):
                answer += 1

    print(answer)
