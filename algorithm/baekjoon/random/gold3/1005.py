import sys
from collections import deque

t = int(sys.stdin.readline().rstrip())

for _ in range(t):
    n, m = map(int, sys.stdin.readline().rstrip().split())
    cost = [0] + list(map(int, sys.stdin.readline().rstrip().split()))
    indegree = [0 for _ in range(n + 1)]
    graph = [[] for _ in range(n + 1)]

    for _ in range(m):
        x, y = map(int, sys.stdin.readline().rstrip().split())
        graph[x].append(y)
        indegree[y] += 1

    w = int(sys.stdin.readline().rstrip())


    def topology_sort(cost, indegree, graph, w):
        q = deque([])
        result = [0] * (n + 1)

        for i in range(1, n + 1):
            if not indegree[i]:
                q.append(i)
                result[i] = cost[i]
        
        while q:
            now = q.popleft()

            for i in graph[now]:
                indegree[i] -= 1
                result[i] = max(result[i], result[now] + cost[i])

                if not indegree[i]:
                    q.append(i)


        return result[w]


    print(topology_sort(cost, indegree, graph, w))
