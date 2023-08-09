def solution(arr):
    arr.remove(min(arr))
    return arr if arr else [-1]


arr = [1, 2, 3, 4]
print(solution(arr))