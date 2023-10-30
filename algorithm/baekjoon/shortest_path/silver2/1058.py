import sys

INF = 1e9

n = int(sys.stdin.readline().rstrip())
graph = [[INF] * (n + 1) for _ in range(n + 1)]

for i in range(1, n + 1):
    for j in range(1, n + 1):
        if i == j:
            graph[i][j] = 0

for i in range(1, n + 1):
    text = sys.stdin.readline().rstrip()
    for j in range(1, n + 1):
        if text[j - 1] == 'Y':
            # 친구 관계 (양방향)
            graph[i][j] = 1
            graph[j][i] = 1

for k in range(1, n + 1):
    for i in range(1, n + 1):
        for j in range(1, n + 1):
            # 2-친구가 되기 위한 조건
            if graph[i][k] + graph[k][j] <= 2:
                graph[i][j] = min(graph[i][j], graph[i][k] + graph[k][j])


# 가장 많은 2-친구의 수
max_result = 0

for i in range(1, n + 1):
    max_result = max(max_result, len(list(filter(lambda x: x != 0 and x != INF, graph[i]))))

print(max_result)
