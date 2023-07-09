array = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
target = 3


def repeat_binary_search(array, target, start, end):
  while start <= end:
    mid = (start + end) // 2

    if array[mid] == target:
      return mid
    elif array[mid] > target:
      end = mid - 1
    else:
      start = mid + 1
  
  return None


print(repeat_binary_search(array, target, 0, len(array) - 1))