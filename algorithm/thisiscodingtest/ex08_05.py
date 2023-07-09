"""
입력
2 15
2
3

출력
5

입력
3 4
3
5
7

출력
-1
"""
# 사전 준비
min_value = 987654321
n, m = map(int, input().split())
coins = []
d = [min_value] * 10001

for _ in range(n):
  coin = int(input())
  coins.append(coin)
  d[coin] = 1

# 문제 풀이
for coin in coins:
  for i in range(coin, m + 1):
    if d[i - coin] != min_value:
      d[i] = min(d[i], d[i - coin] + 1)

print(-1 if d[m] == min_value else d[m])