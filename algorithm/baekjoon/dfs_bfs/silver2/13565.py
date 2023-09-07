"""
검은색 -> 전류 차단 (1)
흰색 -> 전류 통함  (0)

위쪽에서 전류 공급 상하좌우로 전달
아래쪽까지 전류가 공급될 수 있는지 판단하는 프로그램
"""
import sys
from collections import deque

n, m = map(int, sys.stdin.readline().rstrip().split())
maps = []
for _ in range(n):
    maps.append(list(map(int, sys.stdin.readline().rstrip())))


dx = [-1, 0, 1, 0]
dy = [0, -1, 0, 1]


def solution(maps):
    graphs = [[0 for _ in range(m)] for _ in range(n)]
    queue = deque([])

    # 첫 줄에서 전기가 통하는 칸을 찾는다.
    for i in range(len(maps[0])):
        if not maps[0][i]:
            queue.append((0, i))
            graphs[0][i] = 1

    while queue:
        x, y = queue.popleft()

        for i in range(len(dx)):
            nx = x + dx[i]
            ny = y + dy[i]

            # 범위를 벗어나 경우
            if not (0 <= nx < n and 0 <= ny < m):
                continue

            # 전류가 통하지 않는 경우
            if maps[nx][ny]:
                continue

            # 이미 지나온 길인 경우
            if graphs[nx][ny]:
                continue

            graphs[nx][ny] = graphs[x][y] + 1
            queue.append((nx, ny))

    # 마지막 줄에 전기가 통하는 구간이 하나라도 있는 경우
    for i in range(len(maps[0])):
        if graphs[len(maps) - 1][i]:
            return 'YES'

    # 마지막 줄에 전기가 통하느 구간이 하나도 없는 경우
    return 'NO'


print(solution(maps))
