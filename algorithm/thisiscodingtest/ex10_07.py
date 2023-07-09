"""
입력
7 12
1 2 3
1 3 2
3 2 1
2 5 2
3 4 4
7 3 6
5 1 5
1 6 2
6 4 1
6 5 3
4 5 3
6 7 4

출력
8
"""
# 사전 준비
n, m = map(int, input().split())
edges = []
parent = [i for i in range(n + 1)]

for _ in range(m):
  a, b, c = map(int, input().split())
  edges.append((c, a, b))

edges.sort()

# 문제 풀이
def find_parent(parent, x):
  if parent[x] != x:
    parent[x] = find_parent(parent, parent[x])
  return parent[x]


def union_parent(parent, a, b):
  a = find_parent(parent, a)
  b = find_parent(parent, b)

  if a < b:
    parent[b] = a
  else:
    parent[a] = b

# result = []
# better
result = 0
last = 0 # 비용 기준 오름차순으로 정렬했기 때문에 마지막 비용을 빼면 된다.

for edge in edges:
  c, a, b = edge

  if find_parent(parent, a) != find_parent(parent, b):
    union_parent(parent, a, b)
    # result.append(c)
    result += c
    last = c

# print(sum(result) - max(result))
print(result - last)