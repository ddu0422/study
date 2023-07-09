# 사전 준비
n, m, k = map(int, input().split())
result = 0
array = list(map(int, input().split()))[:n]

# 문제 풀이
remains = m % k
max_count = m - remains

array.sort(reverse=True)

large_number = array[0]
second_large_number = array[1]

result = large_number * max_count + second_large_number * remains
print(result)
