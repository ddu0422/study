"""
세로의 길이 N
가로의 길이 M
RGB 색상의 이미를 담고 있다.

- 모든 픽셀에서 "세 가지 색상"을 "평균"내어 경게값 T보다 "크거나 같으면" 255, "작으면" 0으로 바꾼다.
- "255인 픽셀은 물체로 인식"한다.
- 값이 255인 픽셀들이 "상하좌우로 인접"해있다면 이 픽셀들은 "같은 물체로 인식"

물체가 총 몇 개 있는지 구하는 프로그램을 작성하시오.
"""
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().rstrip().split())))
t = int(sys.stdin.readline().rstrip())

dx = [-1, 0, 1 ,0]
dy = [0, -1, 0, 1]


def solution(maps, t):
    graphs = [[0 for _ in range(len(maps[0]) // 3)] for _ in range(len(maps))]
    visited = [[False for _ in range(len(graphs[0]))] for _ in range(len(graphs))]
    answer = 0

    # 평균으로 새로운 내용을 만든다.
    for i in range(0, len(maps[0]), 3):
        for j in range(len(maps)):
            average = (maps[j][i] + maps[j][i + 1] + maps[j][i + 2]) // 3
            graphs[j][i // 3] = 255 if average >= t else 0

    for i in range(len(graphs)):
        for j in range(len(graphs[0])):
            if not visited[i][j] and graphs[i][j] == 255:
                bfs(graphs, i, j, visited)
                answer += 1

    return answer


def bfs(graphs, x, y, visited):
    queue = deque([(x, y)])
    visited[x][y] = True

    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            if not (0 <= nx < len(graphs) and 0 <= ny < len(graphs[0])):
                continue

            if visited[nx][ny] or not graphs[nx][ny]:
                continue

            visited[nx][ny] = True
            queue.append((nx, ny))


print(solution(maps, t))
