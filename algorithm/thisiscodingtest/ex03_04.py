# 사전 준비
n, k = map(int, input().split())
result = 0

# 문제 풀이
while n != 1:
  if n % k == 0:
    n //= k
  else:
    n -= 1
  result += 1

print(result)
