"""
할아버지 - 아버지 - 나
ㄴ  1촌 ㄱㄴ  1촌  ㄱ
ㄴ      2촌      ㄱ

두 사람의 촌수를 계산하는 프로그램

9 (전체 사람의 수)
7 3 (촌수를  계산해야 하는 서로 다른 두 사람의 번호)
7   (부모 자식들 간의 관계의 수)

1 2
1 3
2 7
2 8
2 9
4 5
4 6

1 - 2  - 7
       ㄴ 8
       ㄴ 9
  ㄴ 3

4 - 5
  ㄴ 6

친척 관계가 없는 경우 -1
"""
import sys
from collections import deque

n = int(sys.stdin.readline().rstrip())
a, b = map(int, sys.stdin.readline().rstrip().split())
m = int(sys.stdin.readline().rstrip())
nodes = [[] for _ in range(n + 1)]
for _ in range(m):
    x, y = map(int, sys.stdin.readline().rstrip().split())
    nodes[x].append(y)
    nodes[y].append(x)
visited = [False] * (n + 1)


def solution(a, b, nodes, visited):
    queue = deque([a])
    visited[a] = True
    relatives = [0] * len(visited)

    while queue:
        now = queue.popleft()

        for v in nodes[now]:
            if not visited[v]:
                visited[v] = True
                queue.append(v)
                relatives[v] = relatives[now] + 1

    return relatives[b] if visited[b] else -1


print(solution(a, b, nodes, visited))
