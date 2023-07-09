"""
입력
5 3
1 3 2 3 2

출력
8

입력
8 5
1 5 4 3 2 4 5 2

출력
25
"""
# 사전 준비
n, m = map(int, input().split())
weights = list(map(int, input().split()))
result = 0

# 문제 풀이
for i in range(len(weights)):
  for j in range(i + 1, len(weights)):
    if weights[i] != weights[j]:
      result += 1 

print(result)