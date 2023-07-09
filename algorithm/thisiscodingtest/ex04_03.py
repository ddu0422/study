# 사전 준비
position = input()
column, row = ord(position[0]) - ord('a') + 1, int(position[1])

dx = [2, 1, -1, -2, -2, -1, 1, 2]
dy = [1, 2, 2, 1, -1, -2, -2, -1]
result = 0

# 문제 풀이
for i in range(len(dx)):
  nx = column + dx[i]
  ny = row + dy[i]

  if 1 <= nx <= 8 and 1 <= ny <= 8:
    result += 1

print(result)
