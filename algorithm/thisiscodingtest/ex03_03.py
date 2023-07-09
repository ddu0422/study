# 사전 준비
n, m = map(int, input().split())
maps = []
result = 0

for _ in range(n):
  numbers = list(map(int, input().split()))[:m]
  maps.append(numbers)

# 문제 풀이
min_list = []

for row in maps:
  min_list.append(min(row))

print(max(min_list))
