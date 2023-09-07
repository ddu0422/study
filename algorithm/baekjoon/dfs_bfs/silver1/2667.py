import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
maps = []
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().rstrip())))
visited = [[False for _ in range(n)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def solution(maps, visited):
    answer = []

    for i in range(n):
        for j in range(n):
            if not visited[i][j] and maps[i][j]:
                answer.append(bfs(maps, i, j, visited))

    return [len(answer), *sorted(answer)]


def bfs(maps, x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True
    answer = 1

    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if visited[nx][ny] or not maps[nx][ny]:
                continue

            queue.append((nx, ny))
            visited[nx][ny] = True
            answer += 1

    return answer


print(*solution(maps, visited), sep="\n")
