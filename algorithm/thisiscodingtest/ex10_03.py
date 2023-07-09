"""
입력
3 3
1 2
1 3
2 3

출력
사이클이 발생했습니다.
"""
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]


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


cycle = False

for _ in range(m):
  a, b = map(int, input().split())
  if find_parent(parent, a) == find_parent(parent, b):
    cycle = True
    break
  union_parent(parent, a, b)

print("사이클이 발생했습니다." if cycle else "사이클이 발생하지 않았습니다.")
