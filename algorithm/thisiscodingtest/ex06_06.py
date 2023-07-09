"""
입력
2
홍길동 95
이순신 77

출력
이순신 홍길동
"""
# 사전 준비
n = int(input())
array = []

for _ in range(n):
  line = input().split()
  name, score = line[0], int(line[1])
  array.append((name, score))

array.sort(key=lambda x: x[1])

for line in array:
  print(line[0], end=' ')
print()