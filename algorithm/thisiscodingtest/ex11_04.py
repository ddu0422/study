"""
입력
5
3 2 1 1 9

출력
8
"""
# 사전 준비
n = input()
coins = list(map(int, input().split()))
result = [-1] * (1_000_000 + 1)

# 문제 풀이
