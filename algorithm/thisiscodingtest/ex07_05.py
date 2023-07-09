"""
입력
5
8 3 7 9 2
3
5 7 9

출력
no yes yes
"""
# 사전 준비
n = int(input())
array = list(map(int, input().split()))[:n]
m = int(input())
targets = list(map(int, input().split()))[:m]


# 문제 풀이
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


quick_sort(array, 0, len(array) - 1)  


def binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    if array[mid] == target:
      return True
    elif array[mid] < target:
      start = mid + 1
    else:
      end = mid - 1
  
  return False


for target in targets:
  print('yes' if binary_search(array, target, 0, len(array) - 1) else 'no', end=' ')
print()
