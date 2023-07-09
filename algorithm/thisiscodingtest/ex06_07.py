"""
입력
5 3
1 2 5 4 3
5 5 6 6 5

출력
26
"""
# 사전 준비
n, k = map(int, input().split())
a = list(map(int, input().split()))[:n]
b = list(map(int, input().split()))[:n]

# 문제 풀이
## A asc
## B desc
## k번만큼 swap
## sum A

def quick_sort_asc(array, start, end):
  if start >= end:
    return

  pivot = start
  left = start + 1
  right = end

  while left <= right:
    while left <= end and array[left] <= array[pivot]:
      left += 1

    while right > start and array[right] > array[pivot]:
      right -= 1

    if left >= right:
      array[pivot], array[right] = array[right], array[pivot]
    else:
      array[left], array[right] = array[right], array[left]
    
  
  quick_sort_asc(array, start, right - 1)
  quick_sort_asc(array, right + 1, end)

  return array


def quick_sort_desc(array, start, end):
  if start >= end:
    return
  
  pivot = start
  left = start + 1
  right = end

  while left <= right:
    while left <= end and array[left] >= array[pivot]:
      left += 1

    while right > start and array[right] < array[pivot]:
      right -= 1

    if left >= right:
      array[pivot], array[right] = array[right], array[pivot]
    else:
      array[left], array[right] = array[right], array[left]

  quick_sort_desc(array, 0, right - 1)
  quick_sort_desc(array, right + 1, end)
    
  return array

quick_sort_asc(a, 0, len(a) - 1)
quick_sort_desc(b, 0, len(b) - 1)

for i in range(k):
  a[i], b[i] = b[i], a[i]

print(sum(a))