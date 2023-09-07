"""
N x N 칸으로 이루어진 나무판에서 버섯 농사
버섯이 "자랄 수 있는 칸"과 버섯이 "자랄 수 없는 칸"이 있다.
M개의 버섯 포자를 가지고 있다. 버섯이 자랄 수 있는 칸에만 심을 수 있다.

포자가 심어진 칸을 포함해 최대 K개의 연결된 칸에 버섯을 자라게 한다. (상하좌우)

버섯 포자를 여러 개 겹쳐서 심을 수 있으며,
x개의 버섯 포자를 겹쳐 심으면 포자가 심어진 칸을 포함해 최대 x * K개의 연결된 칸에 버섯이 자란다.

버섯 포자를 심을 때 최소 개수로만 심으려고 한다.
농사가 가능할지 판단하고 남은 버섯 포자 개수를 출력

버섯 포자를 하나라도 사용하고 자랄 수 있는 모든 칸에 버섯이 전부 자랐을 때 농사가 가능하다고 정의한다.

버섯이 자랄 수 있는 칸: 0
버섯이 자랄 수 없는 칸: 1
"""
import sys
from collections import deque
from math import ceil

n, m, k = map(int, sys.stdin.readline().rstrip().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().rstrip().split())))
visited = [[False for _ in range(n)] for _ in range(n)]

dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def solution(maps, visited, k):
    result = []

    for x in range(n):
        for y in range(n):
            if not visited[x][y] and not maps[x][y]:
                result.append(bfs(maps, x, y, visited))

    result = sum([ceil(value / k) for value in result])

    if 0 < result <= m:
        print(*['POSSIBLE', m - result], sep="\n")
    else:
        print('IMPOSSIBLE')


def bfs(maps, x, y, visited):
    queue = deque([(x, y)])    
    visited[x][y] = True
    count = 1

    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < n and 0 <= ny < n):
                continue

            if visited[nx][ny] or maps[nx][ny]:
                continue

            queue.append((nx, ny))
            visited[nx][ny] = True
            count += 1

    return count


solution(maps, visited, k)
