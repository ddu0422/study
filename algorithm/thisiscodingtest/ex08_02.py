"""
입력
26

출력
3
"""

# 사전 준비
x = int(input())
d = [0] * (x + 1)

# 문제 풀이
for i in range(2, x + 1):
  d[i] = d[i - 1] + 1

  if i % 5 == 0:
    d[i] = min(d[i], d[i // 5] + 1)

  if i % 3 == 0:
    d[i] = min(d[i], d[i // 3] + 1)

  if i % 2 == 0:
    d[i] = min(d[i], d[i // 2] + 1)

print(d[i])
