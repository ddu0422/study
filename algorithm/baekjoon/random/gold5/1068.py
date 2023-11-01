import sys

n = int(sys.stdin.readline().rstrip())
nodes = [[] for _ in range(n)]
parent = list(map(int, sys.stdin.readline().rstrip().split()))
m = int(sys.stdin.readline().rstrip())

visited = [False] * n
visited[m] = True

roots = []

for index, value in enumerate(parent):
    # 제거할 노드이므로 애초부터 넣지 않음
    if index == m:
        continue

    if value == -1:
        roots.append(index)
        continue
    nodes[value].append(index)


def dfs(graph, start, visited, result):
    # 이미 방문한 경우라면(or 삭제 처리된 경우라면) 더 이상 탐색하지 않고 종료
    if visited[start]:
        return

    # Leaf Node인 경우 종료
    if not len(graph[start]):
        result.append(True)
        return

    visited[start] = True

    for v in graph[start]:
        if not visited[v]:
            dfs(graph, v, visited, result)

result = []

for root in roots:
    dfs(nodes, root, visited, result)

print(len(result))
