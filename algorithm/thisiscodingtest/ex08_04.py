"""
입력
3

출력
5
"""
# 사전 준비
n = int(input())
d = [0] * (n + 1)
d[1] = 1
d[2] = 3
mod = 796_796

# 문제 풀이
for i in range(3, n + 1):
  d[i] = (d[i - 1] + 2 * d[i - 2]) % mod

print(d[n])