import sys

n = int(sys.stdin.readline().rstrip())
maps = []
for _ in range(n):
    lines = list(map(int ,sys.stdin.readline().rstrip().split()))
    maps.append(lines)

dx = [1, 0]
dy = [0, 1]
visited = [[False for _ in range(n)] for _ in range(n)]


def solution(maps, visited):
    queue = [(0, 0, maps[0][0])]
    visited[0][0] = True

    while queue:
        x, y, distance = queue.pop()

        for i in range(len(dx)):
            nx = x + dx[i] * distance
            ny = y + dy[i] * distance

            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if visited[nx][ny]:
                continue

            queue.append((nx, ny, maps[nx][ny]))
            visited[nx][ny] = True

            if maps[nx][ny] == -1:
                return "Haru" * 2

    return "Hing"


print(solution(maps, visited))
