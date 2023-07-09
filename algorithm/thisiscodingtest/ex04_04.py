# 사전 준비
n, m = map(int, input().split())
a, b, direction = map(int, input().split())
maps = []

for _ in range(n):
  row = list(map(int, input().split()))
  maps.append(row)

# 북동남서
da = [-1, 0, 1, 0]
db = [0, 1, 0, -1]

turn_count = 0
result = 0

# 문제 풀이
## 첫 위치는 이동한 것으로 처리
maps[a][b] = 2
result += 1

def turn_left():
  global direction, turn_count

  direction -= 1
  if direction == -1:
    direction = 3

  turn_count += 1

while True:
  turn_left()

  na = a + da[direction]
  nb = b + db[direction]

  if maps[na][nb] == 0:
    turn_count = 0
    a, b = na, nb
    maps[a][b] = 2
    result += 1
    continue

  if turn_count == 4:
    na = a - da[direction]
    nb = b - db[direction]

    if maps[na][nb] == 1:
      break
    else:
       a, b = na, nb
       turn_count = 0

print(result)