"""
어떤 지역의 높이 정보를 파악한다.
그 지역에 많은 비가 내렸을 때 물에 잠기지 않는 안전한 영역이 최대로 몇 개가 만들어 지는 지를 조사한다.
비의 양에 따라 일정한 높이 이하의 모든 지점은 물에 잠긴다고 가정한다.
N=5

5
6 8 2 6 2
3 2 3 4 6
6 7 3 3 2
7 2 5 3 6
8 9 5 2 7

4 이하인 모든 지점이 물에 잠겼다.

안전한 영역: 물에 잠기지 않는 지점들이 위,아래,오른쪽,왼쪽으로 인접. 그 크기가 최대인 영역
(인접한 영역)

물에 잠기지 않는 영역의 최대 개수는?
"""
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
maps = []
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().rstrip().split())))

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def solution(maps):
    answer = []

    for h in range(1, 101):
        visited = [[False for _ in range(n)] for _ in range(n)]
        number = 0
        for x in range(n):
            for y in range(n):
                if not visited[x][y] and maps[x][y] > h:
                    bfs(maps, h, x, y, visited)
                    number += 1
                    answer.append(number)


    return max(answer) if len(answer) else 1


def bfs(maps, h, x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if visited[nx][ny]:
                continue

            if maps[nx][ny] > h:
                queue.append((nx, ny))
                visited[nx][ny] = True


print(solution(maps))
