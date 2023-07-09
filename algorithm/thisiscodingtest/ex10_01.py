"""
입력
6 4
1 4
2 3
2 4
5 6

출력
각 원소가 속한 집합: 1 1 1 1 5 5
부모 테이블: 1 1 2 1 5 5
"""

v, e = map(int, input().split())
parent = [i for i in range(v + 1)]


def find_parant(parent, x):
  if parent[x] != x:
    return find_parant(parent, parent[x])
  return x


def union_parent(parent, a, b):
  a = find_parant(parent, a)
  b = find_parant(parent, b)

  # 작은 숫자가 큰 숫자의 부모로 설정
  if a < b:
    parent[b] = a
  else:
    parent[a] = b


for i in range(e):
  a, b = map(int, input().split())
  union_parent(parent, a, b)

print('각 원소가 속한 집합: ', end='')
for i in range(1, v + 1):
  print(find_parant(parent, i), end=' ')
print()

print('부모 테이블: ', end='')
for i in range(1, v + 1):
  print(parent[i], end=' ')
print()