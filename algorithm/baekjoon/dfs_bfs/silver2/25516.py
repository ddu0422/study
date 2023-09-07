"""
n개의 정점 / n - 1개의 간선
번호는 0부터 n - 1까지
0번 정점이 루트 / 모든 간선의 길이는 1

각 정점에는 사과가 0개 또는 1개 놓여있다.
루트 노드에서 거리가 k이하인 노드에 있는 사과를 수확하려고 한다.
수확할 수 있는 사과 개수를 출력하자.

0(1) - 1 - 3(1)
         ㄴ 4
     ㄴ 2 - 5(1)
         ㄴ 6 - 7(1)

0, 3, 5 => 2개
"""
import sys
from collections import deque

n, k = map(int, sys.stdin.readline().rstrip().split())
nodes = [[] for _ in range(n + 1)]
for _ in range(n - 1):
    a, b = map(int, sys.stdin.readline().rstrip().split())
    nodes[a].append(b)
    nodes[b].append(a)
distance = [-1] * (n + 1)
apples = list(map(int, sys.stdin.readline().rstrip().split()))


def solution(nodes, distance, k, apples):
    answer = 0
    queue = deque([0])
    distance[0] = 0

    while queue:
        now = queue.popleft()

        for v in nodes[now]:
            if distance[v] == -1:
                distance[v] = distance[now] + 1
                queue.append(v)
    
    for index, value in enumerate(distance):
        if -1 < value <= k and apples[index]:
            answer += 1
        
    return answer


print(solution(nodes, distance, k, apples))
