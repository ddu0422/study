"""
입력
3
15
27
12

출력
27 15 12
"""
# 사전 준비
from copy import deepcopy

n = int(input())
array = []

for _ in range(n):
  array.append(int(input()))

# 문제풀이
## 선택 정렬 (selection sort)
def selection_sort(array):
  for i in range(len(array)):
    max_index = i
    for j in range(i + 1, len(array)):
      if array[max_index] < array[j]:
        max_index = j
    array[i], array[max_index] = array[max_index], array[i]

  return array

print(selection_sort(deepcopy(array)))

## 삽입 정렬 (insertion sort)
def insertion_sort(array):
  for i in range(1, len(array)):
    for j in range(i, 0, -1):
      if array[j] > array[j - 1]:
        array[j], array[j - 1] = array[j - 1], array[j]
      else:
        break

  return array

print(insertion_sort(deepcopy(array)))

## 퀵 정렬 (quick sort)
def quick_sort(array, start, end):
  if start >= end:
    return

  pivot = start
  left = start + 1
  right = end
  
  while left <= right:
    while left >= end and array[left] >= array[pivot]:
      left += 1
    
    while right > start and array[right] < array[pivot]:
      right -= 1

    if left >= right:
      array[pivot], array[right] = array[right], array[pivot]
    else:
      array[left], array[right] = array[right], array[left]

  quick_sort(array, start, right - 1)
  quick_sort(array, right + 1, end) 

  return array

print(quick_sort(deepcopy(array), 0, len(array) - 1))
