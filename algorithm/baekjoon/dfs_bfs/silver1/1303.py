"""
우리 병사: 흰색 옷
적국의 병사: 파란색 옷

같은 팀 병사들은 모이면 모일수록 강해진다.
N명이 뭉쳐있을 때는 N^2의 위력을 낼 수 있다.
누가 승리할 것인가? 상하좌우로 뭉쳐있는 경우만 생각한다.

81 + 49 = 130
1 + 64 = 65
"""
import sys
from collections import deque

m, n = map(int, sys.stdin.readline().rstrip().split())
maps = []
for _ in range(n):
    maps.append(list(sys.stdin.readline().rstrip()))
visited = [[False for _ in range(m)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def solution(maps, visited):
    white_score = 0
    blue_score = 0

    for x in range(n):
        for y in range(m):
            if not visited[x][y]:
                if maps[x][y] == 'W':
                    white_score += bfs(maps, x, y, visited, 'W')**2
                else:
                    blue_score += bfs(maps, x, y, visited, 'B')**2

    return [white_score, blue_score]


def bfs(maps, x, y, visited, team):
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

            if visited[nx][ny] or maps[nx][ny] != team:
                continue

            queue.append((nx, ny))
            visited[nx][ny] = True
            number += 1

    return number


print(*solution(maps, visited))
