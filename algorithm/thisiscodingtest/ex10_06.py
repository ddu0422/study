"""
입력
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1

출력
NO
NO
YES
"""
# 사전 준비
n, m = map(int, input().split())
parent = [i for i in range(n + 1)]


# 문제풀이
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


for _ in range(m):
  x, a, b = map(int, input().split())
  if x == 0:
    union_parent(parent, a, b)
  elif x == 1:
    print('YES' if find_parent(parent, a) == find_parent(parent, b) else 'NO')
      