"""
입력
5
2 3 1 2 2

출력
2
"""
n = int(input())
array = list(map(int, input().split()))

result = 0
pain_total = 0


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
      array[right], array[pivot] = array[pivot], array[right]
    else:
      array[right], array[left] = array[left], array[right]

  quick_sort_asc(array, 0, right - 1)
  quick_sort_asc(array, right + 1, end)


quick_sort_asc(array, 0, len(array) - 1)


for data in array:
  pain_total += data
  if pain_total >= n:
    result += 1
    pain_total = 0

print(result)