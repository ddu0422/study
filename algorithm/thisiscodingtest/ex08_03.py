"""
입력
4
1 3 1 5

출력
8
"""
# 사전 준비
n = int(input())
foods = [0] + list(map(int, input().split()))
stiils = [0] * (n + 1)

stiils[1] = foods[1]

for i in range(2, n + 1):
  stiils[i] = max(foods[i], foods[i - 2] + foods[i])

print(stiils[n])