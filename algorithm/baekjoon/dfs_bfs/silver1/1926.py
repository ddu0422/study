"""
그림의 개수와 그림 중 넓이가 가장 넓은 것의 넓이 출력
1로 연결된 것을 한 그림이라고 정의
가로나 세로로 연결된 된 것이 그림
그림의 넓이란 그림에 포함된 1의 개수
"""
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().rstrip().split())))
visited = [[False for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def solution(maps, visited):
    answer = [0]
    number = 0

    for x in range(n):
        for y in range(m):
            if not visited[x][y] and maps[x][y]:
                answer.append(bfs(maps, x, y, visited))
                number += 1
    
    return [number, max(answer)]


def bfs(maps, x, y, visited):
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

            if visited[nx][ny] or not maps[nx][ny]:
                continue

            queue.append((nx, ny))
            visited[nx][ny] = True
            number += 1

    return number


print(*solution(maps, visited), sep="\n")
