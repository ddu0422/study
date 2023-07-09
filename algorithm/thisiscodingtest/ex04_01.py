# 사전 준비
n = int(input())
inputs = list(input().split())
commands = {
  'R': (0, 1),
  'L': (0, -1),
  'U': (-1, 0),
  'D': (1, 0)
}

y, x = 1, 1

# 문제 풀이
for input in inputs:
  dy, dx = commands[input]
  ny = y + dy
  nx = x + dx

  if 0 < nx <= n and 0 < ny <= n:
    y, x = ny, nx

print(y, x)
