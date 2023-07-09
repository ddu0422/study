"""
입력
4 6
19 15 10 17

출력
15
"""
# 사전 준비
n, m = map(int, input().split())
heights = list(map(int, input().split()))[:n]


def quick_sort(array, start, end):
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

  quick_sort(array, start, right - 1)
  quick_sort(array, right + 1, end)


quick_sort(heights, 0, len(heights) - 1)

# start: 0, end: max(array)
def binary_search(array, target, start, end):
  result = 0

  while start <= end:
    length = 0
    mid = (start + end) // 2
    
    for value in array:
      if value > mid:
        length += value - mid
    
    if length >= target:
      start = mid + 1
      result = mid
    else:
      end = mid - 1
  
  return result

 
print(binary_search(heights, m, 0, max(heights)))